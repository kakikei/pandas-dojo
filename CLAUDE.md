# CLAUDE.md

このファイルは、このリポジトリでClaude Code (claude.ai/code) が作業する際のガイダンスを提供します。

## プロジェクト概要

Pandas Dojoは、Pandasライブラリ（Pythonのデータ分析ライブラリ）をマスターするためのインタラクティブなブラウザベース学習アプリケーションです。ユーザーはCodeMirrorエディタでPandasの問題を解き、Flaskバックエンド経由でコードを実行し、自動検証フィードバックを受け取ります。

## 開発コマンド

### Docker を使用する場合（推奨）

#### アプリケーション全体を起動
```bash
docker compose up
```
バックエンドは `http://localhost:5000`、フロントエンドは `http://localhost:8000` で起動します。

#### バックグラウンドで起動
```bash
docker compose up -d
```

#### ログを確認
```bash
docker compose logs -f
```

#### コンテナを停止
```bash
docker compose down
```

#### イメージを再ビルド
```bash
docker compose build
```

### ローカル環境で直接実行する場合

#### 初期セットアップ
```bash
pip install -r requirements.txt
```

#### バックエンドサーバーの起動
```bash
cd backend
python app.py
```
サーバーは `http://localhost:5000` で起動し、Flaskのデバッグモードが有効になります。

#### フロントエンドサーバーの起動
```bash
cd frontend
python -m http.server 8000
```
`http://localhost:8000` でアプリケーションにアクセスできます。

アプリケーションを動作させるには、両方のサーバーを同時に起動する必要があります。

## アーキテクチャ

### リクエストフロー

1. **問題の読み込み**: フロントエンドが `GET /api/problems` から問題リストを取得し、サイドバーに表示
2. **問題の選択**: ユーザーが問題をクリック → フロントエンドが `GET /api/problems/<id>` から詳細を取得
3. **コードの実行**: ユーザーがコードを記述 → フロントエンドが `{code, problem_id}` を `/api/execute` にPOST
4. **バックエンド処理**:
   - [backend/problems.py](backend/problems.py) から問題定義を読み込み
   - CSVデータセットを `df` 変数に読み込み
   - `pd`, `np`, `df` を含むnamespace内で `exec()` によりユーザーコードを実行
   - 問題の検証ルールに対して結果を検証
   - `{success, output, error, is_correct, feedback}` を返却
5. **結果の表示**: フロントエンドが実行結果と検証フィードバックを表示

### バックエンドコンポーネント

**[backend/app.py](backend/app.py)** - 3つのエンドポイントを持つFlask REST API（CORS有効）

**[backend/code_executor.py](backend/code_executor.py)** - コア実行エンジン:
- `io.StringIO()` リダイレクトを使用してstdoutをキャプチャ
- 制御されたnamespace内でコードを実行（完全にサンドボックス化されていない - 教育目的のみ）
- `validate_solution()` を使用して検証: 変数の存在、型、カスタム検証関数をチェック

**[backend/problems.py](backend/problems.py)** - 問題定義の配列:
- 各問題は以下を持つ: `id`, `title`, `description`, `hint`, `dataset`, `initial_code`, `validation`
- 検証ルールは以下を指定: `variable` (チェックする変数名), `type` (DataFrame/Series), `expected_value`, または `check_function` (ラムダ)
- `get_all_problems()` はフロントエンドに送信する前に検証関数を除外（セキュリティ）

**[backend/datasets/](backend/datasets/)** - コード実行時にDataFrameとして読み込まれるCSVファイル

### フロントエンドコンポーネント

**[frontend/app.js](frontend/app.js)** - Vanilla JavaScriptアプリケーション:
- CodeMirrorをPythonモードとMonokaiテーマで初期化
- 問題選択とエディタの状態を管理
- バックエンドへの非同期API呼び出しを処理
- 検証結果に基づいて成功/エラーのスタイリングを表示

### 実行時のNamespace

ユーザーコードが実行される際、namespaceには以下が含まれます:
- `pd` - pandasモジュール
- `np` - numpyモジュール
- `df` - 問題のCSVデータセットから読み込まれたDataFrame
- `__builtins__` - 標準のPython組み込み関数
- ユーザーコードは問題で指定された変数（通常は `result`）に結果を格納する必要があります

## 新しい問題の追加

[backend/problems.py](backend/problems.py) の `PROBLEMS` リストに追加:

```python
{
    'id': 9,
    'title': '問題のタイトル',
    'description': 'ユーザーに表示されるタスクの説明',
    'hint': '役立つヒント',
    'dataset': 'filename.csv',  # backend/datasets/ に存在する必要がある
    'initial_code': '# 初期テンプレート\nresult = ',
    'validation': {
        'variable': 'result',           # 検証する変数名
        'type': 'DataFrame',            # オプション: 'DataFrame' または 'Series'
        'check_function': lambda x: ... # カスタム検証ロジック
    }
}
```

対応するCSVを [backend/datasets/](backend/datasets/) に追加してください。

## 検証システム

[backend/code_executor.py](backend/code_executor.py) における3つの検証アプローチ:

1. **型チェック**: 結果がDataFrameまたはSeriesであることを検証
2. **期待値との比較**: `.equals()` を使用して `expected_value` と照合
3. **カスタム関数**: ラムダ関数が結果を受け取り、True/Falseを返却

各パターンの例については、[backend/problems.py](backend/problems.py) の既存の問題を参照してください。

## APIの手動テスト

```bash
curl -X POST http://localhost:5000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "result = df.head()", "problem_id": 1}'
```

レスポンスには検証に基づく `is_correct` と `feedback` フィールドが含まれます。

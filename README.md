# Pandas Dojo

Pandasをマスターするためのブラウザベース学習アプリ

## 概要

Pandas Dojoは、Pythonの人気データ分析ライブラリ「Pandas」を実践的に学習できるインタラクティブなWebアプリケーションです。ブラウザ上でコードを書いて実行し、即座にフィードバックを得ることができます。

## 機能

- ブラウザベースのコードエディター（CodeMirror使用）
- リアルタイムでのコード実行
- 自動正誤判定機能
- 段階的な学習問題（基礎から応用まで）
- サンプルデータセットの自動提供
- 詳細なフィードバックとヒント

## プロジェクト構成

```
panda-dojo/
├── backend/              # バックエンド（Flask API）
│   ├── app.py            # APIサーバー
│   ├── problems.py       # 問題定義
│   ├── code_executor.py  # コード実行エンジン
│   └── datasets/         # サンプルデータセット
│       ├── sales_data.csv
│       └── sales_data_with_nan.csv
├── frontend/             # フロントエンド
│   ├── index.html        # メインHTML
│   ├── style.css         # スタイル
│   └── app.js            # JavaScriptロジック
├── requirements.txt      # Python依存関係
└── README.md             # このファイル
```

## セットアップ手順

### 方法1: Docker を使用する（推奨）

#### 必要な環境
- Docker
- Docker Compose
- モダンなWebブラウザ（Chrome, Firefox, Safari, Edgeなど）

#### 起動方法

1. **アプリケーション全体を起動**

```bash
$ docker compose up
```

または、バックグラウンドで起動する場合：

```bash
$ docker compose up -d
```

2. **ブラウザでアクセス**

- フロントエンド: `http://localhost:8000`
- バックエンドAPI: `http://localhost:5000`

3. **停止方法**

```bash
$ docker compose down
```

4. **ログの確認**

```bash
$ docker compose logs -f
```

#### 利点
- Python環境のインストール不要
- 依存関係の自動解決
- 環境の再現性が高い
- コードの変更が自動的に反映される（ホットリロード）

### 方法2: ローカル環境で直接実行する

#### 1. 必要な環境

- Python 3.8以上
- pip
- モダンなWebブラウザ（Chrome, Firefox, Safari, Edgeなど）

#### 2. 依存関係のインストール

```bash
$ pip install -r requirements.txt
```

#### 3. バックエンドサーバーの起動

```bash
$ cd backend
$ python app.py
```

サーバーが起動すると、`http://localhost:5000` でAPIが利用可能になります。

#### 4. フロントエンドの起動

別のターミナルウィンドウで：

```bash
$ cd frontend
$ python -m http.server 8000
```

ブラウザで `http://localhost:8000` にアクセスしてください。

## 使い方

1. ブラウザで `http://localhost:8000` を開く
2. 左サイドバーから問題を選択
3. コードエディターに解答を入力
4. 「実行」ボタンをクリック
5. 実行結果と正誤判定を確認
6. 必要に応じて「リセット」ボタンでコードを初期状態に戻す

## 問題一覧

現在、以下の問題が用意されています：

1. **DataFrameの基本操作** - head()メソッドの使用
2. **列の選択** - 特定の列の取得
3. **データのフィルタリング** - 条件に基づくデータ抽出
4. **集計関数の使用** - 平均値の計算
5. **グループ化と集計** - groupby()の使用
6. **新しい列の追加** - 計算列の作成
7. **ソート** - データの並べ替え
8. **欠損値の処理** - NaNの処理

## 技術スタック

### バックエンド
- **Flask**: PythonのWebフレームワーク
- **Flask-CORS**: CORS対応
- **Pandas**: データ分析ライブラリ
- **NumPy**: 数値計算ライブラリ

### フロントエンド
- **HTML5/CSS3**: 基本構造とスタイル
- **JavaScript**: アプリケーションロジック
- **CodeMirror**: コードエディター

## カスタマイズ

### 新しい問題の追加

`backend/problems.py` ファイルの `PROBLEMS` リストに新しい問題を追加できます：

```python
{
    'id': 9,
    'title': '問題のタイトル',
    'description': '問題の説明',
    'hint': 'ヒント',
    'dataset': 'データセットファイル名.csv',
    'initial_code': '# 初期コード\n',
    'validation': {
        'variable': '結果を格納する変数名',
        'type': 'DataFrame',  # または 'Series'
        'check_function': lambda x: # 検証関数
    }
}
```

### 新しいデータセットの追加

`backend/datasets/` ディレクトリにCSVファイルを追加し、問題定義で参照できます。

## トラブルシューティング

### バックエンドサーバーに接続できない

- バックエンドサーバーが起動しているか確認してください
- ポート5000が使用可能か確認してください
- ファイアウォールの設定を確認してください

### CORS エラーが発生する

- Flask-CORSが正しくインストールされているか確認してください
- `backend/app.py` で CORS が有効になっているか確認してください

## 今後の拡張案

- ユーザー認証機能
- 進捗管理機能
- より多くの問題追加
- 難易度別の問題フィルター
- コードの保存機能
- ランキング機能

## ライセンス

MIT License

## 貢献

プルリクエストを歓迎します！バグ報告や機能リクエストは Issues でお願いします。

## 開発者

Pandas Dojoプロジェクトチーム

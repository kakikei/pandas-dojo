# Python 3.13を使用
FROM python:3.13-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# ビルドツールを一時的にインストールし、依存関係をインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc g++ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# アプリケーションファイルをコピー
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# ポート5000と8000を公開
EXPOSE 5000 8000

# 環境変数を設定
ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development

# デフォルトコマンド（バックエンドサーバーを起動）
CMD ["python", "backend/app.py"]

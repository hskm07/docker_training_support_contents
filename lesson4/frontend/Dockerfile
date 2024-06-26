# ベースイメージの指定
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルのコピー
COPY . /app

# コンテナ起動時に実行されるコマンドを設定
CMD ["python", "app.py"]

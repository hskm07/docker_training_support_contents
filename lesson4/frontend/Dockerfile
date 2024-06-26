# ベースイメージの指定
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションファイルのコピー
COPY . /app

# ストリームリットを外部アクセス可能にするための設定
EXPOSE 8501

# アプリケーションの起動
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

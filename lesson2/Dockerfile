FROM python:3.8
WORKDIR /usr/src/app

ENV FLASK_APP=app

COPY /app/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /app ./


# ポートの公開
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

# コンテナ起動時にapp.pyを実行
CMD ["python", "app.py"]

FROM python:3.10-slim-bullseye
WORKDIR /usr/src/app

ENV FLASK_APP=app

COPY /app/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /app ./


# ポートの公開
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

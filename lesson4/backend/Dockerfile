# ビルドステージ
FROM golang:1.18 as builder

WORKDIR /app

# Goモジュールファイルをコピー
COPY go.mod go.sum ./
# 依存関係をダウンロード
RUN go mod download

# ソースコードをコピー
COPY . .

# 依存関係を整理し、go.sumを更新
RUN go mod tidy

# バイナリをビルド
RUN go build -o main .

ENV CGO_ENABLED=0 \
  GOOS=linux \
  GOARCH=amd64

EXPOSE 8080

CMD ["go", "run", "main.go"]

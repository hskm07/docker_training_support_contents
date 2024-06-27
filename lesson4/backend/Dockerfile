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

# 実行ステージ
FROM alpine:latest

WORKDIR /app

# ビルドしたバイナリをコピー
COPY --from=builder /app/main .

# ポートを公開
EXPOSE 8080

# バイナリを実行
CMD ["./main"]

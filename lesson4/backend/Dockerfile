FROM golang:1.19 as builder

WORKDIR /app

# ソースコードをコピー
COPY main.go .

# Goモジュールを初期化し、依存関係を整理
RUN go mod init main \
 && go mod tidy

# バイナリをビルド
RUN go build -o main .

# 実行ステージ
FROM golang:1.19

WORKDIR /app

# ビルドしたバイナリをコピー
COPY --from=builder /app/main /app/main

# ポートを公開
EXPOSE 8080

# バイナリを実行
CMD ["./main"]

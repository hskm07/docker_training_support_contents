FROM golang:1.18

WORKDIR /app

# Goモジュールファイルをコピー
COPY go.mod go.sum ./
# 依存関係をダウンロード
RUN go mod download

# ソースコードをコピー
COPY . .

# 依存関係を整理し、go.sumを更新
RUN go mod tidy

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]

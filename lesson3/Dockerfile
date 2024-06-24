# 第一ステージ: ビルド環境
FROM rust:1.57 as builder

# 必要なツールをインストール
RUN apt-get update && apt-get install -y pkg-config libssl-dev && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# Rustの依存関係をキャッシュするためにCargo.tomlとCargo.lockをコピー
COPY Cargo.toml ./

# 依存関係を解決
RUN cargo fetch

# アプリケーションのソースコードをコピー
COPY src ./src

# アプリケーションをビルド
RUN cargo build --release

# 第二ステージ: 実行環境
FROM debian:buster-slim

# 必要な依存関係をインストール
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

# 非rootユーザーを作成
RUN useradd -m myuser

# 作業ディレクトリを設定
WORKDIR /home/myuser/

# 第一ステージからビルド済みバイナリをコピー
COPY --from=builder /app/target/release/my_rust_cli .

# 権限を変更
RUN chown myuser:myuser my_rust_cli

# 非rootユーザーに切り替え
USER myuser

# アプリケーションを実行
CMD ["./my_rust_cli"]

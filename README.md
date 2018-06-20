# nginx-gunicorn-django-postgres

# やったこと
## nginx
### 証明書
- certsフォルダ内で以下のコマンドを実行
```
$ openssl genrsa 2048 > server.key
$ openssl req -new -key server.key > server.csr
$ openssl x509 -days 3650 -req -signkey server.key < server.csr > server.crt
```

### 設定ファイル
- デフォルトのnginx.confから以下を変更
    - 80番ポートのserver句を削除
    - ssl_certificateとssl_certificate_keyを同一ディレクトリに合わせる
    - /static/のlocationを追加
    - /のlocationにプロキシ設定を追加

## postgresql
### 設定ファイル
- デフォルトのpostgresql.confから以下を変更
    - timezone = 'Asia/Tokyo'
    - log_timezone = 'Asia/Tokyo'
    - `listen_addresses = '*'

## Django
- 通常のアプリケーション作成

## 初期化
```
# docker exec nginx-gunicorn-django-postgres_django_1 ./init.sh
```

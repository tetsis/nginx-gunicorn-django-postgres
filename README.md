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

# 起動方法
## nginx, Django, Postgresqlすべてコンテナで動かす場合
```
# docker-compose up -d
```

## 外部のPostgresqlに接続する場合
- Postgresqlサーバでは事前にユーザとデータベースを作成しておく
```
# su - postgres
-bash-4.2$ psql -c "CREATE ROLE django WITH LOGIN PASSWORD 'django';"
CREATE ROLE
-bash-4.2$ psql -c "CREATE DATABASE django OWNER django ENCODING 'utf8';"
CREATE DATABASE
-bash-4.2$ exit
```
- docker-command-without-postgres.ymlのdjangoコンテナの環境変数「DATABASE_HOST」にはPostgresqlサーバのアドレスを指定してから、以下のコマンドを実行する
```
# docker-compose -f docker-compose-without-postgres.yml up -d
```

# 初期化
```
# docker exec nginx-gunicorn-django-postgres_django_1 ./init.sh
```

# テスト
```
# python3.6 manage.py test
```

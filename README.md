# 日本学関連データベースリストのデータベースつくった

DockerとDocker-composeさえあれば動くデータベースです。
MySQLとFlaskで作っていて、APIでデータをJSON形式でゲットげきます。
APIはゲットのみ用意しました。
データベースに更新がある場合はCronでグーグルスプレッドシートのデータをとりにゆきます。


## データベースのインストールなど

まずgitなどでこのリポジトリをクローンしてください。
その後クローンしてきた最上位のフォルダに```.env```ファイルを作って必要な環境変数を作成してください。

```
MYSQL_DATABASE=[データベースのなまえ]
MYSQL_USER=[MySQLを操作するユーザー名]
MYSQL_PASSWORD=[ユーザーのパスワード]
MYSQL_ROOT_PASSWORD=[ルートユーザーのパスワード]
DB_HOST=[データベースのホスト名]
```

ファイルを作成したら、```docker-compose.yml```が入っているディレクトリにはいって、
docker-composeコマンドでイメージ・コンテナ作成、コンテナ起動を行ってください。
こんな感じ
```
$ cd ./db_app
$ docker-compose build
$ docker-compose up -d
```

ここには2つのコンテナが入っていて、一つがMySQL, 一つがFlaskのAPIを動かしています。
FlaskのはいったコンテナはMySQLのコンテナのヘルスチェックがすんでから起動するので、
少し時間がかかります。

## APIについて




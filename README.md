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
少し時間がかかります。(30秒くらい)
また、データベースが入っているコンテナのなかでcronをつかってデータべースを更新するので以下のコマンドでDockerに入り、
さらにcronを起動してください。

```
$ docker-compose exec mysql bash
# 以下コンテナ内から実行
$ sh /scripts/for_cron.sh
$ service cron start
```

cronジョブはデフォルトで毎週月曜の4時59分に動くようにしてあります。
そしてそれにあわせてbackendのコンテナを再起動させてあげてください。

```
# ホストのCronで

10 05 * * 0 docker-compose restart backend
```

無事起動したら、以下のURLでアクセスできるはず。
```
localhost:5000
```



APIについては以下を参照してください。


## APIについて


APIは以下の4つのクエリが可能です。
1. **localhost:5000/creator/all**

データベースを作成したすべての団体名を表示。

2. **localhost:5000/creator/search**

データベースを作成した団体を検索。

パラメータは以下のとうりです。

- id = 団体データのid
- name_ja = 団体の日本語名
- name_en = 団体の英語名
- altnames = その他の団体名

クエリの作り方・例
```
localhost:5000/creator/search?name_ja=国立&altnames=NDL
```

結果は20件ごとにページで区切って表示されます。
ページ指定、最高件数変更などは以下のパラメータでできます。

- page =　ページ指定
- per_page = ページあたりの最高件数

3. **localhost:5000/databaselist/all**

登録されたすべてのデータベース表示。

4. **localhost:5000/databaselist/search**

データべースの検索。
パラメータは以下のとうり。

- id = データベースのid
- title_ja = データベースの日本語タイトル
- title_en =　データベースの英語タイトル
- creator_id =　データベースを作成した団体のid
- ddc_category = データベースのDDCカテゴリ（3桁のアラビア数字を文字列として、たとえば"900"など）
- type = メディアタイプ
- description_ja =　データベースの日本語の説明
- description_en = データベースの英語の説明

結果は20件ごとにページで区切って表示されます。
ページ指定、最高件数変更などは以下のパラメータでできます。
- page =　ページ指定
- per_page = ページあたりの最高件数



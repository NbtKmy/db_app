#!/bin/bash

# テーブルの更新は現段階ではtruncateをつかってまるごと交換する。
# 数が増えたらまたいろいろ考える
truncateCreator = "TRUNCATE TABLE dblist.creator;"
truncateDatabase = "TRUNCATE TABLE dblist.databaselist;"

curl -L 'https://docs.google.com/spreadsheets/d/1WSswTgqGPhKslY4iDD4Z-ZqCP3Il6zV7kNQJVzRdwJw/export?format=csv&gid=0' -o /csv_temps/creator.csv
curl -L 'https://docs.google.com/spreadsheets/d/14YoKQgpIlIWQHrInwvs3w-SqnowpNMuXGRxZRZxRQxc/export?format=csv&gid=0' -o /csv_temps/database.csv

loadCreator="LOAD DATA LOCAL INFILE '/tmp/creator.csv' INTO TABLE creator FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
loadDB="LOAD DATA LOCAL INFILE '/tmp/database.csv' INTO TABLE databaselist FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES"

mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} --local-infile dblist -e"${truncateCreator}${truncateDatabase}${loadCreator}${loadDB}"


#!/bin/bash

curl -L 'https://docs.google.com/spreadsheets/d/1WSswTgqGPhKslY4iDD4Z-ZqCP3Il6zV7kNQJVzRdwJw/export?format=csv&gid=0' -o /docker-entrypoint-initdb.d/creator.csv
curl -L 'https://docs.google.com/spreadsheets/d/14YoKQgpIlIWQHrInwvs3w-SqnowpNMuXGRxZRZxRQxc/export?format=csv&gid=0' -o /docker-entrypoint-initdb.d/database.csv

mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --local-infile dblist -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/creator.csv' INTO TABLE creator FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES"
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD --local-infile dblist -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/database.csv' INTO TABLE database FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES"
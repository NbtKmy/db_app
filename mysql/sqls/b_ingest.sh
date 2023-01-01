#!/bin/bash

curl -L 'https://docs.google.com/spreadsheets/d/1WSswTgqGPhKslY4iDD4Z-ZqCP3Il6zV7kNQJVzRdwJw/export?format=csv&gid=0' -o '/docker-entrypoint-initdb.d/creator.csv'
curl -L 'https://docs.google.com/spreadsheets/d/14YoKQgpIlIWQHrInwvs3w-SqnowpNMuXGRxZRZxRQxc/export?format=csv&gid=0' -o '/docker-entrypoint-initdb.d/database.csv'

loadCreator="LOAD DATA LOCAL INFILE '/tmp/creator.csv' 
            INTO TABLE creator FIELDS TERMINATED BY ',' 
            OPTIONALLY ENCLOSED BY '\"' 
            LINES TERMINATED BY '\n' 
            IGNORE 1 LINES 
            (@id, @name_ja, @name_en, @geo, @altnames, @wikidata_id, @change_date) 
            SET 
            id = @id,
            name_ja = @name_ja,
            name_en = @name_en,
            geo = ST_GeomFromText(@geo),
            altnames = @altnames,
            wikidata_id = @wikidata_id,
            change_date = @change_date"

mysql -uroot -p${MYSQL_ROOT_PASSWORD} --local-infile dblist -e "$loadCreator"
mysql -uroot -p${MYSQL_ROOT_PASSWORD} --local-infile dblist -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/database.csv' INTO TABLE databaselist FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES"
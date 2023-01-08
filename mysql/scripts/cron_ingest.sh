#!/bin/bash

curl -L 'https://docs.google.com/spreadsheets/d/1WSswTgqGPhKslY4iDD4Z-ZqCP3Il6zV7kNQJVzRdwJw/export?format=csv&gid=0' -o /csv_temps/creator.csv
curl -L 'https://docs.google.com/spreadsheets/d/14YoKQgpIlIWQHrInwvs3w-SqnowpNMuXGRxZRZxRQxc/export?format=csv&gid=0' -o /csv_temps/database.csv

# テーブルの更新は現段階ではtruncateをつかってまるごと交換する。
# 数が増えたらまたいろいろ考える
truncateCreator = "TRUNCATE TABLE dblist.creator;"
truncateDatabase = "TRUNCATE TABLE dblist.databaselist;"



loadCreator="LOAD DATA LOCAL INFILE '/csv_temps/creator.csv' 
            INTO TABLE creator FIELDS TERMINATED BY ',' 
            OPTIONALLY ENCLOSED BY '\"' 
            LINES TERMINATED BY '\n' 
            IGNORE 1 LINES 
            (@id, @name_ja, @name_en, @geo, @altnames, @wikidata_id, @change_date) 
            SET 
            id = @id,
            name_ja = @name_ja,
            name_en = NULLIF(@name_en, ''),
            geo = IF( @geo = '', NULL, ST_GeomFromText(@geo, 4326)),
            altnames = NULLIF(@altnames, ''),
            wikidata_id = NULLIF(@wikidata_id, ''),
            change_date = @change_date;"

loadDB="LOAD DATA LOCAL INFILE '/csv_temps/database.csv'
        INTO TABLE databaselist FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '\"' 
        LINES TERMINATED BY '\n' 
        IGNORE 1 LINES
        (@id, @title_ja, @title_en, @creator_id, @ddc_category, @type, @description_ja, @description_en, @url, @change_date, @link_check) 
        SET
        id = @id,
        title_ja = @title_ja,
        title_en = NULLIF(@title_en, ''),
        creator_id = NULLIF(@creator_id, ''),
        ddc_category = @ddc_category,
        type = @type,
        description_ja = NULLIF(@description_ja, ''),
        description_en = NULLIF(@description_en, ''),
        url = @url,
        change_date = @change_date,
        link_check = @link_check"

mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} --local-infile dblist -e"${truncateCreator}${truncateDatabase}${loadCreator}${loadDB}"


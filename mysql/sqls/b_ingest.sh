#!/bin/bash

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
            change_date = @change_date"

loadDB="LOAD DATA LOCAL INFILE '/csv_temps/database.csv'
        INTO TABLE databaselist FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '\"' 
        LINES TERMINATED BY '\n' 
        IGNORE 1 LINES
        (@id, @title_ja, @title_en, @creator_id, @ddc_category, @media_type, @description_ja, @description_en, @url, @change_date, @link_check) 
        SET
        id = @id,
        title_ja = @title_ja,
        title_en = NULLIF(@title_en, ''),
        creator_id = NULLIF(@creator_id, ''),
        ddc_category = @ddc_category,
        media_type = @media_type,
        description_ja = NULLIF(@description_ja, ''),
        description_en = NULLIF(@description_en, ''),
        url = @url,
        change_date = @change_date,
        link_check = @link_check"


mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} --local-infile ${MYSQL_DATABASE} -e "${loadCreator}"
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} --local-infile ${MYSQL_DATABASE} -e "${loadDB}"


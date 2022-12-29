
mysql -uroot -pmysql --local-infile sada -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/data.csv' INTO TABLE masashi FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
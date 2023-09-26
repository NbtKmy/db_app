#!/bin/sh

createDatabase="CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};"
dropTableCreator="DROP TABLE IF EXISTS ${MYSQL_DATABASE}.creator;"
dropTableDatabase="DROP TABLE IF EXISTS ${MYSQL_DATABASE}.databaselist"


mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "${createDatabase}${dropTableCreator}${dropTableDatabase}"

createTableCreator="CREATE TABLE ${MYSQL_DATABASE}.creator (
  id varchar(16) NOT NULL NOT NULL UNIQUE,
  name_ja varchar(128) NOT NULL,
  name_en varchar(128),
  geo POINT,
  altnames varchar(256),
  wikidata_id varchar(32),
  change_date date NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

createTableDatabaselist="CREATE TABLE ${MYSQL_DATABASE}.databaselist (
  id varchar(16) NOT NULL UNIQUE,
  title_ja varchar(256) NOT NULL,
  title_en varchar(256),
  creator_id varchar(32),
  ddc_category varchar(128),
  media_type varchar(128),
  description_ja varchar(1024),
  description_en varchar(1024),
  url varchar(128) NOT NULL,
  change_date date NOT NULL,
  link_check varchar(2) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"


mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "${createTableCreator}${createTableDatabaselist}"

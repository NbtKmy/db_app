/* initlialization */
CREATE DATABASE IF NOT EXISTS dblist;
DROP TABLE IF EXISTS dblist.creator;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE dblist.creator (
  `id` varchar(16) NOT NULL NOT NULL UNIQUE,
  `name_ja` varchar(128) NOT NULL,
  `name_en` varchar(128),
  `geo` POINT,
  `altnames` varchar(256),
  `wididata_id` varchar(32),
  `change_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS dblist.database;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE dblist.database (
  `id` varchar(16) NOT NULL UNIQUE,
  `title_ja` varchar(256) NOT NULL,
  `title_en` varchar(256),
  `creator_id` varchar(32),
  `ddc_category` varchar(128),
  `type` varchar(128),
  `description_ja` varchar(1024),
  `description_en` varchar(1024),
  `url` varchar(128) NOT NULL,
  `change_date` date NOT NULL,
  `link_check` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: roofmarket_db
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agent`
--

DROP TABLE IF EXISTS `agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agent` (
  `agent_name` varchar(60) NOT NULL,
  `image_url` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent`
--

LOCK TABLES `agent` WRITE;
/*!40000 ALTER TABLE `agent` DISABLE KEYS */;
/*!40000 ALTER TABLE `agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `message_content` varchar(1024) DEFAULT NULL,
  `read_status` varchar(10) DEFAULT NULL,
  `property_id` varchar(60) NOT NULL,
  `sender_id` varchar(60) NOT NULL,
  `receiver_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_id` (`property_id`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`sender_id`) REFERENCES `user` (`id`),
  CONSTRAINT `message_ibfk_3` FOREIGN KEY (`receiver_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property`
--

DROP TABLE IF EXISTS `property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property` (
  `title` varchar(50) NOT NULL,
  `description` varchar(2050) NOT NULL,
  `property_type` varchar(10) NOT NULL,
  `price` float NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `listing_type` varchar(5) NOT NULL,
  `address` varchar(224) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `zip_code` varchar(15) DEFAULT NULL,
  `bedrooms` int NOT NULL,
  `bathrooms` int NOT NULL,
  `area` float NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `property_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property`
--

LOCK TABLES `property` WRITE;
/*!40000 ALTER TABLE `property` DISABLE KEYS */;
INSERT INTO `property` VALUES ('Summer Suites','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','villa',14550,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',1,2,1404,'b41ca16a-786d-4432-87df-1a5319058c3e','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Royal Haven Inn','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','villa',4578900,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',1,2,4570,'ef6574d5-9758-40e3-91a1-3a81ac303a58','3b36164f-47dc-44ac-acf7-3e6ffadc7045','2024-11-07 17:02:50','2024-11-07 12:02:50'),('Vortex','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','apartment',145880,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',2,2,1240,'e930bbb8-f2f5-456b-963d-24c5e14ef71f','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','2024-11-05 00:41:53','2024-11-04 19:41:53'),('The Golden Feather','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','apartment',8650000,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',3,2,45788,'77476c45-9998-40da-a1c8-1de85fc474d1','4ec2febb-da6d-4e40-b707-0cf1b33256e0','2024-11-07 17:08:07','2024-11-07 12:08:07'),('Regalia','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','apartment',10000,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',3,2,1000,'cb8d20e1-ee2f-4ca8-b3c1-e03933e5445f','591fa027-0b03-4968-9705-2d7a1b334dbc','2024-11-04 18:50:01','2024-11-04 13:50:01'),('Skyline Suites','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','studio',457899,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',6,4,12457,'a07e804b-1043-42f7-8224-db8c16213825','5f9073ed-4388-452e-acda-bdd90a8193be','2024-11-07 16:58:45','2024-11-07 11:58:45'),('Kaloum hotel','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','house',185520,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',4,5,14565,'045baf0b-3c5b-468c-86c4-b83e039b9fb5','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','2024-11-05 00:45:58','2024-11-04 19:45:58'),('The Grand Oasis','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','house',570068,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',4,3,457,'5d8e0636-eb25-4baf-9ebf-386590965d4f','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','2024-11-07 16:56:33','2024-11-07 11:56:33'),('Serenity Resort','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','apartment',578896,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',4,2,1457,'0851d1b5-5a3a-4f73-8986-8742e52fff09','747289b8-86ab-422f-857e-53bd8c1ad7b2','2024-11-07 17:00:38','2024-11-07 12:00:38'),('Noom','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','house',150000,NULL,'sell','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',5,4,1500,'6fbcf672-15fc-4753-88f7-ed23fd16c28f','7bc33a6f-efbb-440d-8523-fb53a1808bdd','2024-11-04 19:08:51','2024-11-04 14:08:51'),('Pita Hostel','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','house',140000,NULL,'rent','1412 Lambanyi','Conakry','Ratoma','Guinea','00224',4,4,41000,'b396f3bb-e578-4f2e-bdc7-5d8b1e66f14d','81097dc7-bd7c-4872-802d-a732c2562783','2024-11-21 18:35:32','2024-11-21 13:35:32'),('Platinium hotel','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','apartment',120000,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',2,2,1400,'b265fbf5-f187-48c3-8089-7ed3a7dad905','d84112ee-646d-4fdf-a023-b6f6f32e8f07','2024-11-04 18:57:28','2024-11-04 13:57:28'),('Azure Bay Retreat','This beautiful modern villa offers luxurious living in a prime location. The property features 4 spacious bedrooms, each with an ensuite bathroom, providing ultimate comfort and privacy. The open-concept living and dining area is flooded with natural light, leading to a stunning outdoor space that includes a private pool, landscaped garden, and a covered terrace ideal for entertaining. The gourmet kitchen is equipped with high-end appliances and sleek finishes. Additional amenities include a home office, a two-car garage, and smart home technology throughout. Situated in a peaceful, family-friendly neighborhood, this villa is perfect for those seeking elegance and convenience.','studio',587966,NULL,'rent','871 Avenue du Bon-air','QUEBEC CITY','QC','Canada','G1V2P6',4,3,14578,'b7f25553-ba37-45d0-837e-e5489175d84c','ef42107f-4c24-44c9-8741-215d58b1a4fc','2024-11-07 17:05:31','2024-11-07 12:05:31');
/*!40000 ALTER TABLE `property` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_image`
--

DROP TABLE IF EXISTS `property_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property_image` (
  `image_type` varchar(45) DEFAULT NULL,
  `image_url` varchar(100) DEFAULT NULL,
  `property_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `property_image_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_image`
--

LOCK TABLES `property_image` WRITE;
/*!40000 ALTER TABLE `property_image` DISABLE KEYS */;
INSERT INTO `property_image` VALUES ('Main_entrance','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_Main_entrance.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','00c042ab-33d7-4158-b8c8-08c781ba58c7','2024-11-07 17:08:07','2024-11-07 12:08:07'),('bathroom','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_bathroom.webp','5f9073ed-4388-452e-acda-bdd90a8193be','02f58ced-1e84-44ef-8515-515fd09e005b','2024-11-07 16:58:45','2024-11-07 11:58:45'),('kitchen','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_kitchen.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','03493c08-ae5e-4d44-8e74-46ec088eb05a','2024-11-07 16:56:33','2024-11-07 11:56:33'),('Main_entrance','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_Main_entrance.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','06cbfa3e-6a55-4841-91bb-786de714e638','2024-11-04 19:08:51','2024-11-04 14:08:51'),('kitchen','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_kitchen.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','0d075055-bb21-4dc7-a412-a57af7a658fc','2024-11-04 18:57:28','2024-11-04 13:57:28'),('Main_entrance','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_Main_entrance.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','0d62f222-4e43-4c4d-ace2-8225e27642db','2024-11-07 17:00:38','2024-11-07 12:00:38'),('bedroom','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_bedroom.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','0df13116-904c-420c-b032-3bded02e111c','2024-11-07 17:08:07','2024-11-07 12:08:07'),('balcony','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_balcony.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','0e1a684e-5e51-43d2-8b59-a4552d199b09','2024-11-04 18:50:02','2024-11-04 13:50:02'),('living_room','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_living_room.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','0f18de15-54ba-4f70-a26f-41134ce5c286','2024-11-07 17:02:50','2024-11-07 12:02:50'),('Main_image','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_Main_image.jpg','747289b8-86ab-422f-857e-53bd8c1ad7b2','11b6e00a-6816-4a77-a951-5282208a1d75','2024-11-07 17:00:38','2024-11-07 12:00:38'),('bathroom','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_bathroom.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','144a792b-6a34-432d-bc64-3037fcee215a','2024-11-04 19:08:51','2024-11-04 14:08:51'),('kitchen','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_kitchen.webp','5f9073ed-4388-452e-acda-bdd90a8193be','197df595-b62d-42c6-92b0-cc0e10a1b7b7','2024-11-07 16:58:45','2024-11-07 11:58:45'),('living_room','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_living_room.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','19d44549-5ded-4946-a67d-bf59a7c13b66','2024-11-04 18:57:28','2024-11-04 13:57:28'),('living_room','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_living_room.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','1a1355cc-9fec-4d81-888d-27df72625410','2024-11-04 18:50:02','2024-11-04 13:50:02'),('living_room','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_living_room.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','1b940344-df60-450e-b3ef-691a20562e07','2024-11-07 16:56:33','2024-11-07 11:56:33'),('bedroom','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_bedroom.webp','5f9073ed-4388-452e-acda-bdd90a8193be','227002f2-a584-4bd7-a0ba-2e3ffc645d52','2024-11-07 16:58:45','2024-11-07 11:58:45'),('Main_entrance','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_Main_entrance.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','238b110c-2ada-4f20-a1cd-c2bb3091210f','2024-11-04 18:50:01','2024-11-04 13:50:01'),('Main_image','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_Main_image.jpg','591fa027-0b03-4968-9705-2d7a1b334dbc','254bd879-0188-44fb-b3f3-4e021918b28f','2024-11-04 18:50:01','2024-11-04 13:50:01'),('living_room','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_living_room.webp','81097dc7-bd7c-4872-802d-a732c2562783','25f709e0-1665-4374-b0bc-e07837743c6c','2024-11-21 18:35:32','2024-11-21 13:35:32'),('balcony','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_balcony.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','273b4930-9b0c-4266-a707-7fd8bad5cfed','2024-11-07 17:00:38','2024-11-07 12:00:38'),('bathroom','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_bathroom.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','285fabe8-d3f9-4602-a62b-280a8e6bc3ac','2024-11-07 16:56:33','2024-11-07 11:56:33'),('bedroom','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_bedroom.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','34c88b71-83cc-419a-8228-7e7eb5f33d59','2024-11-07 17:00:38','2024-11-07 12:00:38'),('kitchen','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_kitchen.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','37ba730c-966b-43cc-94ed-b59cf64c24cc','2024-11-07 17:00:38','2024-11-07 12:00:38'),('Main_entrance','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_Main_entrance.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','3879613c-1f66-4b06-ab24-83b453eb67c4','2024-11-04 18:57:28','2024-11-04 13:57:28'),('living_room','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_living_room.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','3fed7245-45bb-4c5c-97b7-0c4096bcac5c','2024-11-04 19:08:51','2024-11-04 14:08:51'),('bathroom','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_bathroom.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','42cf6afc-27b0-4865-bb20-45506095e337','2024-11-07 17:05:31','2024-11-07 12:05:31'),('kitchen','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_kitchen.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','4514431c-1e93-4352-83d6-aecbf7796e8e','2024-11-07 17:08:07','2024-11-07 12:08:07'),('Main_entrance','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_Main_entrance.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','4f10d0db-4fc6-47b4-b751-1474363ed89b','2024-11-05 00:45:58','2024-11-04 19:45:58'),('balcony','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_balcony.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','4faf88bb-38ac-4c10-ace8-81b6158dab8c','2024-11-04 19:08:51','2024-11-04 14:08:51'),('balcony','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_balcony.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','4ff5c325-ab04-4264-af8c-007ee18c13dd','2024-11-04 18:57:28','2024-11-04 13:57:28'),('living_room','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_living_room.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','529862a2-0e4b-4111-aebf-9652e6234296','2024-11-05 00:45:58','2024-11-04 19:45:58'),('bedroom','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_bedroom.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','5334a308-dd3e-4924-981a-f6ba62357a1b','2024-11-04 18:57:28','2024-11-04 13:57:28'),('bedroom','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_bedroom.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','54be52c0-b04e-42db-8f74-4163cd9fb145','2024-11-04 19:08:51','2024-11-04 14:08:51'),('Main_image','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_Main_image.jpg','d84112ee-646d-4fdf-a023-b6f6f32e8f07','54e08e43-83a6-40fb-9497-e2e92e5ae769','2024-11-04 18:57:28','2024-11-04 13:57:28'),('bedroom','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_bedroom.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','58c6da48-4132-45b6-84a6-812a41a68ebd','2024-11-05 00:41:53','2024-11-04 19:41:53'),('living_room','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_living_room.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','5b39d8dd-9a87-4683-b65c-a03165502b49','2024-11-05 00:41:53','2024-11-04 19:41:53'),('bedroom','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_bedroom.webp','81097dc7-bd7c-4872-802d-a732c2562783','5b62d222-0c4c-4c40-a55a-29f6be5583fd','2024-11-21 18:35:32','2024-11-21 13:35:32'),('Main_image','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_Main_image.jpg','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','5e429c79-0ecc-427e-ae1d-7ee76fd44f7e','2024-11-07 16:56:33','2024-11-07 11:56:33'),('Main_entrance','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_Main_entrance.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','5ed92ee1-da3f-4098-afed-9e15cbd6fdc3','2024-11-05 00:41:53','2024-11-04 19:41:53'),('balcony','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_balcony.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','5fcb396f-4465-49a1-84b3-9303f972c644','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Main_entrance','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_Main_entrance.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','60682a03-c674-49ad-a561-50cce8d6d7db','2024-11-07 17:05:31','2024-11-07 12:05:31'),('bedroom','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_bedroom.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','61443ec3-8b8d-42de-810e-68910d331690','2024-11-07 17:02:50','2024-11-07 12:02:50'),('Main_image','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_Main_image.jpg','7bc33a6f-efbb-440d-8523-fb53a1808bdd','68fdda9c-786d-4574-b1fe-3320e2b86248','2024-11-04 19:08:51','2024-11-04 14:08:51'),('bedroom','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_bedroom.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','6990197d-edbd-49eb-b198-a562e3a6fe21','2024-11-05 00:45:58','2024-11-04 19:45:58'),('Main_entrance','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_Main_entrance.webp','5f9073ed-4388-452e-acda-bdd90a8193be','6be14cf4-535d-4fe0-b724-b9e8657c8941','2024-11-07 16:58:45','2024-11-07 11:58:45'),('Main_image','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_Main_image.jpg','3b36164f-47dc-44ac-acf7-3e6ffadc7045','70ab65b3-abb6-4cde-bd5d-d879f18a4a14','2024-11-07 17:02:50','2024-11-07 12:02:50'),('kitchen','static/uploads/7bc33a6f-efbb-440d-8523-fb53a1808bdd_kitchen.webp','7bc33a6f-efbb-440d-8523-fb53a1808bdd','76160c56-7356-499d-a146-18dea57d5a44','2024-11-04 19:08:51','2024-11-04 14:08:51'),('Main_image','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_Main_image.jpg','4ec2febb-da6d-4e40-b707-0cf1b33256e0','77ab4f81-5f08-4277-8fbc-cd1eb6d506e3','2024-11-07 17:08:07','2024-11-07 12:08:07'),('Main_entrance','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_Main_entrance.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','7a6b5b2f-8a0f-4770-873a-08f04af39121','2024-11-07 17:02:50','2024-11-07 12:02:50'),('kitchen','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_kitchen.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','7dab82c3-17f7-4769-871d-bbfbbd1c9ada','2024-11-07 17:05:31','2024-11-07 12:05:31'),('living_room','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_living_room.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','82a72bce-5b01-465b-a57c-6047a855f8f4','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Main_image','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_Main_image.jpg','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','82d82c97-2e3d-4b13-9cbc-f4c2a6fb2087','2024-11-05 00:38:08','2024-11-04 19:38:08'),('kitchen','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_kitchen.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','8478106c-3e29-49f8-bf33-69d8d0d385d0','2024-11-05 00:41:53','2024-11-04 19:41:53'),('kitchen','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_kitchen.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','8a4392c2-fbd3-4e0f-812d-e727e3634fb4','2024-11-07 17:02:50','2024-11-07 12:02:50'),('balcony','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_balcony.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','8b8515e6-2f8c-4a73-a542-fa83a03efb8f','2024-11-07 17:02:50','2024-11-07 12:02:50'),('bedroom','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_bedroom.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','8d5b735e-1b2b-4d10-bbaa-1e9b8d382ebf','2024-11-07 16:56:33','2024-11-07 11:56:33'),('living_room','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_living_room.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','8fec07b4-0f34-40bd-a903-0198f0aac3c7','2024-11-07 17:05:31','2024-11-07 12:05:31'),('Main_entrance','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_Main_entrance.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','99fce26c-334e-4efb-bc29-0509c6357777','2024-11-05 00:38:08','2024-11-04 19:38:08'),('balcony','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_balcony.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','9b66b51e-930a-48bb-b3db-663af33f62c2','2024-11-07 17:05:31','2024-11-07 12:05:31'),('bathroom','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_bathroom.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','9b995220-24ff-4328-9eaf-3c8f1eeda175','2024-11-05 00:45:58','2024-11-04 19:45:58'),('kitchen','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_kitchen.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','a4d94259-1dd9-406d-9489-7bc715f798de','2024-11-04 18:50:02','2024-11-04 13:50:02'),('Main_image','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_Main_image.jpg','5f9073ed-4388-452e-acda-bdd90a8193be','a8261163-9df7-497f-8d39-ec4c0ac7c21c','2024-11-07 16:58:45','2024-11-07 11:58:45'),('Main_image','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_Main_image.jpg','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','a96783e5-3249-4383-ab70-741fbad1e5d3','2024-11-05 00:41:53','2024-11-04 19:41:53'),('kitchen','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_kitchen.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','ab08b822-a024-4d08-aa64-46863fe9c7e6','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Main_image','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_Main_image.jpg','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','b689dd07-8ece-437e-b5ee-c774275035a4','2024-11-05 00:45:58','2024-11-04 19:45:58'),('Main_entrance','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_Main_entrance.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','bcc859f8-0f71-4016-8ede-3237292dc3b1','2024-11-07 16:56:33','2024-11-07 11:56:33'),('living_room','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_living_room.webp','5f9073ed-4388-452e-acda-bdd90a8193be','c1eb5279-9a9a-4afe-b6aa-70c53b2266cd','2024-11-07 16:58:45','2024-11-07 11:58:45'),('bathroom','static/uploads/d84112ee-646d-4fdf-a023-b6f6f32e8f07_bathroom.webp','d84112ee-646d-4fdf-a023-b6f6f32e8f07','c733d901-f56f-40b6-b657-ba6d771f11be','2024-11-04 18:57:28','2024-11-04 13:57:28'),('bathroom','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_bathroom.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','ce9e3b52-97f7-47ac-b022-94cb634d520f','2024-11-05 00:38:08','2024-11-04 19:38:08'),('bathroom','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_bathroom.webp','81097dc7-bd7c-4872-802d-a732c2562783','cf8d8ced-6a3f-4f4c-9bb3-82116c0c51c2','2024-11-21 18:35:32','2024-11-21 13:35:32'),('bedroom','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_bedroom.webp','ef42107f-4c24-44c9-8741-215d58b1a4fc','d06bc887-b571-4c2d-a932-b940286212cb','2024-11-07 17:05:31','2024-11-07 12:05:31'),('living_room','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_living_room.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','d08f47e0-e209-4222-87eb-785506988dcd','2024-11-07 17:00:38','2024-11-07 12:00:38'),('bedroom','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_bedroom.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','d1fca9e4-f867-4698-aac3-1503024b5b86','2024-11-04 18:50:02','2024-11-04 13:50:02'),('kitchen','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_kitchen.webp','81097dc7-bd7c-4872-802d-a732c2562783','d232c6c7-c72a-4c2a-96d9-f07105de1a7e','2024-11-21 18:35:32','2024-11-21 13:35:32'),('kitchen','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_kitchen.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','d2f0f237-2016-4f5d-992d-7c7d667ba857','2024-11-05 00:45:58','2024-11-04 19:45:58'),('balcony','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_balcony.webp','81097dc7-bd7c-4872-802d-a732c2562783','d367b9aa-7460-4f7b-89ac-ec68a90b22db','2024-11-21 18:35:32','2024-11-21 13:35:32'),('balcony','static/uploads/7001b91a-04d2-4ea5-abd4-87bb6cad2dc7_balcony.webp','7001b91a-04d2-4ea5-abd4-87bb6cad2dc7','d665c356-705e-4d58-adf1-d96d0b1a9c79','2024-11-07 16:56:33','2024-11-07 11:56:33'),('balcony','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_balcony.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','e0a1b6ad-73b3-466c-a5c9-f49648aa7641','2024-11-07 17:08:07','2024-11-07 12:08:07'),('balcony','static/uploads/6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e_balcony.webp','6ab12e4e-9fd7-4ce9-975c-ae0d40168c6e','e14989b7-3125-4941-b8c9-9a785299cac3','2024-11-05 00:45:58','2024-11-04 19:45:58'),('living_room','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_living_room.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','eaa72c34-6486-4bb6-bc32-05a3e3aa3058','2024-11-07 17:08:07','2024-11-07 12:08:07'),('bathroom','static/uploads/747289b8-86ab-422f-857e-53bd8c1ad7b2_bathroom.webp','747289b8-86ab-422f-857e-53bd8c1ad7b2','eb9b16df-02ce-4ea4-b089-c23112094af9','2024-11-07 17:00:38','2024-11-07 12:00:38'),('bathroom','static/uploads/3b36164f-47dc-44ac-acf7-3e6ffadc7045_bathroom.webp','3b36164f-47dc-44ac-acf7-3e6ffadc7045','ee71e10e-b7bc-47a3-8610-c298733ffb12','2024-11-07 17:02:50','2024-11-07 12:02:50'),('Main_image','static/uploads/ef42107f-4c24-44c9-8741-215d58b1a4fc_Main_image.jpg','ef42107f-4c24-44c9-8741-215d58b1a4fc','ee997d3e-4c50-459f-aeaf-6b0deee1468f','2024-11-07 17:05:31','2024-11-07 12:05:31'),('','static/uploads/5f9073ed-4388-452e-acda-bdd90a8193be_.webp','5f9073ed-4388-452e-acda-bdd90a8193be','f1d38c5e-c21b-4c44-9b36-bdecfc3604eb','2024-11-07 16:58:45','2024-11-07 11:58:45'),('bathroom','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_bathroom.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','f2067b07-f471-4bbd-8daa-fea2bffe3a0e','2024-11-05 00:41:53','2024-11-04 19:41:53'),('bathroom','static/uploads/4ec2febb-da6d-4e40-b707-0cf1b33256e0_bathroom.webp','4ec2febb-da6d-4e40-b707-0cf1b33256e0','f403a1cc-81f8-4b32-b134-62e5deb34231','2024-11-07 17:08:07','2024-11-07 12:08:07'),('Main_image','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_Main_image.jpg','81097dc7-bd7c-4872-802d-a732c2562783','f5c40031-23a6-43e3-bc87-f385c1db4f29','2024-11-21 18:35:32','2024-11-21 13:35:32'),('balcony','static/uploads/3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b_balcony.webp','3d813f2b-c03f-4a0e-bc2d-a6ac28f8b53b','f5f87667-ebf9-4d43-9c3e-948d62b017a1','2024-11-05 00:41:53','2024-11-04 19:41:53'),('bathroom','static/uploads/591fa027-0b03-4968-9705-2d7a1b334dbc_bathroom.webp','591fa027-0b03-4968-9705-2d7a1b334dbc','f92779f1-4b16-4a92-a610-bfdeb228f5b2','2024-11-04 18:50:02','2024-11-04 13:50:02'),('bedroom','static/uploads/20c6d3ff-7d80-477f-8ae8-04c90eb7e38a_bedroom.webp','20c6d3ff-7d80-477f-8ae8-04c90eb7e38a','fabd6012-6929-4374-bfbf-fc3500576690','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Main_entrance','static/uploads/81097dc7-bd7c-4872-802d-a732c2562783_Main_entrance.webp','81097dc7-bd7c-4872-802d-a732c2562783','fbd41155-3349-4093-ad0e-6375619a14fd','2024-11-21 18:35:32','2024-11-21 13:35:32');
/*!40000 ALTER TABLE `property_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `rating` int DEFAULT NULL,
  `comment` varchar(1023) DEFAULT NULL,
  `user_id` varchar(60) NOT NULL,
  `property_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `payment_status` varchar(10) DEFAULT NULL,
  `supplier_id` varchar(60) NOT NULL,
  `property_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `user` (`id`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `first_name` varchar(224) NOT NULL,
  `last_name` varchar(224) NOT NULL,
  `email` varchar(224) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `user_type` varchar(10) DEFAULT NULL,
  `profile_image` varchar(65) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'045baf0b-3c5b-468c-86c4-b83e039b9fb5','2024-11-05 00:45:58','2024-11-04 19:45:58'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'0851d1b5-5a3a-4f73-8986-8742e52fff09','2024-11-07 17:00:38','2024-11-07 12:00:38'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'5d8e0636-eb25-4baf-9ebf-386590965d4f','2024-11-07 16:56:33','2024-11-07 11:56:33'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'6fbcf672-15fc-4753-88f7-ed23fd16c28f','2024-11-04 19:08:51','2024-11-04 14:08:51'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'77476c45-9998-40da-a1c8-1de85fc474d1','2024-11-07 17:08:07','2024-11-07 12:08:07'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'a07e804b-1043-42f7-8224-db8c16213825','2024-11-07 16:58:45','2024-11-07 11:58:45'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'b265fbf5-f187-48c3-8089-7ed3a7dad905','2024-11-04 18:54:49','2024-11-04 13:54:49'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'b396f3bb-e578-4f2e-bdc7-5d8b1e66f14d','2024-11-21 18:35:32','2024-11-21 13:35:32'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'b41ca16a-786d-4432-87df-1a5319058c3e','2024-11-05 00:38:08','2024-11-04 19:38:08'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'b7f25553-ba37-45d0-837e-e5489175d84c','2024-11-07 17:05:31','2024-11-07 12:05:31'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'cb8d20e1-ee2f-4ca8-b3c1-e03933e5445f','2024-11-04 18:47:32','2024-11-04 13:47:32'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'e930bbb8-f2f5-456b-963d-24c5e14ef71f','2024-11-05 00:41:53','2024-11-04 19:41:53'),('Amadou','Bah',NULL,NULL,NULL,NULL,NULL,'ef6574d5-9758-40e3-91a1-3a81ac303a58','2024-11-07 17:02:50','2024-11-07 12:02:50');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `whishlist`
--

DROP TABLE IF EXISTS `whishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `whishlist` (
  `user_id` varchar(60) NOT NULL,
  `property_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `whishlist_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `whishlist_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `whishlist`
--

LOCK TABLES `whishlist` WRITE;
/*!40000 ALTER TABLE `whishlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `whishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-21 15:21:12

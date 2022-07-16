-- MariaDB dump 10.19  Distrib 10.6.7-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: system
-- ------------------------------------------------------
-- Server version	10.6.7-MariaDB-2ubuntu1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin_login`
--

DROP TABLE IF EXISTS `Admin_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_login`
--

LOCK TABLES `Admin_login` WRITE;
/*!40000 ALTER TABLE `Admin_login` DISABLE KEYS */;
INSERT INTO `Admin_login` VALUES (1,'hardik@gmail.com','8411075884baf40746696d05e54ad340'),(3,'ram@gmai.com','74df827952e926c8f3aaef5e9b1e5acc'),(5,'sahil@gmai.com','1cc21d91829fa5a483a2e9346686cfa8');
/*!40000 ALTER TABLE `Admin_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_login`
--

DROP TABLE IF EXISTS `User_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_login`
--

LOCK TABLES `User_login` WRITE;
/*!40000 ALTER TABLE `User_login` DISABLE KEYS */;
INSERT INTO `User_login` VALUES (1,'sahil@gmai.com','sahil13','8411075884baf40746696d05e54ad340'),(2,'hardik1@gmail.com','hardik','8411075884baf40746696d05e54ad340'),(3,'vijay@gmail.com','vijay','890b0e8ea66883efc7153b494e95b680'),(4,'ram@gmail.com','ram','74df827952e926c8f3aaef5e9b1e5acc'),(5,'hspithiya9818@gmail.com','hspithiya','1e76a734f75f3cb15f61bd547c60fd92'),(6,'hspithiya9818@gmail.com','testemail','9305edab3f0d808233dcd4d3a00865fc'),(7,'dhruvikaneriya52@gmail.com','dhruvi','a27f79ef693435fb3834bb8391e5a3d5'),(8,'cikik@mailinator.com','qadegin','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(9,'zitaze@mailinator.com','tujuxitera','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(10,'fevuc@mailinator.com','nafym','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(11,'pylejyfur@mailinator.com','vipene','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(12,'zinawoxu@mailinator.com','bewej','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(13,'faheseze@mailinator.com','jyjapoxuva','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(14,'cehov@mailinator.com','xopipes','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(15,'fewutys@mailinator.com','xozynit','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(16,'locaqylaf@mailinator.com','lugype','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(17,'jonytolu@mailinator.com','qobevo','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(18,'weri@mailinator.com','bimih','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(19,'vaquqixul@mailinator.com','jagasid','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(20,'paluj@mailinator.com','rinabelax','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(21,'vuhaloq@mailinator.com','zawegu','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(22,'xiluqah@mailinator.com','hinaqitok','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(23,'kobag@mailinator.com','xideqekiqy','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(24,'mofa@mailinator.com','vunyp','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(25,'gitap@mailinator.com','simivaza','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(26,'makavys@mailinator.com','fonogatu','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(27,'gykity@mailinator.com','turas','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(28,'jenaju@mailinator.com','vogotera','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(29,'kakiq@mailinator.com','rahif','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(30,'ryjeqakaj@mailinator.com','bibosizis','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(31,'tytajiboj@mailinator.com','kydukure','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(32,'vovehyh@mailinator.com','buzizatuv','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(33,'soci@mailinator.com','ryzocibi','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(34,'sutocuhaha@mailinator.com','nisatipo','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(35,'zudysapi@mailinator.com','zysukix','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(36,'xiwyxeme@mailinator.com','vekag','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(37,'xacuryki@mailinator.com','cehulihuru','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(38,'gazy@mailinator.com','toqaf','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(39,'jawykode@mailinator.com','tukoduna','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(40,'qebiqot@mailinator.com','lowot','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(41,'foluxif@mailinator.com','wapivyta','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(42,'jojefelixe@mailinator.com','vyjaxiwed','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(43,'wilaryga@mailinator.com','cujyby','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(44,'vexi@mailinator.com','pagole','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(45,'sisec@mailinator.com','cozufe','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(46,'pisogib@mailinator.com','jemaqemi','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(47,'hafygemuwy@mailinator.com','hijaxu','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(48,'jymo@mailinator.com','cydunygot','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(49,'jejowyto@mailinator.com','titicoxuk','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(50,'kyjexa@mailinator.com','jygukicope','f3ed11bbdb94fd9ebdefbaf646ab94d3'),(51,'mubab@mailinator.com','derogadu','f3ed11bbdb94fd9ebdefbaf646ab94d3');
/*!40000 ALTER TABLE `User_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_profile`
--

DROP TABLE IF EXISTS `User_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_birth` date NOT NULL,
  `mobile_number` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `state` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `zipcode` int(11) NOT NULL,
  `profile_updated_dt` date NOT NULL,
  `img` longblob NOT NULL,
  `birthpdf` blob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `User_profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User_login` (`Id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_profile`
--

LOCK TABLES `User_profile` WRITE;
/*!40000 ALTER TABLE `User_profile` DISABLE KEYS */;
INSERT INTO `User_profile` VALUES (6,1,'Sahil','Patel ','1999-06-30','7894561235','Male','ahmedabad, gujrat','ahmedabad','Meghalaya',362225,'2022-07-16','cf5ed3a2-0508-11ed-bda5-5d0fb9fcfefa_IMG20220716144527.jpg','cf5ed3a3-0508-11ed-bda5-5d0fb9fcfefa_2.PythoProg_softarchive.net.pdf'),(7,4,'Ram','Pitiya','2001-02-14','7418529635','Male','At:-akhodad ta:-keshid did:-junagadh','Akhodad','Punjab',362220,'2022-07-16','7579b778-04d9-11ed-bda5-5d0fb9fcfefa_download.jpg','7579b779-04d9-11ed-bda5-5d0fb9fcfefa_Imagicaa_for_Corporates_Sanskar_Technolab_Private_Limited.pdf'),(8,9,'Zitaze','Trevino','1989-04-17','7894561235','Male','Velit vitae et quia sit doloremque quidem ex elit','Nostrum nihil duis N','Meghalaya',824309,'2022-07-12','be3f14be-01c6-11ed-945a-43551c83f646_download.png',''),(9,10,'Elton','Valenzuela','1999-06-01','7895555555','Male','Eos dolores placeat hic aut inventore rerum velit','Dolorem tenetur sunt','Andhra Pradesh',172928,'2022-07-12','9c57c2c4-01e4-11ed-945a-43551c83f646_images.png','birth.pdf'),(10,11,'Aiko','Lewis','2004-02-16','7787845455','Female','Deserunt sit ratione laborum Placeat veniam lor','Hic deserunt culpa ','Punjab',938238,'2022-07-12','8312a0b2-01e5-11ed-945a-43551c83f646_download.jpg','8312a0b3-01e5-11ed-945a-43551c83f646_Imagicaa_for_Corporates_Sanskar_Technolab_Private_Limited.pdf'),(11,12,'Rebecca','Sharpe','1992-03-23','7745555555','Male','Pariatur Aut ex voluptates consequat Eaque in au','Sint pariatur Solut','Maharashtra',724505,'2022-07-12','4d97d758-01e6-11ed-945a-43551c83f646_download.png','Imagicaa_for_Corporates_Sanskar_Technolab_Private_Limited.pdf'),(19,13,'Naida','Luna','1998-05-20','9531254878','Male','Voluptate et culpa adipisci enim minus aperiam sa','Quasi recusandae Qu','Rajasthan',551085,'2022-07-13','ef72e280-027b-11ed-a0df-071fe7cbc68e_ram.png','ef72e281-027b-11ed-a0df-071fe7cbc68e_12RulestoLearntoCode2ndEdition2022.pdf'),(20,7,'Dhruvi','Patel','2002-07-18','7444444444','Female','At:-akhodad ta:-keshid did:-junagadh','Akhodad','Gujarat',362220,'2022-07-16','c082877e-04e1-11ed-bda5-5d0fb9fcfefa_sample4.png','c082877f-04e1-11ed-bda5-5d0fb9fcfefa_PDF_Sample_1.pdf');
/*!40000 ALTER TABLE `User_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-16 19:00:55

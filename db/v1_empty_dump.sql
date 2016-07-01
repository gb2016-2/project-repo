-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ark
-- ------------------------------------------------------
-- Server version	5.5.49-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add персону',7,'add_persons'),(20,'Can change персону',7,'change_persons'),(21,'Can delete персону',7,'delete_persons'),(22,'Can add ключевое слово',8,'add_keywords'),(23,'Can change ключевое слово',8,'change_keywords'),(24,'Can delete ключевое слово',8,'delete_keywords'),(25,'Can add сайт',9,'add_sites'),(26,'Can change сайт',9,'change_sites'),(27,'Can delete сайт',9,'delete_sites'),(28,'Can add страницу',10,'add_pages'),(29,'Can change страницу',10,'change_pages'),(30,'Can delete страницу',10,'delete_pages'),(31,'Can add рейтинг',11,'add_personpagerank'),(32,'Can change рейтинг',11,'change_personpagerank'),(33,'Can delete рейтинг',11,'delete_personpagerank');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$24000$e3YOqkN8E1BX$OBoeP+07XUbd3Z3M+5lrw6iOslxWUPwL8+HN2d0Gnoo=','2016-06-27 20:38:28',0,'someone','Некто','Таинственный','',1,1,'2016-06-27 20:17:52'),(3,'pbkdf2_sha256$24000$eQGiDpxwJJ9M$6y//ynl23wwZFTMDhm2C9lxCUG+3O534Hzb6x5OwwEI=','2016-06-29 18:37:46',1,'robot','Робот','Странный','robot@mail.ru',1,1,'2016-06-27 20:25:21');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coriander_keywords`
--

DROP TABLE IF EXISTS `coriander_keywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coriander_keywords` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coriander_keywords_45b2392b` (`person_id`),
  CONSTRAINT `coriander_keywords_person_id_d85d3b7d_fk_coriander_persons_id` FOREIGN KEY (`person_id`) REFERENCES `coriander_persons` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coriander_keywords`
--

LOCK TABLES `coriander_keywords` WRITE;
/*!40000 ALTER TABLE `coriander_keywords` DISABLE KEYS */;
/*!40000 ALTER TABLE `coriander_keywords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coriander_pages`
--

DROP TABLE IF EXISTS `coriander_pages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coriander_pages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(450) NOT NULL,
  `found_date_time` date DEFAULT NULL,
  `last_scan_date` date DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coriander_pages_a0b7f670` (`site_id`),
  CONSTRAINT `coriander_pages_site_id_3fe9871b_fk_coriander_sites_id` FOREIGN KEY (`site_id`) REFERENCES `coriander_sites` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coriander_pages`
--

LOCK TABLES `coriander_pages` WRITE;
/*!40000 ALTER TABLE `coriander_pages` DISABLE KEYS */;
/*!40000 ALTER TABLE `coriander_pages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coriander_personpagerank`
--

DROP TABLE IF EXISTS `coriander_personpagerank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coriander_personpagerank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank` int(11) NOT NULL,
  `page_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coriander_personpagerank_45b2392b` (`person_id`),
  KEY `coriander_personpagerank_page_id_c32fb4d1_fk_coriander_pages_id` (`page_id`),
  KEY `coriander_personpagerank_9365d6e7` (`site_id`),
  CONSTRAINT `coriander_personpagerank_page_id_c32fb4d1_fk_coriander_pages_id` FOREIGN KEY (`page_id`) REFERENCES `coriander_pages` (`id`),
  CONSTRAINT `coriander_personpagerank_site_id_650b5381_fk_coriander_sites_id` FOREIGN KEY (`site_id`) REFERENCES `coriander_sites` (`id`),
  CONSTRAINT `coriander_personpager_person_id_8bd003a2_fk_coriander_persons_id` FOREIGN KEY (`person_id`) REFERENCES `coriander_persons` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coriander_personpagerank`
--

LOCK TABLES `coriander_personpagerank` WRITE;
/*!40000 ALTER TABLE `coriander_personpagerank` DISABLE KEYS */;
/*!40000 ALTER TABLE `coriander_personpagerank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coriander_persons`
--

DROP TABLE IF EXISTS `coriander_persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coriander_persons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coriander_persons`
--

LOCK TABLES `coriander_persons` WRITE;
/*!40000 ALTER TABLE `coriander_persons` DISABLE KEYS */;
INSERT INTO `coriander_persons` VALUES (4,'Путин'),(5,'Медведеа');
/*!40000 ALTER TABLE `coriander_persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coriander_sites`
--

DROP TABLE IF EXISTS `coriander_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coriander_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coriander_sites`
--

LOCK TABLES `coriander_sites` WRITE;
/*!40000 ALTER TABLE `coriander_sites` DISABLE KEYS */;
INSERT INTO `coriander_sites` VALUES (1,'http://lenta.ru');
/*!40000 ALTER TABLE `coriander_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (4,'2016-06-27 20:26:17','1','root',3,'',4,3),(5,'2016-06-27 20:28:53','3','robot',2,'Изменен first_name и last_name.',4,3),(6,'2016-06-27 20:29:02','2','someone',2,'Изменен is_staff.',4,3),(7,'2016-06-27 20:32:17','2','someone',2,'Изменен password.',4,3),(8,'2016-06-27 20:58:46','2','Putin',1,'Добавлено.',7,3),(9,'2016-06-27 20:58:51','2','Putin',2,'Ни одно поле не изменено.',7,3),(10,'2016-06-27 21:01:00','1','http://lenta.ru',1,'Добавлено.',9,3),(11,'2016-06-27 21:13:12','2','Putin',3,'',7,3),(12,'2016-06-27 21:13:33','4','123',1,'Добавлено.',7,3),(13,'2016-06-27 21:15:30','4','Путин',2,'Изменен name.',7,3),(14,'2016-06-29 18:30:59','5','Медведеа',1,'Добавлено.',7,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'coriander','keywords'),(10,'coriander','pages'),(11,'coriander','personpagerank'),(7,'coriander','persons'),(9,'coriander','sites'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-06-27 19:02:33'),(2,'auth','0001_initial','2016-06-27 19:02:34'),(3,'admin','0001_initial','2016-06-27 19:02:34'),(4,'admin','0002_logentry_remove_auto_add','2016-06-27 19:02:34'),(5,'contenttypes','0002_remove_content_type_name','2016-06-27 19:02:34'),(6,'auth','0002_alter_permission_name_max_length','2016-06-27 19:02:34'),(7,'auth','0003_alter_user_email_max_length','2016-06-27 19:02:34'),(8,'auth','0004_alter_user_username_opts','2016-06-27 19:02:34'),(9,'auth','0005_alter_user_last_login_null','2016-06-27 19:02:34'),(10,'auth','0006_require_contenttypes_0002','2016-06-27 19:02:34'),(11,'auth','0007_alter_validators_add_error_messages','2016-06-27 19:02:34'),(12,'sessions','0001_initial','2016-06-27 19:02:35'),(13,'coriander','0001_initial','2016-06-27 19:08:18'),(14,'coriander','0002_auto_20160627_1915','2016-06-27 19:15:12'),(15,'coriander','0003_personpagerank_site','2016-06-30 07:44:42');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5gof720f1xvq473soa7cdwfy3qv5lxjr','OGVjOGUwMTIxMjMwMDlhYmJjZDc5MjViMWIzNTM5NzcwNTg2MTU5ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyZDUxZmYxMzQzNGQ3Njk0MTBjMjVjMmQwYTBmNDAyMDg3MzkwNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-07-13 18:37:46'),('alykj8tvymkotmbilbloqns656c3e5vo','OGVjOGUwMTIxMjMwMDlhYmJjZDc5MjViMWIzNTM5NzcwNTg2MTU5ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyZDUxZmYxMzQzNGQ3Njk0MTBjMjVjMmQwYTBmNDAyMDg3MzkwNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-07-11 20:41:58'),('bmyjntudv0xgsq3f2192yug42v43wjw3','OGVjOGUwMTIxMjMwMDlhYmJjZDc5MjViMWIzNTM5NzcwNTg2MTU5ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyZDUxZmYxMzQzNGQ3Njk0MTBjMjVjMmQwYTBmNDAyMDg3MzkwNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-07-13 18:28:51'),('u1owye9ppvu5hga0dypf10rgbhnpqp47','OGVjOGUwMTIxMjMwMDlhYmJjZDc5MjViMWIzNTM5NzcwNTg2MTU5ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyZDUxZmYxMzQzNGQ3Njk0MTBjMjVjMmQwYTBmNDAyMDg3MzkwNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2016-07-11 20:54:21');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-01 15:26:33

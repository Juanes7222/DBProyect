-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 28-10-2023 a las 22:37:33
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbproject`
--
CREATE DATABASE IF NOT EXISTS `dbproject` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `dbproject`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_userbase'),
(22, 'Can change user', 6, 'change_userbase'),
(23, 'Can delete user', 6, 'delete_userbase'),
(24, 'Can view user', 6, 'view_userbase'),
(25, 'Can add psychologist', 7, 'add_psychologist'),
(26, 'Can change psychologist', 7, 'change_psychologist'),
(27, 'Can delete psychologist', 7, 'delete_psychologist'),
(28, 'Can view psychologist', 7, 'view_psychologist'),
(29, 'Can add requests', 8, 'add_requests'),
(30, 'Can change requests', 8, 'change_requests'),
(31, 'Can delete requests', 8, 'delete_requests'),
(32, 'Can view requests', 8, 'view_requests'),
(33, 'Can add forms', 9, 'add_forms'),
(34, 'Can change forms', 9, 'change_forms'),
(35, 'Can delete forms', 9, 'delete_forms'),
(36, 'Can view forms', 9, 'view_forms');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'user', 'userbase'),
(7, 'user', 'psychologist'),
(8, 'user', 'requests'),
(9, 'user', 'forms');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-28 19:16:42.821762'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-10-28 19:16:43.376692'),
(3, 'auth', '0001_initial', '2023-10-28 19:16:45.772113'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-10-28 19:16:45.905132'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-10-28 19:16:45.918126'),
(6, 'auth', '0004_alter_user_username_opts', '2023-10-28 19:16:45.931117'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-10-28 19:16:45.942111'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-10-28 19:16:45.946109'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-10-28 19:16:45.958103'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-10-28 19:16:45.971095'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-10-28 19:16:45.984086'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-10-28 19:16:46.377552'),
(13, 'auth', '0011_update_proxy_permissions', '2023-10-28 19:16:46.394542'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-10-28 19:16:46.405536'),
(15, 'user', '0001_initial', '2023-10-28 19:16:52.919170'),
(16, 'admin', '0001_initial', '2023-10-28 19:16:54.339131'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-10-28 19:16:54.379106'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-28 19:16:54.409086'),
(19, 'sessions', '0001_initial', '2023-10-28 19:16:55.135124');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ifq1zcy76nmb67nopa3bna8pab4vmbwf', '.eJxVjEEOwiAQRe_C2hCmYKe4dO8ZyAwMUjU0Ke3KeHfbpAvdvvf-f6tA61LC2mQOY1IXBer0y5jiU-ou0oPqfdJxqss8st4Tfdimb1OS1_Vo_w4KtbKtmbtzFgOUwaaeyIJgcoMHDwIpChuTe-isZ8bBEAK6jXjrPFqHiOrzBezvNzc:1qwql5:wE1pe42MxEehVon2wfTJKatrEG6XhyJYmMf1ZTkd-JI', '2023-10-28 22:22:15.499579'),
('2kh2m9qcr87vm2wnljdtatmkk1vd9btp', 'e30:1qwrcs:E3uKf2DoVlWr9wkKUcOJ5SWZ4P1GjvyWKmPbA_6tPV4', '2023-10-28 23:17:50.600175'),
('cz145ie0ecrfo6s6rz485hxdqb36cvfg', '.eJxVjMsOgjAUBf-la9NcWqTFpXu-obmvWtRAQmFl_HclYaHbMzPnZRJua0lb1SWNYi4mmNPvRsgPnXYgd5xus-V5WpeR7K7Yg1Y7zKLP6-H-HRSs5VtH5wUCt-SiitOuzdL1jsn3iOAAI0cAQa8I4LMwaEON5tCBPxMRm_cH8Zg4nA:1qwrnD:VoAc4Jb5njP0gYcT1MO4RRhaCxewy69oYeDUW_TBDQ0', '2023-10-28 23:28:31.424509');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_forms`
--

DROP TABLE IF EXISTS `user_forms`;
CREATE TABLE IF NOT EXISTS `user_forms` (
  `form_id` bigint NOT NULL AUTO_INCREMENT,
  `salud` int NOT NULL,
  `economia` int NOT NULL,
  `trabajo` int NOT NULL,
  `romance` int NOT NULL,
  `crecimiento_personal` int NOT NULL,
  `amigos` int NOT NULL,
  `diversion` int NOT NULL,
  `imagen_propia` int NOT NULL,
  `ambiente_fisico` int NOT NULL,
  `date` datetime(6) NOT NULL,
  `message` longtext,
  `message_title` longtext,
  `img` varchar(100) DEFAULT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`form_id`),
  KEY `user_forms_user_id_id_f9aedbc1` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `user_forms`
--

INSERT INTO `user_forms` (`form_id`, `salud`, `economia`, `trabajo`, `romance`, `crecimiento_personal`, `amigos`, `diversion`, `imagen_propia`, `ambiente_fisico`, `date`, `message`, `message_title`, `img`, `user_id_id`) VALUES
(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '2023-10-28 20:30:09.108872', NULL, NULL, 'wheels/1_1_2023-10-28.png', 1),
(2, 3, 4, 2, 3, 3, 1, 2, 5, 2, '2023-10-28 21:18:54.455265', NULL, NULL, 'wheels/1_2_2023-10-28.png', 1),
(3, 2, 3, 4, 4, 3, 1, 4, 3, 4, '2023-10-28 22:09:30.875643', NULL, NULL, 'wheels/3_3_2023-10-28.png', 3),
(4, 4, 3, 4, 2, 4, 4, 5, 4, 2, '2023-10-28 22:14:41.449337', NULL, NULL, 'wheels/4_4_2023-10-28.png', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_psychologist`
--

DROP TABLE IF EXISTS `user_psychologist`;
CREATE TABLE IF NOT EXISTS `user_psychologist` (
  `user_id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `user_psychologist`
--

INSERT INTO `user_psychologist` (`user_id`, `code`) VALUES
(2, 'YNpvatwzOL'),
(7, '1E8akuuffV');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_psychologist_clients`
--

DROP TABLE IF EXISTS `user_psychologist_clients`;
CREATE TABLE IF NOT EXISTS `user_psychologist_clients` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `psychologist_id` bigint NOT NULL,
  `userbase_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_psychologist_client_psychologist_id_userbase_6e42431e_uniq` (`psychologist_id`,`userbase_id`),
  KEY `user_psychologist_clients_psychologist_id_41ce55bc` (`psychologist_id`),
  KEY `user_psychologist_clients_userbase_id_69a82b1b` (`userbase_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `user_psychologist_clients`
--

INSERT INTO `user_psychologist_clients` (`id`, `psychologist_id`, `userbase_id`) VALUES
(1, 2, 1),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_requests`
--

DROP TABLE IF EXISTS `user_requests`;
CREATE TABLE IF NOT EXISTS `user_requests` (
  `req_id` bigint NOT NULL AUTO_INCREMENT,
  `result` tinyint(1) NOT NULL,
  `user_id_id` bigint NOT NULL,
  `user_req_id` bigint NOT NULL,
  PRIMARY KEY (`req_id`),
  KEY `user_requests_user_id_id_c79ebd07` (`user_id_id`),
  KEY `user_requests_user_req_id_f9a8d5a7` (`user_req_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `user_requests`
--

INSERT INTO `user_requests` (`req_id`, `result`, `user_id_id`, `user_req_id`) VALUES
(1, 1, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_userbase`
--

DROP TABLE IF EXISTS `user_userbase`;
CREATE TABLE IF NOT EXISTS `user_userbase` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` int NOT NULL,
  `document` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `document` (`document`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `user_userbase`
--

INSERT INTO `user_userbase` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`, `document`) VALUES
(1, 'pbkdf2_sha256$600000$1OXQ2EH1Je50QJzmruzDC4$7dh9gKDARZ4TFIzag3ulhGYS5hYzJttspkHMjwfigkI=', '2023-10-28 22:07:52.612712', 0, 'juanb', 'Juan', 'Cardona Blandon', 'juanblandon975@gmail.com', 0, 1, '2023-10-28 20:29:52.851994', 1, '1113858851'),
(2, 'pbkdf2_sha256$600000$K5JMwc8zoTMMwdSfKSgdX7$Wsw6IA6pi4FI+jvvTR/vSYUTwq+iVfFcM38yhvlwU9c=', '2023-10-28 22:07:19.649361', 0, 'psi', 'Prueba', 'Psi', 'juan.cardona13@gmail.com', 0, 1, '2023-10-28 22:07:16.064016', 2, '123456'),
(3, 'pbkdf2_sha256$600000$w2FfJowwcmCK0z0LNz0kju$AnJo0OcGmp58PKFoFcVOCJHBpSbv8UsCOUfvoQej34I=', '2023-10-28 22:08:53.921439', 0, 'user2', 'Carlitos', 'Carabali', 'juanblandon975s@gmail.com', 0, 1, '2023-10-28 22:08:50.598761', 1, '5352'),
(4, 'pbkdf2_sha256$600000$4CGL8WO9Vldp9APD5Cvoij$hcwJ+fQXeetRJVYKEzKRICoXbZEFFf/tKNu/v0xocwY=', '2023-10-28 22:11:55.813699', 0, 'user3', 'Manuel', 'Gonzales', 'juanblandon975sss@gmail.com', 0, 1, '2023-10-28 22:11:51.972896', 1, '654123'),
(5, 'pbkdf2_sha256$600000$FYR4ECa8NkaYsTKM6FJ9WX$EcQeJl5F+CZjYSdPQwTRPYLBdT1ODe5ENyDb6BfnGrg=', '2023-10-28 22:17:50.604172', 0, 'psi2', 'Isabella', 'Carmona', 'isa_2273@hotmail.com', 0, 1, '2023-10-28 22:17:47.391062', 2, '65446541564654654654'),
(6, 'pbkdf2_sha256$600000$C8FHsYpTxhGdXVDwn4qGpK$WXj8xT41VPWjK1nqo61FWHXbp09kA3176nPKBojHpmQ=', '2023-10-28 22:25:46.995764', 0, 'pruebauser3', 'Juana', 'Henao', 'juanblandon97@hotmail.com', 0, 1, '2023-10-28 22:25:43.055293', 1, '545455456'),
(7, 'pbkdf2_sha256$600000$prKvvwgCC4Zwunu8comNnr$DgW9H+k/Okdgv2VfmwWJ2UhkEfDP8g8bhC1sBZthLJg=', '2023-10-28 22:28:24.692263', 0, 'hola', 'Jose', 'Montilla', 'iglesiammmcartagovalle@gmail.com', 0, 1, '2023-10-28 22:28:20.819993', 2, '21514654');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_userbase_groups`
--

DROP TABLE IF EXISTS `user_userbase_groups`;
CREATE TABLE IF NOT EXISTS `user_userbase_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userbase_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_userbase_groups_userbase_id_group_id_617efe64_uniq` (`userbase_id`,`group_id`),
  KEY `user_userbase_groups_userbase_id_746e0834` (`userbase_id`),
  KEY `user_userbase_groups_group_id_70a2e1f4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_userbase_user_permissions`
--

DROP TABLE IF EXISTS `user_userbase_user_permissions`;
CREATE TABLE IF NOT EXISTS `user_userbase_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userbase_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_userbase_user_permi_userbase_id_permission_i_da1ff290_uniq` (`userbase_id`,`permission_id`),
  KEY `user_userbase_user_permissions_userbase_id_225f8981` (`userbase_id`),
  KEY `user_userbase_user_permissions_permission_id_969f7fa8` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

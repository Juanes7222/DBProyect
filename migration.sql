--
-- Create model UserBase
--
CREATE TABLE `user_userbase` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `password` varchar(128) NOT NULL, `last_login` datetime(6) NULL, `is_superuser` BOOLEAN NOT NULL, `username` varchar(30) NOT NULL UNIQUE, `first_name` varchar(150) NOT NULL, `last_name` varchar(150) NOT NULL, `email` varchar(254) NOT NULL, `is_staff` BOOLEAN NOT NULL, `is_active` BOOLEAN NOT NULL, `date_joined` datetime(6) NOT NULL, `user_type` integer NOT NULL, `document` varchar(20) NOT NULL UNIQUE);
CREATE TABLE `user_userbase_groups` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `userbase_id` bigint NOT NULL, `group_id` integer NOT NULL);
CREATE TABLE `user_userbase_user_permissions` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `userbase_id` bigint NOT NULL, `permission_id` integer NOT NULL);
--
-- Create model Psychologist
--
CREATE TABLE `user_psychologist` (`user_id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `code` varchar(10) NOT NULL UNIQUE);
CREATE TABLE `user_psychologist_clients` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `psychologist_id` bigint NOT NULL, `userbase_id` bigint NOT NULL);
--
-- Create model Requests
--
CREATE TABLE `user_requests` (`req_id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `result` BOOLEAN NOT NULL, `user_id_id` bigint NOT NULL, `user_req_id` bigint NOT NULL);
--
-- Create model Forms
--
CREATE TABLE `user_forms` (`form_id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `salud` integer NOT NULL, `economia` integer NOT NULL, `trabajo` integer NOT NULL, `romance` integer NOT NULL, `crecimiento_personal` integer NOT NULL, `amigos` integer NOT NULL, `diversion` integer NOT NULL, `imagen_propia` integer NOT NULL, `ambiente_fisico` integer NOT NULL, `date` datetime(6) NOT NULL, `message` longtext NULL, `message_title` longtext NULL, `img` varchar(100) NULL, `user_id_id` bigint NOT NULL);
ALTER TABLE `user_userbase_groups` ADD CONSTRAINT `user_userbase_groups_userbase_id_group_id_617efe64_uniq` UNIQUE (`userbase_id`, `group_id`);
ALTER TABLE `user_userbase_groups` ADD CONSTRAINT `user_userbase_groups_userbase_id_746e0834_fk_user_userbase_id` FOREIGN KEY (`userbase_id`) REFERENCES `user_userbase` (`id`);
ALTER TABLE `user_userbase_groups` ADD CONSTRAINT `user_userbase_groups_group_id_70a2e1f4_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE INDEX `user_userbase_groups_userbase_id_746e0834` ON `user_userbase_groups` (`userbase_id`);
CREATE INDEX `user_userbase_groups_group_id_70a2e1f4` ON `user_userbase_groups` (`group_id`);
ALTER TABLE `user_userbase_user_permissions` ADD CONSTRAINT `user_userbase_user_permi_userbase_id_permission_i_da1ff290_uniq` UNIQUE (`userbase_id`, `permission_id`);
ALTER TABLE `user_userbase_user_permissions` ADD CONSTRAINT `user_userbase_user_p_userbase_id_225f8981_fk_user_user` FOREIGN KEY (`userbase_id`) REFERENCES `user_userbase` (`id`);
ALTER TABLE `user_userbase_user_permissions` ADD CONSTRAINT `user_userbase_user_p_permission_id_969f7fa8_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE INDEX `user_userbase_user_permissions_userbase_id_225f8981` ON `user_userbase_user_permissions` (`userbase_id`);
CREATE INDEX `user_userbase_user_permissions_permission_id_969f7fa8` ON `user_userbase_user_permissions` (`permission_id`);
ALTER TABLE `user_psychologist_clients` ADD CONSTRAINT `user_psychologist_client_psychologist_id_userbase_6e42431e_uniq` UNIQUE (`psychologist_id`, `userbase_id`);
ALTER TABLE `user_psychologist_clients` ADD CONSTRAINT `user_psychologist_cl_psychologist_id_41ce55bc_fk_user_psyc` FOREIGN KEY (`psychologist_id`) REFERENCES `user_psychologist` (`user_id`);
ALTER TABLE `user_psychologist_clients` ADD CONSTRAINT `user_psychologist_cl_userbase_id_69a82b1b_fk_user_user` FOREIGN KEY (`userbase_id`) REFERENCES `user_userbase` (`id`);
CREATE INDEX `user_psychologist_clients_psychologist_id_41ce55bc` ON `user_psychologist_clients` (`psychologist_id`);
CREATE INDEX `user_psychologist_clients_userbase_id_69a82b1b` ON `user_psychologist_clients` (`userbase_id`);
ALTER TABLE `user_requests` ADD CONSTRAINT `user_requests_user_id_id_c79ebd07_fk_user_userbase_id` FOREIGN KEY (`user_id_id`) REFERENCES `user_userbase` (`id`);
ALTER TABLE `user_requests` ADD CONSTRAINT `user_requests_user_req_id_f9a8d5a7_fk_user_psychologist_user_id` FOREIGN KEY (`user_req_id`) REFERENCES `user_psychologist` (`user_id`);
CREATE INDEX `user_requests_user_id_id_c79ebd07` ON `user_requests` (`user_id_id`);
CREATE INDEX `user_requests_user_req_id_f9a8d5a7` ON `user_requests` (`user_req_id`);
ALTER TABLE `user_forms` ADD CONSTRAINT `user_forms_user_id_id_f9aedbc1_fk_user_userbase_id` FOREIGN KEY (`user_id_id`) REFERENCES `user_userbase` (`id`);
CREATE INDEX `user_forms_user_id_id_f9aedbc1` ON `user_forms` (`user_id_id`);

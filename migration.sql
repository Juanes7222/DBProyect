BEGIN;
--
-- Create model UserBase
--
CREATE TABLE "user_userbase" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "user_type" integer NOT NULL, "document" varchar(20) NOT NULL UNIQUE);
CREATE TABLE "user_userbase_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "userbase_id" bigint NOT NULL REFERENCES "user_userbase" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "user_userbase_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "userbase_id" bigint NOT NULL REFERENCES "user_userbase" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Psychologist
--
CREATE TABLE "user_psychologist" ("user_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "code" varchar(10) NOT NULL UNIQUE);
CREATE TABLE "user_psychologist_clients" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "psychologist_id" bigint NOT NULL REFERENCES "user_psychologist" ("user_id") DEFERRABLE INITIALLY DEFERRED, "userbase_id" bigint NOT NULL REFERENCES "user_userbase" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Requests
--
CREATE TABLE "user_requests" ("req_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "result" bool NOT NULL, "user_id_id" bigint NOT NULL REFERENCES "user_userbase" ("id") DEFERRABLE INITIALLY DEFERRED, "user_req_id" bigint NOT NULL REFERENCES "user_psychologist" ("user_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Forms
--
CREATE TABLE "user_forms" ("form_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "salud" integer NOT NULL, "economia" integer NOT NULL, "trabajo" integer NOT NULL, "romance" integer NOT NULL, "crecimiento_personal" integer NOT NULL, "amigos" integer NOT NULL, "diversion" integer NOT NULL, "imagen_propia" integer NOT NULL, "ambiente_fisico" integer NOT NULL, "date" datetime NOT NULL, "message" text NULL, "message_title" text NULL, "user_id_id" bigint NOT NULL REFERENCES "user_userbase" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "user_userbase_groups_userbase_id_group_id_617efe64_uniq" ON "user_userbase_groups" ("userbase_id", "group_id");
CREATE INDEX "user_userbase_groups_userbase_id_746e0834" ON "user_userbase_groups" ("userbase_id");
CREATE INDEX "user_userbase_groups_group_id_70a2e1f4" ON "user_userbase_groups" ("group_id");
CREATE UNIQUE INDEX "user_userbase_user_permissions_userbase_id_permission_id_da1ff290_uniq" ON "user_userbase_user_permissions" ("userbase_id", "permission_id");
CREATE INDEX "user_userbase_user_permissions_userbase_id_225f8981" ON "user_userbase_user_permissions" ("userbase_id");
CREATE INDEX "user_userbase_user_permissions_permission_id_969f7fa8" ON "user_userbase_user_permissions" ("permission_id");
CREATE UNIQUE INDEX "user_psychologist_clients_psychologist_id_userbase_id_6e42431e_uniq" ON "user_psychologist_clients" ("psychologist_id", "userbase_id");
CREATE INDEX "user_psychologist_clients_psychologist_id_41ce55bc" ON "user_psychologist_clients" ("psychologist_id");
CREATE INDEX "user_psychologist_clients_userbase_id_69a82b1b" ON "user_psychologist_clients" ("userbase_id");
CREATE INDEX "user_requests_user_id_id_c79ebd07" ON "user_requests" ("user_id_id");
CREATE INDEX "user_requests_user_req_id_f9a8d5a7" ON "user_requests" ("user_req_id");
CREATE INDEX "user_forms_user_id_id_f9aedbc1" ON "user_forms" ("user_id_id");
COMMIT;

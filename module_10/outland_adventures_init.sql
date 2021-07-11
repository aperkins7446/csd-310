
DROP DATABASE IF EXISTS outland_adventures;
CREATE DATABASE outland_adventures;
DROP USER IF EXISTS 'outland_adventures_user'@'localhost';
-- create outland_adventures_user and grant them all priveledges to the outland_adventures database
CREATE USER 'outland_adventures_user'@'localhost' IDENTIFIED WITH mysql_native_password By 'Angel@84';
-- grant all priveleges to the outland_adventures database to user outland_adventures_user on localhost
GRANT ALL PRIVILEGES ON outland_adventures.* TO 'outland_adventures_user'@'localhost';
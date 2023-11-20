--  script that prepares a MySQL server
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
USE hbnb_dev_db;
-- Crea o usa un usuario existente en hbnb_dev en el localhost
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* to ' hbnb_dev'@'localhost';
SHOW DATABASES;
--  script that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- -- Create or use the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* to ' hbnb_dev'@'localhost';

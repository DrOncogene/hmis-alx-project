-- sets up a dev db and creates a new user
CREATE DATABASE IF NOT EXISTS hmis_dev_db;
CREATE USER IF NOT EXISTS 'hmis_dev'@'localhost' IDENTIFIED BY 'hmis_pwd';
GRANT ALL PRIVILEGES ON `hmis_dev_db`.* TO 'hmis_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hmis_dev'@'localhost';
FLUSH PRIVILEGES;

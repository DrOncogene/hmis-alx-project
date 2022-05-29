-- sets up a dev db and creates a new user
CREATE DATABASE IF NOT EXISTS hmis_test_db;
CREATE USER IF NOT EXISTS 'hmis_test'@'localhost' IDENTIFIED BY 'hmis_pwd';
GRANT ALL PRIVILEGES ON `hmis_test_db`.* TO 'hmis_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hmis_test'@'localhost';
FLUSH PRIVILEGES;

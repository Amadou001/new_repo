CREATE DATABASE IF NOT EXISTS roofmarket_db;
CREATE USER 'roofmarket_user'@'localhost' IDENTIFIED BY 'roofmarket_pwd';
GRANT ALL PRIVILEGES ON roofmarket_db.* TO 'roofmarket_user'@'localhost';
FLUSH PRIVILEGES;

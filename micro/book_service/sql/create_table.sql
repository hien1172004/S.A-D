CREATE DATABASE book_service_db;
USE book_service_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

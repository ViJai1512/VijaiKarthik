CREATE DATABASE retail_inventory;
USE retail_inventory;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    supplier VARCHAR(100)
);

CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO products (product_name, category, price, supplier)
VALUES
('Laptop', 'Electronics', 55000, 'HP Pvt Ltd'),
('Mobile', 'Electronics', 25000, 'Samsung Co'),
('Headphones', 'Accessories', 2000, 'Boat Ltd');

INSERT INTO inventory (product_id, stock)
VALUES
(1, 50),
(2, 30),
(3, 10);

INSERT INTO sales (product_id, quantity, sale_date)
VALUES
(1, 2, '2025-01-10'),
(2, 1, '2025-01-11'),
(3, 3, '2025-01-12');

SELECT * FROM products;
SELECT * FROM inventory;
SELECT * FROM sales;

UPDATE inventory
SET stock = 45
WHERE product_id = 1;

DELETE FROM sales
WHERE sale_id = 3;

DELIMITER $$

CREATE PROCEDURE sp_low_stock()
BEGIN
    SELECT p.product_name, i.stock
    FROM products p
    JOIN inventory i ON p.product_id = i.product_id
    WHERE i.stock < 15;
END$$

DELIMITER ;


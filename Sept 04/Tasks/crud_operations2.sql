create Table orders(
order_id int primary key auto_increment,
customer_name varchar(100),
product varchar(100),
quantity int,
price decimal(10,2),
order_date date
);

INSERT INTO orders (customer_name, product, quantity, price, order_date) VALUES
('Rahul Sharma', 'Laptop', 1, 55000.00, '2025-01-05'),
('Priya Singh', 'Headphones', 2, 3000.00, '2025-01-06'),
('Aman Kumar', 'Mobile Phone', 1, 25000.00, '2025-01-06'),
('Sneha Reddy', 'Keyboard', 3, 1500.00, '2025-01-07'),
('Arjun Mehta', 'Monitor', 2, 12000.00, '2025-01-07'),
('Pooja Iyer', 'Laptop', 1, 60000.00, '2025-01-08'),
('Ravi Sharma', 'Mouse', 5, 800.00, '2025-01-08'),
('Neha Kapoor', 'Tablet', 1, 20000.00, '2025-01-09'),
('Vikram Rao', 'Printer', 1, 8500.00, '2025-01-09'),
('Divya Nair', 'Laptop', 2, 58000.00, '2025-01-10');

select * from orders where order_date = '2025-01-07';


SELECT COUNT(*) AS total_orders FROM orders;

SELECT AVG(price) AS average_price FROM orders;

SELECT MAX(price) AS max_price FROM orders;

SELECT SUM(quantity) AS total_quantity_sold FROM orders;

SELECT product, SUM(quantity * price) AS total_sales
FROM orders
GROUP BY product;

SELECT product, COUNT(*) AS order_count
FROM orders
GROUP BY product;

SELECT customer_name, AVG(price) AS avg_price_per_customer
FROM orders
GROUP BY customer_name;

SELECT product, SUM(quantity) AS total_quantity
FROM orders
GROUP BY product
HAVING SUM(quantity) > 3;

SELECT customer_name, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_name
HAVING COUNT(*) > 1;




create database hexadb;

use hexadb;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

INSERT INTO departments (dept_name, location) VALUES
('IT', 'Bangalore'),
('HR', 'Hyderabad'),
('Finance', 'Mumbai'),
('Marketing', 'Delhi'),
('Operations', 'Chennai');

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    dept_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO employees (emp_id, first_name, last_name, age, dept_id, salary) VALUES
(101, 'Amit', 'Verma', 28, 1, 55000.00),   -- belongs to IT
(102, 'Sneha', 'Reddy', 32, 2, 60000.00),  -- belongs to HR
(103, 'Ravi', 'Sharma', 26, NULL, 48000.00), -- employee with NO department
(104, 'Pooja', 'Iyer', 29, 4, 52000.00),   -- belongs to Marketing
(105, 'Arjun', 'Mehta', 31, 1, 75000.00);  -- belongs to IT

SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, d.location
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, d.location
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id

UNION

SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, d.location
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

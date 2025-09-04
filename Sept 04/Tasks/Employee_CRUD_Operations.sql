-- Create database
CREATE DATABASE company_db;

-- Use the database
USE company_db;

-- Create employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employees (first_name, last_name, age, department, salary)
VALUES 
('John', 'Doe', 28, 'IT', 55000),
('Alice', 'Smith', 32, 'Finance', 60000),
('Bob', 'Johnson', 26, 'HR', 45000),
('Charlie', 'Brown', 30, 'IT', 58000),
('Diana', 'Williams', 35, 'Accounts', 65000);


-- Display all employees
SELECT * FROM employees;

-- Display only sp
SELECT first_name, department, salary FROM employees;

-- Find all employees who belong to the IT department
SELECT * FROM employees WHERE department = 'IT';

-- Update department of one employee from "Finance" to "Accounts"
UPDATE employees
SET department = 'Accounts'
WHERE department = 'Finance'
LIMIT 1;

-- Delete an employee from the HR department
DELETE FROM employees
WHERE department = 'HR'
LIMIT 1;


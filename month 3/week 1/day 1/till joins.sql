create database company;

use company;

create table employees(id serial primary key,
name varchar(50),
department varchar(100),
salary decimal(10.5),
city varchar(50));

show tables;

INSERT INTO employees (name, department, salary, city)
VALUES ('Gurman', 'IT', 10000.5, 'Indore'),
 ('Avantika', 'IT', 10000.5, 'Indore'),
 ('yo', 'IT', 10000.5, 'Indore'),
 ('ehhehe', 'IT', 10000.5, 'Indore');
 
select * from employees;  # to show table
 select * from employees order by salary desc; # order desc salary print
SELECT * FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1; # limit value to 1 and offset means values skip
delete from employees where name='Gurman';
select distinct name from employees; #distinct values 
# agggregate funct 5 count,avg,sum,min,max

#create another table and try to connect with previous table 
create table departments(id serial primary key,department_name varchar(50));
INSERT INTO departments(department_name) 
values('it'),('hr'),('finance'),('marketing'),('sales');

CREATE TABLE employee_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id BIGINT UNSIGNED,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
);
INSERT INTO employee_details (name, department_id, salary)
VALUES
('Gurman', 1, 40000),
('Avantika', 2, 50000),
('Ravi', 1, 45000),
('Aman', 3, 55000);

-- joins 
select e.name,e.salary,d.department_name from employee_details e inner join departments d on e.department_id=d.id;
select e.name,e.salary,d.department_name from employee_details e right join departments d on e.department_id=d.id;
select e.name,e.salary,d.department_name from employee_details e left join departments d on e.department_id=d.id;
select e.name,e.salary,d.department_name from employee_details e join departments d on e.department_id=d.id;

-- group by= used with aggregate functions
-- having=conditions 
CREATE DATABASE IF NOT EXISTS  ParkDB;
USE DATABASE ParkDB;

-- Схеми
CREATE SCHEMA IF NOT EXISTS  VISITORS;
CREATE  SCHEMA IF NOT EXISTS  ATTRACTIONS;
CREATE  SCHEMA IF NOT EXISTS  EMPLOYEES;
CREATE  SCHEMA IF NOT EXISTS  STORES;
CREATE SCHEMA IF NOT EXISTS  EVENTS;
CREATE  SCHEMA IF NOT EXISTS  FINANCES;

-- Посетители, посещения и билети

USE SCHEMA VISITORS;

CREATE OR REPLACE TABLE VISITORS.Visitors(
    visitor_id INT AUTOINCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30)
);

CREATE OR REPLACE TABLE VISITORS.Tickets(
    ticket_id INT AUTOINCREMENT,
    visitor_id INT,
    ticket_type VARCHAR(10),
    price FLOAT,
    purchase_time TIMESTAMP_LTZ DEFAULT CURRENT_TIMESTAMP --TIMESTAMP за да следим и часа на покупка, може да е закупен преди посещение
);

CREATE OR REPLACE TABLE VISITORS.Entries(
    entry_id INT AUTOINCREMENT,
    visitor_id INT,
    ticket_id INT,
    entry_time TIMESTAMP_LTZ DEFAULT CURRENT_TIMESTAMP,
    leave_time TIMESTAMP_LTZ
);

-- Атракциони и поддръжка

USE SCHEMA ATTRACTIONS;

CREATE OR REPLACE TABLE ATTRACTIONS.Attractions (
    attraction_id INT AUTOINCREMENT,
    name VARCHAR(20),
    capacity INT,
    age_restriction INT,
    category VARCHAR(20),
    status STRING -- Отворен, затворен, ремонт
);

CREATE OR REPLACE TABLE ATTRACTIONS.MaintenanceRecords(
    maintenance_id INT AUTOINCREMENT,
    attraction_id INT,
    description STRING,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE
);

-- Магазини/Ресторанти и продукти за хранене

USE SCHEMA STORES;

CREATE OR REPLACE TABLE STORES.Stores(
    store_id INT AUTOINCREMENT,
    name VARCHAR(20),
    category VARCHAR(20), -- Магазини, ресторанти и т.н.
    opening_time TIME,
    closing_time TIME
);

CREATE OR REPLACE TABLE STORES.Products(
    product_id INT AUTOINCREMENT PRIMARY KEY,
    store_id INT,
    category STRING, -- Храна, напитки, дрехи и т.н.
    name STRING,
    price FLOAT
);

CREATE OR REPLACE TABLE STORES.Inventory(
    inventory_id INT AUTOINCREMENT PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity INT
);

CREATE OR REPLACE TABLE STORES.Sales(
    sale_id INT AUTOINCREMENT PRIMARY KEY,
    store_id INT,
    product_id INT,
    quantity INT,
    total_price FLOAT
);

-- Финанси

USE SCHEMA FINANCES;

CREATE OR REPLACE TABLE FINANCES.Expenses(
    expense_id INT AUTOINCREMENT PRIMARY KEY,
    expense_type STRING,
    amount FLOAT,
    expense_date DATE DEFAULT CURRENT_DATE -- При въвеждане на разход, датата е текущата по подразбиране
);

CREATE OR REPLACE TABLE FINANCES.Incomes(
    income_id INT AUTOINCREMENT PRIMARY KEY,
    income_type STRING,
    amount FLOAT,
    income_date DATE DEFAULT CURRENT_DATE -- Същото като за разходите
);


-- Служители, отдели, позиции, смени, плащания

USE SCHEMA EMPLOYEES;

CREATE OR REPLACE TABLE EMPLOYEES.Employees(
    employee_id INT AUTOINCREMENT PRIMARY KEY,
    department_id INT,
    first_name STRING,
    last_name STRING,
    position_id INT ,
    manager_id INT   -- Мениджър на служителя, ако има такъв (може да е NULL)

);

CREATE OR REPLACE TABLE EMPLOYEES.Departments(
    department_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    manager_id INT -- Мениджър на отдела, ако има такъв (може да е NULL)

);

CREATE OR REPLACE TABLE EMPLOYEES.Positions(
    position_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    base_salary FLOAT
);

CREATE OR REPLACE TABLE EMPLOYEES.Payroll(
    payment_id INT AUTOINCREMENT PRIMARY KEY,
    employee_id INT,
    payment_date DATE,
    amount FLOAT,
    bonus FLOAT

);

CREATE OR REPLACE TABLE EMPLOYEES.Shifts(
    shift_id INT AUTOINCREMENT PRIMARY KEY,
    employee_id INT,
    name VARCHAR(20),
    start_time TIME,
    end_time TIME

);

-- Събития

USE SCHEMA EVENTS;

CREATE OR REPLACE TABLE EVENTS.Events(
    event_id INT AUTOINCREMENT PRIMARY KEY,
    name STRING,
    category STRING, -- Специални събития, концерти, промоции
    description STRING,
    start_date DATE,
    end_date DATE
);
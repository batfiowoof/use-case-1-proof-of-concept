CREATE DATABASE ParkDB;
USE ParkDB;

-- Схеми
CREATE SCHEMA VISITORS;
CREATE SCHEMA ATTRACTIONS;
CREATE SCHEMA EMPLOYEES;
CREATE SCHEMA STORES;
CREATE SCHEMA EVENTS;
CREATE SCHEMA FINANCES;

-- Посетители, посещения и билети

CREATE TABLE VISITORS.Visitors(
    VisitorID INT AUTOINCREMENT PRIMARY KEY,
    FirstName STRING, --Може и с VARCHAR, но в документацията прочетох, че при STRING не е необходимо да задаваме лимит пр. VARCHAR(30)
    LastName STRING
);

CREATE TABLE VISITORS.Tickets(
    TicketID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT FOREIGN KEY REFERENCES Visitors(VisitorID),
    TicketType STRING,
    Price FLOAT,
    PurchaseTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP --TIMESTAMP за да следим и часа на покупка, може да е закупен преди посещение
);

CREATE TABLE VISITORS.Entries(
    EntryID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT FOREIGN KEY REFERENCES Visitors(VisitorID),
    TicketID INT FOREIGN KEY REFERENCES Tickets(TicketID),
    EntryTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    LeaveTime TIMESTAMP
);

-- Атракциони и поддръжка

CREATE TABLE ATTRACTIONS.Attractions (
    AttractionID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING,
    Category STRING
);

CREATE TABLE ATTRACTIONS.MaintenanceRecords(
    MaintenanceID INT AUTOINCREMENT PRIMARY KEY,
    AttractionID INT FOREIGN KEY REFERENCES Attractions(AttractionID),
    Description STRING,
    StartDate DATE DEFAULT CURRENT_DATE,
    EndDate DATE
);

-- Магазини/Ресторанти и продукти за хранене

CREATE TABLE STORES.Stores(
    StoreID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING,
    Category STRING -- Магазини, ресторанти и т.н.
);

CREATE TABLE STORES.Products(
    ProductID INT AUTOINCREMENT PRIMARY KEY,
    StoreID INT FOREIGN KEY REFERENCES Stores(StoreID),
    Category STRING, -- Храна, напитки, дрехи и т.н.
    Name STRING,
    PRICE FLOAT
);

CREATE TABLE STORES.Sales(
    SaleID INT AUTOINCREMENT PRIMARY KEY,
    StoreID INT FOREIGN KEY REFERENCES Stores(StoreID),
    FoodID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT,
    TotalPrice FLOAT
);

-- Финанси

CREATE TABLE FINANCES.Expenses(
    ExpenseID INT AUTOINCREMENT PRIMARY KEY,
    ExpenseType STRING,
    Amount FLOAT,
    ExpenseDate DATE DEFAULT CURRENT_DATE -- При въвеждане на разход, датата е текущата по подразбиране
);

CREATE TABLE FINANCES.Incomes(
    IncomeID INT AUTOINCREMENT PRIMARY KEY,
    IncomeType STRING,
    Amount FLOAT,
    IncomeDate DATE DEFAULT CURRENT_DATE -- Същото като за разходите
);

CREATE TABLE EMPLOYEES.Payroll(
    PaymentID INT AUTOINCREMENT PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employees(EmployeeID),
    PaymentDate DATE,
    Amount FLOAT,
    Bonus FLOAT
);

-- Служители, отдели, позиции, смени, плащания

CREATE TABLE EMPLOYEES.Departments(
    DepartmentID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING
);

CREATE TABLE EMPLOYEES.Positions(
    PositionID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING
);

CREATE TABLE EMPLOYEES.Employees(
    EmployeeID INT AUTOINCREMENT PRIMARY KEY,
    DepartmentID INT FOREIGN KEY REFERENCES Departments(DepartmentID),
    FirstName STRING,
    LastName STRING,
    PositionID INT FOREIGN KEY REFERENCES Positions(PositionID),
    ManagerID INT FOREIGN KEY REFERENCES Employees(EmployeeID) -- Мениджър на служителя, ако има такъв (може да е NULL)
);

CREATE TABLE EMPLOYEES.Shifts(
    ShiftID INT AUTOINCREMENT PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employees(EmployeeID),
    ShiftDate DATE,
    HoursWorked FLOAT
);

-- Събития

CREATE TABLE EVENTS.Events(
    EventID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING,
    Category STRING, -- Специални събития, концерти, промоции
    Description STRING,
    StartDate DATE,
    EndDate DATE
);
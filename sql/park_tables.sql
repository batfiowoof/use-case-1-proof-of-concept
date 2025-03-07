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
    FirstName STRING NOT NULL , --Може и с VARCHAR, но в документацията прочетох, че при STRING не е необходимо да задаваме лимит пр. VARCHAR(30)
    LastName STRING NOT NULL
);

CREATE TABLE VISITORS.Tickets(
    TicketID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT FOREIGN KEY REFERENCES Visitors(VisitorID),
    TicketType STRING NOT NULL ,
    Price FLOAT NOT NULL ,
    PurchaseTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP --TIMESTAMP за да следим и часа на покупка, може да е закупен преди посещение
);

CREATE TABLE VISITORS.Entries(
    EntryID INT AUTOINCREMENT PRIMARY KEY,
    VisitorID INT FOREIGN KEY REFERENCES Visitors(VisitorID),
    TicketID INT FOREIGN KEY REFERENCES Tickets(TicketID),
    EntryTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    LeaveTime TIMESTAMP
);

-- Атракциони и поддръжка

CREATE TABLE ATTRACTIONS.Attractions (
    AttractionID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING NOT NULL,
    Category STRING NOT NULL,
    Capacity INT NOT NULL,
    AgeRestriction INT NOT NULL,
    Status STRING NOT NULL -- Отворен, затворен, поддръжка
);

CREATE TABLE ATTRACTIONS.MaintenanceRecords(
    MaintenanceID INT AUTOINCREMENT PRIMARY KEY,
    AttractionID INT FOREIGN KEY REFERENCES Attractions(AttractionID),
    Description STRING NOT NULL,
    StartDate DATE DEFAULT CURRENT_DATE NOT NULL,
    EndDate DATE
);

-- Магазини/Ресторанти и продукти за хранене

CREATE TABLE STORES.Stores(
    StoreID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING NOT NULL,
    Category STRING NOT NULL, -- Магазини, ресторанти и т.н.
    OpeningTime TIME NOT NULL,
    ClosingTime TIME NOT NULL
);

CREATE TABLE STORES.Products(
    ProductID INT AUTOINCREMENT PRIMARY KEY,
    StoreID INT FOREIGN KEY REFERENCES Stores(StoreID), -- От кой магазин е продуктът
    Category STRING NOT NULL, -- Храна, напитки, дрехи и т.н.
    Name STRING NOT NULL,
    PRICE FLOAT NOT NULL
);

CREATE TABLE Stores.Inventory(
    InventoryID INT AUTOINCREMENT PRIMARY KEY,
    StoreID INT FOREIGN KEY REFERENCES Stores(StoreID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT
);

CREATE TABLE STORES.Sales(
    SaleID INT AUTOINCREMENT PRIMARY KEY,
    StoreID INT FOREIGN KEY REFERENCES Stores(StoreID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT NOT NULL,
    TotalPrice FLOAT NOT NULL
);

-- Финанси

CREATE TABLE FINANCES.Expenses(
    ExpenseID INT AUTOINCREMENT PRIMARY KEY,
    ExpenseType STRING NOT NULL , -- Какъв е разхода - наем, поддръжка и т.н.
    Amount FLOAT NOT NULL,
    ExpenseDate DATE DEFAULT CURRENT_DATE -- При въвеждане на разход, датата е текущата по подразбиране
);

CREATE TABLE FINANCES.Incomes(
    IncomeID INT AUTOINCREMENT PRIMARY KEY,
    IncomeType STRING NOT NULL, -- Какъв е прихода - билети, продажби и т.н.
    Amount FLOAT NOT NULL,
    IncomeDate DATE DEFAULT CURRENT_DATE -- Същото като за разходите
);

CREATE TABLE FINANCES.Payroll(
    PaymentID INT AUTOINCREMENT PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES EMPLOYEES.Employees(EmployeeID),
    PaymentDate DATE NOT NULL ,
    Amount FLOAT NOT NULL ,
    OvertimeHours FLOAT,
    OvertimePay FLOAT,
    Bonus FLOAT
);

-- Служители, отдели, позиции, смени, плащания

CREATE TABLE EMPLOYEES.Departments(
    DepartmentID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING NOT NULL,
    ManagerID INT FOREIGN KEY REFERENCES Employees(EmployeeID) -- Мениджър на отдела, ако има такъв (може да е NULL)
);

CREATE TABLE EMPLOYEES.Positions(
    PositionID INT AUTOINCREMENT PRIMARY KEY,
    Name STRING NOT NULL,
    BaseSalary FLOAT NOT NULL
);

CREATE TABLE EMPLOYEES.Employees(
    EmployeeID INT AUTOINCREMENT PRIMARY KEY,
    FirstName STRING  NOT NULL,
    LastName STRING NOT NULL,
    DepartmentID INT FOREIGN KEY REFERENCES Departments(DepartmentID),
    PositionID INT FOREIGN KEY REFERENCES Positions(PositionID),
    ManagerID INT FOREIGN KEY REFERENCES Employees(EmployeeID), -- Мениджър на служителя, ако има такъв (може да е NULL)
    ShiftID INT FOREIGN KEY REFERENCES Shifts(ShiftID)
);

CREATE TABLE EMPLOYEES.Shifts(
    ShiftID INT AUTOINCREMENT PRIMARY KEY,
    ShiftName STRING NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL
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
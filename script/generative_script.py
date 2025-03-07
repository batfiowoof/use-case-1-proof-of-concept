import random
import datetime

def generate_inserts(business_climate):
    insert_statements = []

    #Visitors
    first_names = ['Bozhidar', 'Mihail' , 'Georgi', 'Plamen', 'Petar']
    last_names = ['Petrov', 'Lambov', 'Dimitrov', 'Stoyanov', 'Nikolov']

    for _ in range(100 if business_climate == 'positive' else 20):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        insert_statements.append(f"INSERT INTO VISITORS.Visitors (FirstName, LastName) VALUES ('{first_name}', '{last_name}');")


    #Tickets
    ticket_types = ['Standard','VIP']
    price_range = (30,100) if business_climate == 'positive' else (10, 50)
    for visitor_id in range(1, 101 if business_climate == 'positive' else 21):
        ticket_type = random.choice(ticket_types)
        price = round(random.uniform(price_range[0], price_range[1]), 2)
        insert_statements.append(f"INSERT INTO VISITORS.Tickets (VisitorId, TicketType, Price) VALUES ({visitor_id}, '{ticket_type}', {price});")

    #Entries
    for entry_id in range(1, 101 if business_climate == 'positive' else 21):
        entry_time = datetime.datetime.now() - datetime.timedelta(hours = random.randint(1, 8))
        leave_time = entry_time + datetime.timedelta(hours=random.randint(2, 6))
        entry_time = entry_time.strftime('%Y-%m-%d %H:%M:%S')
        leave_time = leave_time.strftime('%Y-%m-%d %H:%M:%S')
        insert_statements.append(f"INSERT INTO VISITORS.Entries (EntryTime, LeaveTime, VisitorId, TicketID) VALUES ('{entry_time}', '{leave_time}', {entry_id}, {entry_id});")

    #Attractions
    attraction_names = ['Rollercoaster', 'Ferris Wheel', 'Haunted House', 'Carousel', 'Bumper Cars']
    attraction_categories = ['Thrill', 'Family', 'Horror', 'Kids', 'Fun']
    for attraction_id in range(1, 6):
        attraction_name = attraction_names[attraction_id - 1]
        attraction_category = attraction_categories[attraction_id - 1]
        insert_statements.append(f"INSERT INTO ATTRACTIONS.Attractions (AttractionName, Category) VALUES ('{attraction_name}', '{attraction_category}');")

    #Maintenance records
    descriptions = ['Cleaning', 'Repair', 'Inspection', 'Replacement', 'Upgrade']
    for maintenance_id in range(1, 6):
        start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        end_date = start_date + datetime.timedelta(days=random.randint(1, 5))
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        description = random.choice(descriptions)
        insert_statements.append(f"INSERT INTO ATTRACTIONS.MaintenanceRecords (StartDate, EndDate, Description, AttractionID) VALUES ('{start_date}', '{end_date}', '{description}', {maintenance_id});")

    #Stores
    store_names = ['Souvenirs', 'Snacks', 'Drinks', 'Toys', 'Books']
    store_categories = ['Restaurant', 'Cafe', 'Bar', 'Shop', 'Kiosk']
    for store_id in range(1, 6):
        store_name = random.choice(store_names)
        store_category = random.choice(store_categories)
        insert_statements.append(f"INSERT INTO STORES.Stores (StoreName, Category) VALUES ('{store_name}', '{store_category}');")

    #Products
    product_names = ['T-shirt', 'Magnet', 'Cup', 'Keychain', 'Book']
    product_categories = ['Clothing', 'Accessories', 'Kitchenware', 'Souvenirs', 'Books']
    product_prices = (20, 50)
    for product_id in range(1, 6):
        product_name = product_names[product_id - 1]
        product_category = product_categories[product_id - 1]
        product_price = round(random.uniform(product_prices[0], product_prices[1]), 2)
        insert_statements.append(f"INSERT INTO STORES.Products (ProductName, Category, Price) VALUES ('{product_name}', '{product_category}', {product_price});")

    #Sales

    for sale_id in range(100,150 if business_climate == 'positive' else 20):
        quantity = random.randint(50, 100 if business_climate == 'positive' else 20)
        total_price = round(quantity * random.uniform(product_price[0], product_price[1]), 2)
        insert_statements.append(f"INSERT INTO STORES.Sales (ProductID, StoreID, Quantity, TotalPrice) VALUES ({sale_id}, {sale_id}, {quantity}, {total_price});")

    #Expenses
    expense_types = ['Rent', 'Utilities', 'Salaries', 'Maintenance', 'Supplies']
    amount = (1000, 2000)
    for expense_id in range(1, 6):
        expense_type = random.choice(expense_types)
        expense_amount = round(random.uniform(amount[0], amount[1]), 2)
        expense_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        expense_date = expense_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO FINANCE.Expenses (ExpenseType, Amount, ExpenseDate) VALUES ('{expense_type}', {expense_amount}, '{expense_date}');")

    #Income
    income_types = ['Ticket Sales', 'Store Sales', 'Donations', 'Sponsorships', 'Grants']
    amount = (5000, 10000 if business_climate == 'positive' else 2000)
    for income_id in range(1, 6):
        income_type = random.choice(income_types)
        income_amount = round(random.uniform(amount[0], amount[1]), 2)
        income_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        income_date = income_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO FINANCE.Income (IncomeType, Amount, IncomeDate) VALUES ('{income_type}', {income_amount}, '{income_date}');")

    #Departments
    department_names = ['Marketing', 'Finance', 'Maintenance', 'Security', 'HR']
    for department_id in range(1, 6):
        department_name = department_names[department_id - 1]
        insert_statements.append(f"INSERT INTO EMPLOYEES.Departments (Name) VALUES ('{department_name}');")

    #Positions
    position_names = ['Manager', 'Supervisor', 'Employee', 'Security Guard', 'Janitor']
    for position_id in range(1, 6):
        position_name = position_names[position_id - 1]
        insert_statements.append(f"INSERT INTO EMPLOYEES.Positions (Name) VALUES ('{position_name}');")

    #Employees
    for employee_id in range(1, 6):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        department_id = random.randint(1, 5)
        position_id = random.randint(1, 5)
        manager_id = 'NULL'
        if employee_id % 2 == 0:
            manager_id = employee_id - 1
        insert_statements.append(f"INSERT INTO EMPLOYEES.Employees (FirstName, LastName, DepartmentID, PositionID, ManagerID) VALUES ('{first_name}', '{last_name}', {department_id}, {position_id}, {manager_id});")

    #Shifts
    shift_dates = [datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30)) for _ in range(5)]
    hours_worked = [8, 10, 12]
    for shift_id in range(1, 6):
        employee_id = shift_id
        shift_date = shift_dates[shift_id - 1]
        shift_date = shift_date.strftime('%Y-%m-%d')
        hours = random.choice(hours_worked)
        insert_statements.append(f"INSERT INTO EMPLOYEES.Shifts (EmployeeID, ShiftDate, HoursWorked) VALUES ({employee_id}, '{shift_date}', {hours});")

    #Payroll
    payroll_amounts = [1000, 2000, 3000, 4000, 5000]
    payroll_bonuses = [100, 200, 300, 400, 500]
    for payroll_id in range(1, 6):
        employee_id = payroll_id
        amount = payroll_amounts[payroll_id - 1]
        bonus = payroll_bonuses[payroll_id - 1]
        payment_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        payment_date = payment_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO EMPLOYEES.Payroll (EmployeeID, Amount, Bonus, PaymentDate) VALUES ({employee_id}, {amount}, {bonus}, '{payment_date}');")

    #Events
    event_names = ['Concert', 'Festival', 'Exhibition', 'Workshop', 'Conference']
    event_categories = ['Music', 'Art', 'Science', 'Education', 'Business']
    for event_id in range(1, 6):
        event_name = event_names[event_id - 1]
        event_category = event_categories[event_id - 1]
        start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        end_date = start_date + datetime.timedelta(days=random.randint(1, 5))
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO EVENTS.Events (Name, Category, StartDate, EndDate) VALUES ('{event_name}', '{event_category}', '{start_date}', '{end_date}');")

    return insert_statements

def main():
    business_climate = input('Enter business climate: (positive/negative)').strip().lower()
    if business_climate not in ['positive', 'negative']:
        print('Invalid input')
        return

    insert_statements = generate_inserts(business_climate)

    with open('insert_statements.sql', 'w') as f:
        for statement in insert_statements:
            f.write(statement + '\n')

    print('Insert statements generated successfully')

if __name__ == '__main__':
    main()
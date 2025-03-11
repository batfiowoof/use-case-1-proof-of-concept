import random
import datetime

def generate_inserts(business_climate):
    insert_statements = []

    #Посетители
    first_names = ['Bozhidar', 'Mihail' , 'Georgi', 'Plamen', 'Petar']
    last_names = ['Petrov', 'Lambov', 'Dimitrov', 'Stoyanov', 'Nikolov']


    insert_statements.append("USE DATABASE ParkDB;")

    insert_statements.append("USE SCHEMA VISITORS;")
    for _ in range(100 if business_climate == 'positive' else 20):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        insert_statements.append(f"INSERT INTO VISITORS.Visitors (first_name, last_name) VALUES ('{first_name}', '{last_name}');")


    #Билети
    ticket_types = ['Standard','VIP']
    price_range = (30,100) if business_climate == 'positive' else (10, 50)
    for visitor_id in range(1, 101 if business_climate == 'positive' else 21):
        ticket_type = random.choice(ticket_types)
        price = round(random.uniform(price_range[0], price_range[1]), 2)
        purchase_time = datetime.datetime.now() - datetime.timedelta(hours=random.randint(1, 8))
        purchase_time = purchase_time.strftime('%Y-%m-%d %H:%M:%S')
        insert_statements.append(f"INSERT INTO VISITORS.Tickets (ticket_type, price, purchase_time, visitor_id) VALUES ('{ticket_type}', {price}, '{purchase_time}', {visitor_id});")

    #Посещения
    for entry_id in range(1, 101 if business_climate == 'positive' else 21):
        entry_time = datetime.datetime.now() - datetime.timedelta(hours = random.randint(1, 8))
        leave_time = entry_time + datetime.timedelta(hours=random.randint(2, 6))
        entry_time = entry_time.strftime('%Y-%m-%d %H:%M:%S')
        leave_time = leave_time.strftime('%Y-%m-%d %H:%M:%S')
        insert_statements.append(f"INSERT INTO VISITORS.Entries (entry_time, leave_time, visitor_id, ticket_id) VALUES ('{entry_time}', '{leave_time}', {entry_id}, {entry_id});")

    #Атракциони
    attraction_names = ['Rollercoaster', 'Ferris Wheel', 'Haunted House', 'Carousel', 'Bumper Cars']
    attraction_categories = ['Thrill', 'Family', 'Horror', 'Kids', 'Fun']
    attraction_capacities = [50, 100, 20, 30, 40]
    attraction_age_restrictions = [16, 10, 18, 5, 12]
    attraction_statuses = ['Open', 'Closed', 'Under Maintenance']

    insert_statements.append("USE SCHEMA ATTRACTIONS;")
    for attraction_id in range(1, 6):
        attraction_name = attraction_names[attraction_id - 1]
        attraction_category = attraction_categories[attraction_id - 1]
        attraction_capacity = attraction_capacities[attraction_id - 1]
        attraction_age_restriction = attraction_age_restrictions[attraction_id - 1]
        attraction_status = random.choice(attraction_statuses)
        insert_statements.append(f"INSERT INTO ATTRACTIONS.Attractions (name, category, capacity, age_restriction, status) VALUES ('{attraction_name}', '{attraction_category}', {attraction_capacity}, {attraction_age_restriction}, '{attraction_status}');")

    #Поддръжка
    descriptions = ['Cleaning', 'Repair', 'Inspection', 'Replacement', 'Upgrade']
    for maintenance_id in range(1, 6):
        start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        end_date = start_date + datetime.timedelta(days=random.randint(1, 5))
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        description = random.choice(descriptions)
        insert_statements.append(f"INSERT INTO ATTRACTIONS.MaintenanceRecords (start_date, end_date, description, attraction_id) VALUES ('{start_date}', '{end_date}', '{description}', {maintenance_id});")

    #Магазини
    store_names = ['Steak Dreams', 'Cafe Latte', 'Bar Hopper', 'Gift Shop', 'Snack Shack']
    store_categories = ['Restaurant', 'Cafe', 'Bar', 'Shop', 'Kiosk']

    insert_statements.append("USE SCHEMA STORES;")
    for store_id in range(1, 6):
        store_name = random.choice(store_names)
        store_category = random.choice(store_categories)
        opening_time = datetime.datetime.now() - datetime.timedelta(hours=random.randint(1, 8))
        closing_time = opening_time + datetime.timedelta(hours=random.randint(2, 6))
        opening_time = opening_time.strftime('%H:%M:%S')
        closing_time = closing_time.strftime('%H:%M:%S')
        insert_statements.append(f"INSERT INTO STORES.Stores (name, category, opening_time, closing_time) VALUES ('{store_name}', '{store_category}', '{opening_time}', '{closing_time}');")

    #Продукти
    product_names = ['T-shirt', 'Magnet', 'Cup', 'Keychain', 'Book']
    product_categories = ['Clothing', 'Accessories', 'Kitchenware', 'Souvenirs', 'Books']
    product_prices = (20, 50) if business_climate == 'positive' else (10, 30)
    for product_id in range(1, 6):
        product_name = product_names[product_id - 1]
        product_category = product_categories[product_id - 1]
        product_price = round(random.uniform(product_prices[0], product_prices[1]), 2)
        insert_statements.append(f"INSERT INTO STORES.Products (name, category, price) VALUES ('{product_name}', '{product_category}', {product_price});")

    #Инвентар
    quantities = [10, 20, 30, 40, 50]
    for inventory_id in range(1, 6):
        product_id = inventory_id
        store_id = inventory_id
        quantity = random.choice(quantities)
        insert_statements.append(f"INSERT INTO STORES.Inventory (product_id, store_id, quantity) VALUES ({product_id}, {store_id}, {quantity});")

    #Продажби

    for sale_id in range(100,150 if business_climate == 'positive' else 20):
        quantity = random.randint(50, 100 if business_climate == 'positive' else 20)
        total_price = round(quantity * random.uniform(product_prices[0], product_prices[1]), 2)
        insert_statements.append(f"INSERT INTO STORES.Sales (product_id, store_id, quantity, total_price) VALUES ({sale_id}, {sale_id}, {quantity}, {total_price});")

    #Разходи
    expense_types = ['Rent', 'Utilities', 'Salaries', 'Maintenance', 'Supplies']
    amount = (1000, 2000)

    insert_statements.append("USE SCHEMA FINANCES;")
    for expense_id in range(1, 6):
        expense_type = random.choice(expense_types)
        expense_amount = round(random.uniform(amount[0], amount[1]), 2)
        expense_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        expense_date = expense_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO FINANCES.Expenses (expense_type, amount, expense_date) VALUES ('{expense_type}', {expense_amount}, '{expense_date}');")

    #Приходи
    income_types = ['Ticket Sales', 'Store Sales', 'Donations', 'Sponsorships', 'Grants']
    amount = (5000, 10000 if business_climate == 'positive' else 2000)
    for income_id in range(1, 6):
        income_type = random.choice(income_types)
        income_amount = round(random.uniform(amount[0], amount[1]), 2)
        income_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        income_date = income_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO FINANCES.Incomes (income_type, amount, income_date) VALUES ('{income_type}', {income_amount}, '{income_date}');")

    #Отдели
    department_names = ['Marketing', 'Finance', 'Maintenance', 'Security', 'HR']

    insert_statements.append("USE SCHEMA EMPLOYEES;")
    for department_id in range(1, 6):
        department_name = department_names[department_id - 1]
        manager_id = department_id
        insert_statements.append(f"INSERT INTO EMPLOYEES.Departments (name, manager_id) VALUES ('{department_name}', {manager_id});")

    #Позиции
    position_names = ['Manager', 'Supervisor', 'Employee', 'Security Guard', 'Janitor']
    base_salaries = [6000, 4000, 3000, 2000, 1000]
    for position_id in range(1, 6):
        position_name = position_names[position_id - 1]
        base_salary = base_salaries[position_id - 1]
        insert_statements.append(f"INSERT INTO EMPLOYEES.Positions (name, base_salary) VALUES ('{position_name}', {base_salary});")

    #Служители
    for employee_id in range(1, 6):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        department_id = random.randint(1, 5)
        position_id = random.randint(1, 5)
        manager_id = random.randint(1, 5)
        shift_id = employee_id
        insert_statements.append(f"INSERT INTO EMPLOYEES.Employees (first_name, last_name, department_id, position_id, manager_id) VALUES ('{first_name}', '{last_name}', {department_id}, {position_id}, {manager_id});")

    #Смени
    shift_names = ['Morning', 'Afternoon', 'Evening', 'Night', 'Overtime']
    shift_start_times = ['08:00:00', '12:00:00', '16:00:00', '20:00:00', '00:00:00']
    shift_end_times = ['12:00:00', '16:00:00', '20:00:00', '00:00:00', '04:00:00']
    for shift_id in range(1, 6):
        employee_id = shift_id
        shift_name = shift_names[shift_id - 1]
        shift_start_time = shift_start_times[shift_id - 1]
        shift_end_time = shift_end_times[shift_id - 1]
        insert_statements.append(f"INSERT INTO EMPLOYEES.Shifts (employee_id, name, start_time, end_time) VALUES ({employee_id}, '{shift_name}', '{shift_start_time}', '{shift_end_time}');")

    #Заплати
    payroll_amounts = [1000, 2000, 3000, 4000, 5000]
    payroll_bonuses = [100, 200, 300, 400, 500]
    for payroll_id in range(1, 6):
        employee_id = payroll_id
        amount = payroll_amounts[payroll_id - 1]
        bonus = payroll_bonuses[payroll_id - 1]
        payment_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        payment_date = payment_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO EMPLOYEES.Payroll (employee_id, amount, bonus, payment_date) VALUES ({employee_id}, {amount}, {bonus}, '{payment_date}');")

    #Събития
    event_names = ['Concert', 'Festival', 'Exhibition', 'Workshop', 'Conference']
    event_categories = ['Music', 'Art', 'Science', 'Education', 'Business']
    event_descriptions = ['Live music performances', 'Art installations', 'Scientific presentations', 'Educational activities', 'Business networking']

    insert_statements.append("USE SCHEMA EVENTS;")
    for event_id in range(1, 6):
        event_name = event_names[event_id - 1]
        event_category = event_categories[event_id - 1]
        event_description = event_descriptions[event_id - 1]
        start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        end_date = start_date + datetime.timedelta(days=random.randint(1, 5))
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        insert_statements.append(f"INSERT INTO EVENTS.Events (name, category, description, start_date, end_date) VALUES ('{event_name}', '{event_category}', '{event_description}', '{start_date}', '{end_date}');")

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

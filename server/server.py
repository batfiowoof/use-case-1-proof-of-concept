from flask import Flask, jsonify, request
import os
import snowflake.connector

from dotenv import load_dotenv
from controllers.attractions_controller import attractions_route_reg

app = Flask(__name__)

app.register_blueprint(attractions_route_reg)


# Snowflake connection

print('Snowflake connection established!')


# ROUTES AND CONNECTIONS



def fetch_data(query, params = None): # функция за изпълнение на SQL заявки, която връща резултата като списък от речници. params е параметър, който може да се подаде на заявката за да се избегне SQL injection
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )
    print('Connection established')
    cursor = conn.cursor() # създаваме курсор, с който да изпълняваме SQL заявките
    cursor.execute(query, params or {}) # изпълняваме заявката с подаден параметър
    rows = cursor.fetchall() # редовете от резултата
    cols = [col[0] for col in cursor.description] # имена на колоните от резултата
    cursor.close() # затваряме курсора
    conn.close() # затваряме връзката
    print('Connection closed')
    return [dict(zip(cols, row)) for row in rows] # връщаме резултата като списък от речници


@app.route('/sales', methods=['GET'])
def get_sales():
    data = fetch_data('SELECT * FROM STORES.Sales')
    return jsonify(data), 200

@app.route('/sales/<int:id>', methods=['GET'])
def get_sales_by_id(id):
    data = fetch_data('SELECT * FROM STORES.Sales WHERE sale_id = %s', (id,))
    return jsonify(data), 200

@app.route('/tickets', methods=['GET'])
def get_tickets():
    data = fetch_data('SELECT * FROM VISITORS.Tickets')
    return jsonify(data), 200

@app.route('/tickets', methods=['POST'])
def create_ticket():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        role=os.getenv('SNOWFLAKE_ROLE')
    )

    data = request.json # взимаме данните от заявката с библиотеката request в JSON формат

    if not data:
        return jsonify({'error': 'No data provided'}), 400 # ако няма данни, връщаме съобщение за грешка
    elif 'ticket_id' not in data or 'visitor_id' not in data or 'ticket_type' not in data or 'ticket_price' not in data:
        return jsonify({'error': 'Missing data'}), 400 # ако липсват някои от полетата, връщаме съобщение за грешка

    cursor = conn.cursor()
    cursor.execute('INSERT INTO VISITORS.Tickets (ticket_id, visitor_id, ticket_type, price) VALUES (%s, %s, %s, %s)', (data['ticket_id'], data['visitor_id'], data['ticket_type'], data['ticket_price'])) # изпълняваме заявката за попълване на нов билет

    conn.commit() # потвърждаваме промените
    cursor.close()
    conn.close()

    return jsonify({'message': 'Ticket created'}), 201 # връщаме съобщение за успешно създаден билет

@app.route('/tickets/<int:id>', methods=['GET'])
def get_tickey_by_id(id):
    data = fetch_data('SELECT FROM VISITORS.Tickets WHERE ticket_id = %s', (id,))
    if not data:
        return jsonify({'error': f'Ticket with id {id} not found'}), 404
    return jsonify(data), 200

@app.route('/events', methods=['GET'])
def get_events():
    data = fetch_data('SELECT * FROM EVENTS.Events')
    return jsonify(data), 200

@app.route('/events/<int:id>', methods=['GET'])
def get_event_by_id(id):
    data = fetch_data('SELECT * FROM EVENTS.Events WHERE event_id = %s', (id,))
    if not data:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify(data), 200

@app.route('/visitors', methods=['GET'])
def get_visitors():
    data = fetch_data('SELECT * FROM VISITORS.Visitors')
    return jsonify(data), 200

@app.route ('/visitors/<int:id>', methods=['GET'])
def get_visitor_by_id(id):
    data = fetch_data('SELECT * FROM VISITORS.Visitors WHERE visitor_id = %s', (id,))
    if not data:
        return jsonify({'error': f'Visitor with id {id} not found'}), 404
    return jsonify(data), 200

@app.route('/incomes' , methods=['GET'])
def get_incomes():
    data = fetch_data('SELECT * FROM FINANCES.Incomes')
    return jsonify(data), 200

@app.route('/incomes/<int:id>', methods=['GET'])
def get_income_by_id(id):
    data = fetch_data('SELECT * FROM FINANCES.Incomes WHERE income_id = %s', (id,))
    if not data:
        return jsonify({'error': f'Income with id {id} not found'}), 404
    return jsonify(data), 200

@app.route('/expenses', methods=['GET'])
def get_expenses():
    data = fetch_data('SELECT * FROM FINANCES.Expenses')
    return jsonify(data), 200

@app.route('/expenses/<int:id>', methods=['GET'])
def get_expense_by_id(id):
    data = fetch_data('SELECT * FROM FINANCES.Expenses WHERE expense_id = %s', (id,))
    if not data:
        return jsonify({'error': f'Expense with id {id} not found'}), 404
    return jsonify(data), 200

# ERROR HANDLING

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Address not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error, please try again later'}), 500

def bad_request(error):
    return jsonify({'error': 'Bad request :('}), 400


if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify

from controllers.attractions_controller import attractions_route_reg
from controllers.employees_controller import employees_route_reg
from controllers.sales_controller import sales_route_reg
from controllers.tickets_controller import tickets_route_reg
from controllers.events_controller import events_route_reg
from controllers.visitors_controller import visitors_route_reg
from controllers.incomes_controller import incomes_route_reg

app = Flask(__name__)

app.register_blueprint(attractions_route_reg)
app.register_blueprint(employees_route_reg)
app.register_blueprint(sales_route_reg)
app.register_blueprint(tickets_route_reg)
app.register_blueprint(events_route_reg)
app.register_blueprint(visitors_route_reg)
app.register_blueprint(incomes_route_reg)

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
    app.run(debug=True)
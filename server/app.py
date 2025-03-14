from flask import Flask

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



if __name__ == '__main__':
    app.run(debug=True)
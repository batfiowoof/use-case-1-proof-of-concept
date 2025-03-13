from flask import Blueprint, request

import db
employees_route_reg = Blueprint('employees', __name__)

@employees_route_reg.route('/employees', methods=['GET'])
def get_employees():
    return db.db_select("EMPLOYEES.Employees")

@employees_route_reg.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    return db.db_select("EMPLOYEES.Employees",'*', 'employee_id = %s' , (id, ))

@employees_route_reg.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    return db.db_update("EMPLOYEES.Employees", data, 'employee_id = %s', (id,))

@employees_route_reg.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    return db.db_insert("EMPLOYEES.Employees", data)

@employees_route_reg.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    return db.db_delete("EMPLOYEES.Employees", f'employee_id = %s', (id,))
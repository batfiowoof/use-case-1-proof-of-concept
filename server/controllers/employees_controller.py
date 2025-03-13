from flask import Blueprint, request
from server import db

employees_route_reg = Blueprint('employees', __name__)

@employees_route_reg.route('/employees', methods=['GET'])
def get_attraction():
    return db.db_select("EMPLOYEES.Employees") # SELECT * FROM ATTRACTIONS.Attractions

@employees_route_reg.route('/employees/<int:id>', methods=['GET'])
def get_attraction_by_id(id):
    return db.db_select("EMPLOYEES.Employees",'*', True , id) # SELECT * FROM ATTRACTIONS.Attractions WHERE attraction_id = id

@employees_route_reg.route('/employees/<int:id>', methods=['PUT'])
def update_attraction(id):
    data = request.json
    return db.db_update("EMPLOYEES.Employees", data, f'employee_id = {id}', id) # UPDATE ATTRACTIONS.Attractions SET key1 = %s, key2 = %s, ... WHERE attraction_id = id

@employees_route_reg.route('/employees', methods=['POST'])
def create_attraction():
    data = request.json
    return db.db_insert("EMPLOYEES.Employees", data) # INSERT INTO ATTRACTIONS.Attractions VALUES (%s, %s, %s, ...)

@employees_route_reg.route('/employees/<int:id>', methods=['DELETE'])
def delete_attraction(id):
    return db.db_delete("EMPLOYEES.Employees", f'employee_id = {id}', id) # DELETE FROM ATTRACTIONS.Attractions WHERE attraction_id = id
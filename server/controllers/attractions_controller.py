from flask import Blueprint, request
from server import db

attractions_route_reg = Blueprint('attractions', __name__)

@attractions_route_reg.route('/attractions', methods=['GET'])
def get_attraction():
    return db.db_select("ATTRACTIONS.Attractions") # SELECT * FROM ATTRACTIONS.Attractions

@attractions_route_reg.route('/attractions/<int:id>', methods=['GET'])
def get_attraction_by_id(id):
    return db.db_select("ATTRACTIONS.Attractions",'*', True , id) # SELECT * FROM ATTRACTIONS.Attractions WHERE attraction_id = id

@attractions_route_reg.route('/attractions/<int:id>', methods=['PUT'])
def update_attraction(id):
    data = request.json
    return db.db_update("ATTRACTIONS.Attractions", data, f'attraction_id = {id}', id) # UPDATE ATTRACTIONS.Attractions SET key1 = %s, key2 = %s, ... WHERE attraction_id = id

@attractions_route_reg.route('/attractions', methods=['POST'])
def create_attraction():
    data = request.json
    return db.db_insert("ATTRACTIONS.Attractions", data) # INSERT INTO ATTRACTIONS.Attractions VALUES (%s, %s, %s, ...)

@attractions_route_reg.route('/attractions/<int:id>', methods=['DELETE'])
def delete_attraction(id):
    return db.db_delete("ATTRACTIONS.Attractions", f'attraction_id = {id}', id) # DELETE FROM ATTRACTIONS.Attractions WHERE attraction_id = id
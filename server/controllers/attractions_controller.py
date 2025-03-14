from flask import Blueprint, request

import db

attractions_route_reg = Blueprint('attractions', __name__)

@attractions_route_reg.route('/attractions', methods=['GET'])
def get_attractions():
    order = request.args.get('order')
    return db.db_select("ATTRACTIONS.Attractions", order = order)

@attractions_route_reg.route('/attractions/<int:id>', methods=['GET'])
def get_attraction_by_id(id):
    return db.db_select("ATTRACTIONS.Attractions",'*', 'attraction_id = %s' , (id, ))

@attractions_route_reg.route('/attractions/<int:id>', methods=['PUT'])
def update_attraction(id):
    data = request.json
    return db.db_update("ATTRACTIONS.Attractions", data, 'attraction_id = %s', (id,))

@attractions_route_reg.route('/attractions', methods=['POST'])
def create_ticket():
    data = request.json
    return db.db_insert("ATTRACTIONS.Attractions", data)

@attractions_route_reg.route('/attractions/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    return db.db_delete("ATTRACTIONS.Attractions", f'attraction_id = %s', (id,))
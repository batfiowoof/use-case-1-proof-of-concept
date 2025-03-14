from flask import Blueprint, request

import db

visitors_route_reg = Blueprint('visitors', __name__)

@visitors_route_reg.route('/visitors', methods=['GET'])
def get_visitors():
    order = request.args.get('order')
    where = request.args.get('where')
    return db.db_select("VISITORS.Visitors", order = order, where = where)

@visitors_route_reg.route('/visitors/<int:id>', methods=['GET'])
def get_visitor_by_id(id):
    return db.db_select("VISITORS.Visitors",'*', 'visitor_id = %s' , (id, ))

@visitors_route_reg.route('/visitors/<int:id>', methods=['PUT'])
def update_visitor(id):
    data = request.json
    return db.db_update("VISITORS.Visitors", data, 'visitor_id = %s', (id,))

@visitors_route_reg.route('/visitors', methods=['POST'])
def create_visitor():
    data = request.json
    return db.db_insert("VISITORS.Visitors", data)

@visitors_route_reg.route('/visitors/<int:id>', methods=['DELETE'])
def delete_visitor(id):
    return db.db_delete("VISITORS.Visitors", f'visitor_id = %s', (id,))
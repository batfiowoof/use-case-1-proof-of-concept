from flask import Blueprint, request

import db

tickets_route_reg = Blueprint('tickets', __name__)

@tickets_route_reg.route('/tickets', methods=['GET'])
def get_tickets():
    return db.db_select("VISITORS.Tickets")

@tickets_route_reg.route('/tickets/<int:id>', methods=['GET'])
def get_ticket_by_id(id):
    return db.db_select("VISITORS.Tickets",'*', 'ticket_id = %s' , (id, ))

@tickets_route_reg.route('/tickets/<int:id>', methods=['PUT'])
def update_ticket(id):
    data = request.json
    return db.db_update("VISITORS.Tickets", data, 'ticket_id = %s', (id,))

@tickets_route_reg.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    return db.db_insert("VISITORS.Tickets", data)

@tickets_route_reg.route('/tickets/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    return db.db_delete("VISITORS.Tickets", f'ticket_id = %s', (id,))
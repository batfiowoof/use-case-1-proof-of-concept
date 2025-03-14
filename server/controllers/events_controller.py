from flask import Blueprint, request

import db

events_route_reg = Blueprint('events', __name__)

@events_route_reg.route('/events', methods=['GET'])
def get_events():
    order = request.args.get('order')
    return db.db_select("EVENTS.Events", order = order)

@events_route_reg.route('/events/<int:id>', methods=['GET'])
def get_event_by_id(id):
    return db.db_select("EVENTS.Events",'*', 'event_id = %s' , (id, ))

@events_route_reg.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.json
    return db.db_update("EVENTS.Events", data, 'event_id = %s', (id,))

@events_route_reg.route('/events', methods=['POST'])
def create_event():
    data = request.json
    return db.db_insert("EVENTS.Events", data)

@events_route_reg.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    return db.db_delete("EVENTS.Events", f'event_id = %s', (id,))
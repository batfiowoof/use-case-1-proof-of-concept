from flask import Blueprint, request

import db

incomes_route_reg = Blueprint('incomes', __name__)

@incomes_route_reg.route('/incomes', methods=['GET'])
def get_incomes():
    order = request.args.get('order')
    where = request.args.get('where')
    return db.db_select("VISITORS.Incomes", order = order, where = where)

@incomes_route_reg.route('/incomes/<int:id>', methods=['GET'])
def get_income_by_id(id):
    return db.db_select("VISITORS.Incomes",'*', 'income_id = %s' , (id, ))

@incomes_route_reg.route('/incomes/<int:id>', methods=['PUT'])
def update_income(id):
    data = request.json
    return db.db_update("VISITORS.Incomes", data, 'income_id = %s', (id,))

@incomes_route_reg.route('/incomes', methods=['POST'])
def create_income():
    data = request.json
    return db.db_insert("VISITORS.Incomes", data)

@incomes_route_reg.route('/incomes/<int:id>', methods=['DELETE'])
def delete_income(id):
    return db.db_delete("VISITORS.Incomes", f'income_id = %s', (id,))

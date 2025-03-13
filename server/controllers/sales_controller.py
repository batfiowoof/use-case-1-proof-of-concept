from flask import Blueprint, request
import db

sales_route_reg = Blueprint('sales', __name__)

@sales_route_reg.route('/sales', methods=['GET'])
def get_sales():
    return db.db_select("STORES.Sales") # SELECT * FROM STORES.Sales

@sales_route_reg.route('/sales/<int:id>', methods=['GET'])
def get_sale_by_id(id):
    return db.db_select("STORES.Sales",'*', 'sale_id = %s' , (id, )) # SELECT * FROM STORES.Sales WHERE sale_id = id

@sales_route_reg.route('/sales/<int:id>', methods=['PUT'])
def update_sale(id):
    data = request.json
    return db.db_update("STORES.Sales", data, f'sale_id = %s', (id, )) # UPDATE STORES.Sales SET key1 = %s, key2 = %s, ... WHERE sale_id = id

@sales_route_reg.route('/sales', methods=['POST'])
def create_sale():
    data = request.json
    return db.db_insert("STORES.Sales", data) # INSERT INTO STORES.Sales VALUES (%s, %s, %s, ...)

@sales_route_reg.route('/sales/<int:id>', methods=['DELETE'])
def delete_sale(id):
    return db.db_delete("STORES.Sales", f'sale_id = %s', (id, )) #
from flask import jsonify
import snowflake.connector

import os

def get_connection():
    return snowflake.connector.connect(user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA'),
    role=os.getenv('SNOWFLAKE_ROLE'))

def db_select(table, columns = '*', where = None, params = None):
    query = f'SELECT {columns} FROM {table}'
    if where:
        query += f' WHERE {where}'
    con = get_connection()
    cursor = con.cursor()
    try:
        cursor.execute(query, params or {})
        data = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    finally:
        cursor.close()
        con.close()
    return jsonify(data)

def db_insert(table, params = None):
    query_insert_col = ', '.join(params.keys()) # 'key1, key2, ...'
    query_data = tuple(params.values())
    query_count = len(query_data)
    print(params.values)

    query_insert_vals = ', '.join(['%s' for _ in range(query_count)]) # '%s, %s, ...'


    query = f'INSERT INTO {table} ({query_insert_col}) VALUES ({query_insert_vals})' # INSERT INTO table (key1, key2, ...) VALUES (%s, %s, ...)
    con = get_connection()
    cursor = con.cursor()
    try:
        cursor.execute(query, query_data)
        con.commit()
    finally:
        cursor.close()
        con.close()
    return jsonify("Created"), 201

def db_update(table, data, where, params = None):
    print(data)
    set_part = ', '.join([f'{key} = %s' for key in data.keys()]) # 'key1 = %s, key2 = %s, ...'
    val_part = tuple(data.values())
    print(val_part)
    query = f'UPDATE {table} SET {set_part} WHERE {where}' # UPDATE table SET key1 = %s, key2 = %s, ... WHERE ...

    con = get_connection()
    cursor = con.cursor()
    try:
        cursor.execute(query, val_part + params or {}) # data.values() + params
        con.commit()
    finally:
        cursor.close()
        con.close()
    return jsonify("Updated"), 200

def db_delete(table, where, params = None):
    query = f'DELETE FROM {table} WHERE {where}' # DELETE FROM table WHERE ...
    con = get_connection()
    cursor = con.cursor()
    try:
        cursor.execute(query, params or {})
        con.commit()
    finally:
        cursor.close()
        con.close()
    return jsonify("Deleted"), 200
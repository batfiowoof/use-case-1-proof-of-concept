from flask import Flask, jsonify, request
import os
import snowflake.connector
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


# Snowflake connection
conn = snowflake.connector.connect(
    user = os.getenv('SNOWFLAKE_USER'),
    password = os.getenv('SNOWFLAKE_PASSWORD'),
    account = os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse = os.getenv('SNOWFLAKE_WAREHOUSE'),
    database = os.getenv('SNOWFLAKE_DATABASE'),
    schema = os.getenv('SNOWFLAKE_SCHEMA'),
    role = os.getenv('SNOWFLAKE_ROLE')
)

def get_connection():
    return conn



if __name__ == '__main__':
    app.run(debug=True)
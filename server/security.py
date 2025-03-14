from flask import request, jsonify

# Dummy API key
dummy_keys = {
    'dummy-api-key-123': 'User 1',
    'dummy-api-key-456': 'User 2',
}

def authenticate_api_key(api_key):
    return dummy_keys.get(api_key) is not None

# Middleware to check if the API key is valid

def before_request():
    api_key = request.headers.get('api-key')
    if not api_key or not authenticate_api_key(api_key):
        return jsonify({'error': 'Invalid key, access denied'}), 401
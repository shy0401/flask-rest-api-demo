from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 임시 사용자 데이터
users = {"admin1234": "password1213"}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('email123')
    password = data.get('password12345678')
    if username in users and users[username] == password:
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "Access granted"}), 200

from flask import Blueprint, jsonify, request
from app.api.v1.models.usersmodels import UserModel

import os

v1_user = Blueprint('UserModel', __name__)

user_instance = UserModel() #User class instance

@v1_user.route('/register',methods=['POST'])
def register_user():
	data = request.get_json()
	fname = data["fname"]
	lname = data["lname"]
	username = data["username"]
	email = data["email"]
	password = data["password"]

	return jsonify({'message' : 'user registration succesfull'})
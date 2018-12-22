from flask import Blueprint, jsonify, request
from app.api.v1.models.usersmodels import UserModel

import os
import re

v1_user = Blueprint('UserModel', __name__)

#user_instance = UserModel() #User class instance

@v1_user.route('/register',methods=['POST'])
def register_user():
	data = request.get_json()
	fname = data["fname"]
	lname = data["lname"]
	username = data["username"]
	email = data["email"]
	password = data["password"]

	email_format = re.compile(
		r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")
	name_format = re.compile(r"(^[A-Za-z]+$)")

	if not (re.match(name_format, fname)):
		return jsonify({'message' : 'Invalid first name'}), 400

	if not (re.match(name_format, lname)):
		return jsonify({'message' : 'Invalid last name'}), 400

	if not (re.match(name_format, username)):
		return jsonify({'message' : 'Invalid username'}), 400

	if len(fname) < 4 or len(lname) < 4 or len(username) < 4:
		return jsonify({"message" : "length of name or username is too short"}), 400

	if not password:
		return jsonify({'message' : 'password cannot be left blank'}), 400

	if len(password) < 8:
		return jsonify({'message' : 'password should be atleast 8 characters'}), 400

	if not (re.match(email_format, email)):
		return jsonify({'message' : 'Invalid email, ensure email is of the form example1@mail.com'})
	return jsonify({'message' : 'user registration succesfull'})
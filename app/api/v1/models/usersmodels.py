class UserModel(object):
	def __init__(self):
		self.users = {}

	def sign_up(self, fname, lname, username, email, password):
		user_id = str(len(self,users) + 1)
		reg_user = {
			"id" : user_id
			"fname" : fname
			"lname" : lname
			"username" : username
			"email" : email
			"password" : password
		}

		self.username[username] = reg_user
		return self.users
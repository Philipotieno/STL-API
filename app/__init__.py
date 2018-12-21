from flask import Flask

from config import app_config


def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])
	app.register_blueprint(v1_user, url_prefix="/signup")


	return app
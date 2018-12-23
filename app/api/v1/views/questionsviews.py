from flask import request, jsonify, Blueprint
from app.api.v1.models.questionsmodel import Questions


v1_questions = Blueprint('questions', __name__)

questions = Questions()

@v1_questions.route('', methods=['POST'])
def ask_question(current_user):
	data = request.get_json()
	qns = data["qns"]
	total = questions.total(qns)
	questions.ask_question(
			user = current_user,
			qns=qns,
			total=total
		)
	return jsonify({'Message' : 'You have succesfully posted your question'})
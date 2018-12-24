from flask import request, jsonify, Blueprint
from app.api.v1.models.questionsmodels import Questions


v1_questions = Blueprint('questions', __name__)

questions = Questions()

@v1_questions.route('', methods=['POST'])
def ask_question():
	data = request.get_json()
	title = data['title']
	content = data['content']

	questions.ask_question(
			title=title,
			content=content
		)

	if not title or not content:
		return jsonify({'message': 'Please input all required fields!'}), 400
	return jsonify({'Message' : 'You have succesfully posted your question'}), 201

@v1_questions.route('', methods=['GET'])
def get_questions():
	all_qns = questions.get_all_questions()
	if not all_qns:
		return jsonify({'message' : 'no questions posted'}), 404

	return jsonify({"Questions" : all_qns}), 200

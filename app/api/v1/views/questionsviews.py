from flask import request, jsonify, Blueprint
from app.api.v1.models.questionsmodels import Questions


v1_questions = Blueprint('questions', __name__)

questions = Questions()

@v1_questions.route('', methods=['POST'])
def ask_question():
	data = request.get_json()
	title = data['title']
	content = data['content']

	if not title or not content:
		return jsonify({'message': 'Please input all required fields!'}), 400
	return jsonify({'Message' : 'You have succesfully posted your question'})
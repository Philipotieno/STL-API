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

@v1_questions.route('<question_id>', methods=['GET'])
def get_specific_questions(question_id):
	a_qns = questions.get_specific_question(question_id)
	if not a_qns:
		return jsonify({'message' : 'no such question posted'}), 404

	return jsonify({"Questions" : a_qns}), 200

@v1_questions.route('<question_id>', methods=['PUT'])
def answer_qns(question_id):
	data = request.get_json()

	all_qns = questions.get_all_questions()
	if not all_qns:
		return jsonify({'message' : 'questions not found'}), 404

	new_answer = data['answer']
	questions.answer_qn(question_id, new_answer)
	return jsonify({'message' : 'you have posted an answer'})


@v1_questions.route('<question_id>', methods=['POST'])
def accept_ans(question_id):
	data = request.get_json()

	all_qns = questions.get_all_questions()
	if not all_qns:
		return jsonify({'message' : 'questions not found'}), 404

	new_status = data['answer_status']
	questions.accept_ans(question_id, new_status)
	return jsonify({'message' : 'your response has been recorded'})
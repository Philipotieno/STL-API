class Questions():
	def __init__(self):
		self.questions = {}

	def ask_question(self, title, content):
		question_id = str(len(self.questions) + 1)
		new_question = {
			"id" : question_id,
				"title" : title,
				"content" : content,
				"answer" : "no answer",
				"answer_status" : "pending"
		}

		self.questions[question_id] = new_question
		return self.questions

	def get_all_questions(self):
		'''Method to fetch all questions'''
		if self.questions:
			return self.questions

	def get_specific_question(self, question_id):
		""" Fetch a specific order using given id"""
		if self.questions:
			for qns in self.questions.values():
				if qns["id"] == question_id:
					return qns
	def answer_qn(self, question_id, answer):
		""" Method to answer a specific question"""
		answered_qns = self.get_specific_question(question_id)
		if answered_qns:
			answered_qns["answer"] = answer
			return answered_qns

	def accept_ans(self, question_id, answer_status):
		""" Method to acdept an answer a specific question"""
		answered_qns = self.get_specific_question(question_id)
		if answered_qns:
			answered_qns["answer_status"] = answer_status
			return answered_qns
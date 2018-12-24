class Questions():
	def __init__(self):
		self.questions = {}

	def ask_question(self, title, content):
		question_id = str(len(self.questions) + 1)
		new_question = {
			"id" : question_id,
				"title" : title,
				"content" : content
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
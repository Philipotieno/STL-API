class Questions():
	def __init__(self):
		self.questions = {}

	def ask_question(self, user, qns={"Question" : 0}, total=0):
		quetion_id = str(len(self.questions) + 1)
		new_question = {
			"id" : question_id,
				"title" : title,
				"content" : content
		}

		self.questions[question_id] = new_question
		return self.questions
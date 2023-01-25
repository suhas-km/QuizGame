import data
from quiz_brain import QuizBrain
import os

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for question in data.question_data:
    new_q = Question(question["text"], question["answer"])
    # print(f"text:{new_q.text}, answer:{new_q.answer}")
    question_bank.append(new_q)

# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

os.system("clear")
print("You've completed the quiz")
print(f"Your final score was: {quiz.percentage()}")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = Question(item["text"], item["answer"])
    question_bank.append(q)

question = QuizBrain(question_bank)



for i in range (0,len(question_bank)):
    question.next_question()

print(f"your score is: {question.score} out of {len(question_bank)}")
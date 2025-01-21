from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
quiz = QuizBrain(question_bank)
for i in question_data:
    a = i['text']
    b = i['answer']
    q1 = Question(question=a, answer=b)
    question_bank.append(q1)

"""#we have now all the object in the bank
print(question_bank)
#and we can call them
print(question_bank[0].question)"""

while quiz.still_has_questions(question_bank):
    quiz.next_question()

print('Nice try!!')
print(f'Your final score was {quiz.score}/{len(question_bank)}')
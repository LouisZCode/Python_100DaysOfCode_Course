class QuizBrain:

    #these are GLOBAL to this Class!! interesting
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    #and these are local..! to each Method, so we need parameters to be passed around!
    def still_has_questions(self,q_list):
        while self.question_number != len(q_list):
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {current_question.question}, True or False?')
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, real_answer):
        if user_answer.lower() == real_answer.lower():
            self.score += 1
            print(f'Correct!')
        else:
            print(f'InCorrect! Mens@')

        print(f'your score = {self.score}/{self.question_number}')
        print('')


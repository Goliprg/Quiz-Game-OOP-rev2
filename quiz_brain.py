class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # def still_has_questions(self):
    #     if self.question_number < len(self.question_list):
    #         return 1
    #     else:
    #         return 0

    def next_question(self):
        user_answer = input(f"Q{self.question_number+1}: {self.question_list[self.question_number].text} True or False?")

        if user_answer == self.question_list[self.question_number].answer:
            print("you are right!")
            self.score += 1
        else:
            print("you are wrong!")
        self.question_number += 1
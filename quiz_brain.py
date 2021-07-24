class QuizBrain:

    def __init__(self, questions_list):
        self.list = questions_list
        self.questions_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.questions_number < len(self.list)

    def next_question(self):
        current_question = self.list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Not correct!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Current score is {self.score}/{self.questions_number}.\n")

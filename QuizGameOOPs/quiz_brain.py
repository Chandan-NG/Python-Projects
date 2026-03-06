class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0


    def still_has_question(self):
        return self.q_number < len(self.q_list)


    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/ False): ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer.title():
            print("Correct Answer...!")
            self.score += 1
        else:
            print("Wrong Answer...!")
        print(f"The Correct Answer was: {correct_answer}")
        print(f"Your Current Score is: {self.score}/{self.q_number}")
        print(3 * "\n")
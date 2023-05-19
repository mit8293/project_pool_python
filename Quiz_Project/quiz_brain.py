
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(
            f"Q.{self.question_number}: {current_question.text}(True/False): ").lower()
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            self.score += 1
            print("You are Right")
        else:
            print("You got it wrong.")
        print(f"Your current score is {self.score}/{self.question_number}")

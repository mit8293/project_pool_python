from quiz_brain import QuizBrain
from data import question_data, add_question, quiz_master
from question_model import Question
import os
def clear(): return os.system('cls')


master = True
while master == True:
    print("Welcome to Quiz gaming challnge")
    print("Select your role: ")
    print(" Quiz Master (press 1)")
    print(" Quiz Cracker (press 2)")
    print(" Stop (press 3)")

    select = input("Enter your role: ")
    if select == "1":
        print("Quiz master")
        quiz_master()
        clear()
    if select == "2":
        question_bank = []

        for i in range(len(question_data)):
            q = Question(question_data[i]["text"], question_data[i]["answer"])
            question_bank.append(q)

        quiz = QuizBrain(question_bank)

        while quiz.still_has_questions():
            quiz.next_question()

        print("You have completed the quiz.")
        print(f"Your final score is : {quiz.score}/{quiz.question_number}")
    if select == '3':
        master = False

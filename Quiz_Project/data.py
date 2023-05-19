
def add_question():
    question_input = input(
        "Please enter your question (True or False questions): ")
    answer_input = input("Please input answer : ")
    add_question_dict = {"text": question_input, "answer": answer_input}
    question_data.insert(0, add_question_dict)


def quiz_master():
    master = True
    while master == True:
        print("Welcome Master")
        print("Shake your brains and add some challanging questions..")
        print("MENU")
        print("Press 1 for Add questions:")
        print("Press 2 for View questions:")
        print("Press 3 for Delete questions:")
        print("Press 4 for Exit")
        select = input("Which operation you want to perform: ")
        if select == "1":
            add_question()
        elif select == "2":
            for question in question_data:
                print(
                    f"Question {question_data.index(question)+1} {question['text']} Answer : {question['answer']}")
        elif select == "3":
            del_question = int(input(
                "You want to delete which question? enter number only : "))
            del question_data[del_question-1]
            print("Now the list is :")
            for question in question_data:
                print(
                    f"Question {question_data.index(question)+1} {question['text']} Answer : {question['answer']}")
        elif select == "4":
            master = False


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
                "you are free to take it home to eat.",
        "answer": "True"},
    # {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
    #  "answer": "False"},
    # {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    # {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    # {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    # {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    # {"text": "No piece of square dry paper can be folded in half more than 7 times.",
    #     "answer": "False"},
    # {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


# Get API json from this address. change in data for different questions.
# https://opentdb.com/

total_score = 0
incorrect_questions = []
def question_one():
    question = "Make School is located in San Francisco, true or false? Enter a 0 for false and a 1 for true: "
    response = input(question)
    correct_answer = "1"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        incorrect_questions.append(question)
        return 0


def question_two():
    question = "How many concentrations are there at Make School? Enter answer in form of integer: "
    response = input(question)
    correct_answer = "4"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        incorrect_questions.append(question)
        return 0

def question_three():
    question = "Make School is a business school, true or false? Enter a 0 for false and a 1 for true: "
    response = input(question)
    correct_answer = "0"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        incorrect_questions.append(question)
        return 0

def question_four():
    question = "Which of the following is NOT a concentration at Make School? Please enter a letter. \n a) Data Science \n b) Front End Web \n c) 3D Animation \n d) Mobile \n e) Back End Web \n"
    response = input(lower(question))
    correct_answer = "c"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        incorrect_questions.append(question)
        return 0

def info():
    print(f"Your final score is {total_score}/5, here are the questions you missed:")
    for incorrect in incorrect_questions:
        print(incorrect)

#Code to run the quiz
points = question_one()
total_score += points
points = question_two()
total_score += points
points = question_three()
total_score += points
points = question_four()
total_score += points

info()

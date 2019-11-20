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

#Code to run the quiz
points = question_one()
total_score += points
question_two()
total_score += points

print(total_score)
print(incorrect_questions)

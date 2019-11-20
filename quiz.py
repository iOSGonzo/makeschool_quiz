total_score = 0

def question_one():
    response = input("Make School is located in San Francisco, true or false? Enter a 0 for false and a 1 for true: ")
    correct_answer = "1"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        return 0


def question_two():
    response = input("How many concentrations are there at Make School? Enter answer in form of integer: ")
    correct_answer = "4"
    if response == correct_answer:
        print("Correct!")
        return 1
    elif response != correct_answer:
        print("Sorry, wrong answer!")
        return 0

#Code to run the quiz
points = question_one()
total_score += points
question_two()
total_score += points

print(total_score)

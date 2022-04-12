from random import randint
from random import choice
DESCRIPTION = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 50


def round():
    ramdom_number1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    ramdom_number2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    opetator_set = "+-*"
    random_operator = choice(opetator_set)
    if random_operator == "+":
        right_answer = str(ramdom_number1 + ramdom_number2)
    elif random_operator == "-":
        right_answer = str(ramdom_number1 - ramdom_number2)
    else:
        right_answer = str(ramdom_number1 * ramdom_number2)
    question = f"{ramdom_number1} {random_operator} {ramdom_number2}"
    return question, right_answer

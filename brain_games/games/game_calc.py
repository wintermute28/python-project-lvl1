from random import randint
from random import choice
description = 'What is the result of the expression?'


def round():
    opetator_set = "+-*"
    random_number1 = randint(1, 50)
    random_number2 = randint(1, 50)
    random_operator = choice(opetator_set)
    if random_operator == "+":
        question = f"{random_number1} + {random_number2}"
        right_answer = str(random_number1 + random_number2)
    elif random_operator == "-":
        question = f"{random_number1} - {random_number2}"
        right_answer = str(random_number1 - random_number2)
    else:
        question = f"{random_number1} * {random_number2}"
        right_answer = str(random_number1 * random_number2)
    return question, right_answer


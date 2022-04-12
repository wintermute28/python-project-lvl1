from random import randint
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def round():
    random_number = randint(1, 100)
    question = random_number
    if random_number % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer

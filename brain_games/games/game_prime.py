import random
description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    random_number = random.randint(1, 100)
    question = random_number
    if random_number in range(2, 4):
        right_answer = "yes"
    elif random_number == 1:
        right_answer = "no"
    else:
        for elenent in range(2, random_number - 1):
            if random_number % elenent != 0:
                right_answer = "yes"
            else:
                right_answer = "no"
                break
    return question, right_answer

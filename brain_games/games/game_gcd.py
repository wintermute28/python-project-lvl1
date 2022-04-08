import random
description = "Find the greatest common divisor of given numbers."


def round():
    random_number1 = random.randint(1, 50)
    random_number2 = random.randint(1, 50)
    question = f"{random_number1} {random_number2}"
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
    right_answer = str(random_number1 + random_number2)
    return question, right_answer


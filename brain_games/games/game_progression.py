import random
description = "What number is missing in the progression?"


def round():
    random_len = random.randint(5, 10)
    hidden_element = random.randint(0, random_len)
    random_number = random.randint(1, 50)
    random_delta = random.randint(2, 10)
    progression = [random_number]
    i = 0
    while i < random_len:
        random_number += random_delta
        progression.append(random_number)
        i += 1
    right_answer = str(progression[hidden_element])
    progression[hidden_element] = ".."
    question = ' '.join(map(str, progression))
    return question, right_answer

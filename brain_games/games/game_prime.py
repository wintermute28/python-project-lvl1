import random
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    divider = 2
    if random_number == 1:
        return False
    else:
        while divider <= random_number / 2:
            if random_number % divider == 0:
                return False
                break
            else:
                divider += 1
        return True


def round():
    random_number = random.randint(1, 100)
    question = random_number
    if is_prime(random_number) is True:
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer

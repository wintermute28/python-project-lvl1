#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    win_end = 2
    while win <= win_end:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            right_answer = "yes"
        else:
            right_answer = "no"
        print("Question: " + str(random_number))
        user_answer = prompt.string("Your answer: ")
        if user_answer != right_answer:
            print("'" + user_answer + "'" + " is wrong answer ;(. Correct\
 answer was " + "'" + right_answer + "'" + ".\nLet's try\
 again, " + name + "!")
            break
        elif user_answer == right_answer:
            win += 1
            print("Correct!")
    if win == 3:
        return print("Congratulations, " + name + "!")
    else:
        pass


if __name__ == '__main__':
    main()

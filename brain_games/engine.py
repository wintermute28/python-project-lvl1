import prompt
win_score = 2


def launch_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print(game.description)
    user_score = 0

    while user_score <= win_score:
        question, right_answer = game.round()
        print("Question: {}".format(question))
        user_answer = str(prompt.string("Your answer: "))
        if user_answer == right_answer:
            user_score += 1
            print("Correct!")
        else:
            print("'" + str(user_answer) + "'" + " is wrong answer ;(. Correct\
 answer was " + "'" + str(right_answer) + "'" + ".\nLet's try\
 again, " + name + "!")
            break
    return print("Congratulations, " + name + "!")

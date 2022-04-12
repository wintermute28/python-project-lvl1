import prompt
WIN_SCORE = 2


def launch_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print(game.DESCRIPTION)
    user_score = 0

    while user_score <= WIN_SCORE:
        question, right_answer = game.round()
        print("Question: {}".format(question))
        user_answer = str(prompt.string("Your answer: "))
        if user_answer == right_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was \
'{}'.".format(user_answer, right_answer))
            print("Let's try again, {}!".format(name))
            break
        user_score += 1
    if user_score == 3:
        return print("Congratulations, " + name + "!")

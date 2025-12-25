import prompt
from brain_games import cli

ROUNDS_COUNT = 3


def play(game):
    name = cli.welcome_user()

    print(game.DESCRIPTION)

    for num in range(ROUNDS_COUNT):
        question, good_ans = game.generate_round()

        print("Question:", question)
        ans = prompt.string("Your answer: ")

        if ans != good_ans:
            print(
                f"{ans} is wrong answer ;(. Correct answer was {good_ans}.",
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
    print(f"Congratulations, {name}!")

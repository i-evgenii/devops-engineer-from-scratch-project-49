import prompt

ROUNDS_COUNT = 3


def play(game):
    print("Welcome to the Brain Games!")
    print(game.DESCRIPTION)

    name = prompt.string("May I have your name? ")

    print(f"Hello, {name}")

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

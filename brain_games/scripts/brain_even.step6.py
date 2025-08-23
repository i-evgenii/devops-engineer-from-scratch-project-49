import prompt
from random import randint

ROUNDS_COUNT = 3
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def make_num():
    question = randint(1, 100)
    good_ans = "yes" if is_even(question) else "no"
    return str(question), good_ans


def main():
    print("Welcome to the Brain Games!")
    print(DESCRIPTION)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    count = ROUNDS_COUNT
    while count:
        question, good_ans = make_num()

        print("Question:", question)
        ans = prompt.string("Your answer: ")

        if ans != good_ans:
            print(
                f"{ans} is wrong answer ;(. Correct answer was {good_ans}.",
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        count -= 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

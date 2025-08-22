import prompt
from random import randint

ROUNDS_COUNT = 3
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

def make_num():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), correct_answer


def main():
    print('Welcome to the Brain Games!')
    print(DESCRIPTION)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    count = ROUNDS_COUNT
    while count:
        question, correct_answer = make_num()

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(
                f'{answer} is wrong answer ;(. '
                f'Correct answer was {correct_answer}.',
            )
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        count -= 1

    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
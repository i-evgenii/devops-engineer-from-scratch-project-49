import prompt

ROUNDS_COUNT = 3

def play(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}')

    count = ROUNDS_COUNT
    while count:
        question, correct_answer = game.generate_round()

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

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = randint(1, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return str(question), correct_answer

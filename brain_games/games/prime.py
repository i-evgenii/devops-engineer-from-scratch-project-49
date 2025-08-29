from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number // 2):
        if not number % divisor:
            return False
    return True


def generate_round():
    question = randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return str(question), correct_answer

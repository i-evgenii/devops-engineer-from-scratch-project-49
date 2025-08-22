from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MINIMAL_NUMBER = 10
MAXIMAL_NUMBER = 100

def gcd(number_a, number_b):

    remainder = number_a % number_b
    if not remainder:
        return number_b
    return gcd(number_b, remainder)


def generate_round():
    
    number_a = randint(MINIMAL_NUMBER, MAXIMAL_NUMBER)
    number_b = randint(MINIMAL_NUMBER, MAXIMAL_NUMBER)

    question = f'{number_a} {number_b}'
    correct_answer = gcd(number_a, number_b)

    return question, str(correct_answer)

import random

print('Answer "yes" if the number is even, otherwise answer "no".')


def random_even(num):
    if num % 2 == 0:
        question = 'yes'
    else:
        question = 'no'
    return question


game = True
counter = 0

while game:
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = input()
    if answer == random_even(number):
        print('Correct!')
        counter += 1
    elif counter == 3:
        print(f'Congratulations, {name}')
        game = False
    else:
        print(f'{answer} is a wrong answer ;(. Correct answer was "{random_even(number)}".')
        print(f"Let's try again, {name}!")
        game = False

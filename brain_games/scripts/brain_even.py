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

while game or counter != 3:
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = input()

    if answer == random_even(number):
        print('Correct!')
        counter += 1
    else:
        print(f'{answer} is a wrong answer ;(. Correct answer was "{random_even(number)}".')
        print(f"Let's try again!")
        game = False

    if counter == 3:
        game = False
        print(f'Congratulations!')

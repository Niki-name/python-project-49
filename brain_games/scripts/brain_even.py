#!/usr/bin/env python3
from brain_games.hello_name import welcome
import random


def main():

    name = welcome()
    round = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while round != 3:
        number = random.randint(0, 4)
        print(f"Question: {number}")
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == "yes":
            print("Correct")

        elif number % 2 != 0 and answer == "no":
            print("Correct")

        else:
            print(f"Let's try again, {name}")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()

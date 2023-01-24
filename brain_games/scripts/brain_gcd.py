#!/usr/bin/env python3
from brain_games.hello_name import welcome
import math
import random


def main():
    name = welcome()
    round = 0
    print('Find the greatest common divisor of given numbers.')
    while round != 3:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        Question = math.gcd(number_1, number_2)
        print(f"Question: {number_1}, {number_2}")
        answer = int(input('Your answer: '))
        if answer == Question:
            print("Correct")
        else:
            print(f"'{answer}' is wrong ;(. Correct answer was '{Question}'")
            print(f"Let's try again, {name}")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()

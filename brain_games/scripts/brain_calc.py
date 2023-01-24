#!/usr/bin/env python3
from brain_games.hello_name import welcome
import random


def main():
    name = welcome()
    round = 0
    value = 0
    print('What is the result of the expression?')
    while round != 3:
        number_1 = random.randint(0, 5)
        number_2 = random.randint(0, 5)
        math_operation = random.choice(['+', '*', '-'])
        Question = str(number_1) + ' ' + math_operation + ' ' + str(number_2)
        if math_operation == "+":
            value = number_1 + number_2
        elif math_operation == "-":
            value = number_1 - number_2
        elif math_operation == "*":
            value = number_1 * number_2
        print(f"Question: {Question}")
        answer = int(input('Your answer: '))
        if answer == value:
            print("Correct")
        else:
            print(f"'{answer}' is wrong ;(. Correct answer was '{value}'")
            print(f"Let's try again, {name}!")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()

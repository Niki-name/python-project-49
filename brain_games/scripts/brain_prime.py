#! /usr/bin/env python3
from brain_games.hello_name import welcome
import random


def main():
    name = welcome()
    round = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while round != 3:
        number = random.randint(3,100)
        divider = []  # для цикла
        print(f"Question: {number}")
        for i in range(3,number):       # Перебор делителей
            if (number % i) == 0:           # Если делиться хоть 1 делитель на 0, список пуст(число сложное)
                break
        else:
            divider.append(number)           # иначе список заполнится (число простое)
        if divider == []:
            True_answer = 'no'
        else:
            True_answer = 'yes'
        answer = input('Your answer: ')
        if answer == True_answer:
            print('Corret!')
        else:
            print(f"Let's try again {name}")
            break
        round += 1
        if round == 3:
            print(f"Congratulations,{name}! ")


if __name__ == '__main__':
    main()

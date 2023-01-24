#! /usr/bin/env python3
import random
from brain_games.hello_name import welcome


def main():
    name = welcome()
    round = 0
    print('What number is missing in the progression?')
    while round != 3:
        start = random.randint(0, 40)
        end = random.randint(60, 100)
        step = random.randint(2, 4)
        progression = list(range(start, end, step))
        Question = progression[:10]         # ибо прогрессия может быть большой)
        element = random.choice(Question)      # рандомный элемент
        if element in Question:
            for index, value in enumerate(Question):
                if value == element:
                    Question[index] = '..'   # замена рандомного элемента на ..
        print(f"Question: {Question}")              # Вопрос
        answer = int(input('Your answer: '))
        if answer == element:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong ;(. Correct answer was '{element}'")
            print(f"Let's try again, {name}")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()

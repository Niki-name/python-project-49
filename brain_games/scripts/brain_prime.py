#! /usr/bin/env python3
from brain_games.hello_name import welcome
from brain_games.engine_game import game_prime


def main():
    name = welcome()
    round = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while round != 3:
        answer, True_answer = game_prime()
        if answer == True_answer:
            print('Corret!')
        else:
            print(f"Let's try again, {name}!")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()

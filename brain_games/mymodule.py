import random


def game_even():
    winner = ''
    round = 0
    while round != 3:
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == "yes":
            print("Correct")
        elif number % 2 != 0 and answer == "no":
            print("Correct")
        else:
            break
        round += 1
        if round == 3:
            return winner

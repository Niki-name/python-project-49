import random


def game_progression():
    start = random.randint(0, 40)
    end = random.randint(60, 100)
    step = random.randint(2, 4)
    progression = list(range(start, end, step))
    Question = progression[:10]         # ибо прогрессия может быть большой)
    element = random.choice(Question)      # рандомный элемент
    if element in Question:
        for index, value in enumerate(Question):
            if value == element:
                Question[index] = '..'      # замена рандомной цифры на ..
    for_print = " ".join(map(str, Question))
    print(f"Question: {for_print}")              # Вопрос
    answer = int(input('Your answer: '))
    return answer, element


def game_prime():
    number = random.randint(3, 100)
    divider = []  # для цикла
    print(f"Question: {number}")
    for i in range(2, number):  # Перебор делителей
        if (number % i) == 0:   # (число сложное)
            break
    else:
        divider.append(number)  # (число простое)
    if divider == []:
        True_answer = 'no'
    else:
        True_answer = 'yes'
    answer = input('Your answer: ')
    return answer, True_answer


def first_game():

    from brain_games.hello_name import welcome

    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    from brain_games.mymodule import game_even

    if game_even() == '':
        print(f"Congratulations, {name}! ")
    else:
        print(f"Let's try again, {name}!")

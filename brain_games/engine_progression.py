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

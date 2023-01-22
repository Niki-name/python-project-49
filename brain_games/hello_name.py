import prompt


def welcome():
    print('brain-games \nWelcome to the Brain Games !')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name} !')
    return name

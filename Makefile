#Устанавливает зависимости
install: 
	poetry install

#запуск приветствия
brain-games:
	poetry run brain-games

#Сборка пакета
build:
	poetry build

#Отладка пакета
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

#Проверка на ошибки
lint:
	poetry run flake8 brain_games

# Запуск игры на чётность
even:
	poetry run brain-even

#Запуск игры калькулятор
calc:
	poetry run brain-calc
#Запуск игры НОД
gcd:
	poetry run brain-gcd

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

#Установка игры
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

#Запуск игры на прогрессию
progression:
	poetry run brain-progression

#Запуск игры на простое число
prime:
	poetry run brain-prime

#Переустановка игры(при обновлении)
reinstall:
	python3 -m pip install --force-reinstall --user dist/hexlet_code-0.1.0-py3-none-any.whl

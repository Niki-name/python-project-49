#Устанавливает зависимости
install: 
	poetry install

#запуск игры
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

install:
	poetry install

brain-games bg:
	poetry run brain-games

build:
	poetry build

lint:
	poetry run flake8 brain_games

publish:
	poetry publish --dry-run

package-install pi:
	python3 -m pip install --user dist/*.whl
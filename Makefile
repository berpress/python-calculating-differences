install:
	@poetry install

lint:
	@poetry run flake8 gendiff tests


pytest:
	@poetry run pytest

build:
	@poetry build

publish:
	@poetry publish -r pypi_test
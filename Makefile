install:
		pip install -r requirements.txt
format:

	black $(shell git ls-files -o --exclude-standard)

test:
	python -m pytest -vv  test/test.py
run:
	python utility.py

lint:
	pylint $(shell find . -name "*.py")

all: install format lint
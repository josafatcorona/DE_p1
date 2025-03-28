install:
		pip install -r requirements.txt
format:
	black *.py

test:
	pytest 
run:
	python utility.py

lint:
	pylint $(shell find . -name "*.py")

all: install format lint
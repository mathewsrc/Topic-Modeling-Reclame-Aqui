setup:
	python3 -m venv ~/.env

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --vv test_app.py

format:
	black *.py

lint:
	pylint --disable=R,C codigoquebrado.py


all: install lint test 

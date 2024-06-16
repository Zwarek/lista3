.PHONY: install test run

install:
	pip install -r requirements.txt

test:
	python test_app.py

run:
	python app.py

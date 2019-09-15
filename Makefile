init: 
	pip install -r requirements.txt

test:
	python -m unittest sample_test.py

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

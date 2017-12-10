build:
	docker build --no-cache -t liftos:1.0 .

run:
	./venv/bin/python3.5 liftOS/__init__.py

test:
	./venv/bin/python3.5 -m unittest discover


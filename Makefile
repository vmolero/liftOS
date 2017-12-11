python=./venv/bin/python3.5

build:
	$(python) setup.py build

server:
	$(python) -m liftOS 

client:
	$(python) -m liftOS/client.py ${ARGS} 

test:
	$(python) -m unittest discover


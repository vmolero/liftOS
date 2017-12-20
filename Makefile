python="./venv/bin/python3"

build:
	$(python) setup.py build

server:
	$(python) -m LiftOS

client:
	$(python) -m LiftClient ${ARGS}

test:
	$(python) -m unittest discover

clean: 
	rm -rf build dist liftOS.egg-info __pycache__


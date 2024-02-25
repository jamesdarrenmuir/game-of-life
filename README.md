# Conway's Game of Life

## Installation

1. Clone the repository

2. Set up a Python virtual environment
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. Install the dependencies
	```bash
	pip install -r requirements.txt
	```

## Running

* Defaults:
	```bash
	python3 game_of_life.py
	```

* Different Sizes:
	```bash
	python3 game_of_life.py -s 100
	```

* Different Simulation Rates:
	```bash
	python3 game_of_life.py -r 20
	```

* Import Image:
	```bash
	python3 game_of_life.py -r 10 -i file -f presets/glider_gun.png
	```

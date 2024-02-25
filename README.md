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

* Defaults: `python3 game_of_life.py`

* Different Sizes: `python3 game_of_life.py -s 100`

* Different Simulation Rates: `python3 game_of_life.py -r 20`

* Import Image: `python3 game_of_life.py -r 10 -i file -f presets/glider_gun.png`

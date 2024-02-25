import argparse

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

parser = argparse.ArgumentParser(
    prog="Conway's Game of Life",
    description="Simulation of Conway's Game of Life using NumPy, SciPy, and Matplotlib.",
    epilog="Created by James Muir.",
)

parser.add_argument(
    "-r",
    "--rate",
    help="simulation rate (Hz)",
    metavar="f",
    default=1,
    type=int,
)

parser.add_argument(
    "-i",
    "--init",
    choices=["random", "file"],
    help="source of the initial board state",
    default="random",
    metavar="source"
)

parser.add_argument(
    "-s",
    "--size",
    help="number of cells on one side of the square board",
    metavar="N",
    default=30,
    type=int,
)

parser.add_argument(
    "-f",
    "--file",
    help="image file to use as initial board state",
    metavar="/path/to/file",
)

args = parser.parse_args()

if args.init == "random":
    rng = np.random.default_rng()
    board = rng.integers(1, size=(args.size, args.size), dtype=bool, endpoint=True)

if args.init == "file":
    # negate image to make black pixels True
    board = ~plt.imread(args.file).astype(bool)

neighbors_kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

# make program stop when figure is closed
running = True


def close(event):
    global running
    running = False


fig, ax = plt.subplots()
fig.canvas.mpl_connect("close_event", close)

# main loop
while running:
    # display board
    ax.imshow(board, cmap="binary")
    plt.pause(1/args.rate)

    # calculate new board
    neighbors = convolve(board, neighbors_kernel, mode="same")
    board = board * (neighbors == 2) + (neighbors == 3)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

rng = np.random.default_rng()

BOARD_SIZE = 100
# 
# board = np.zeros([BOARD_SIZE, BOARD_SIZE])
# board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
board = rng.integers(1, size=(BOARD_SIZE, BOARD_SIZE), dtype=bool, endpoint=True)
# print(f"{board=}")

neighbors_kernel = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]])

# make program stop when figure is closed
running = True
def close(event):
    global running
    running = False
fig, ax = plt.subplots()
fig.canvas.mpl_connect("close_event", close)

# main loop
while running:
    print(f"{running=}")
    # display board
    ax.imshow(board, cmap="binary")
    plt.pause(1)

    # calculate new board
    neighbors = convolve(board, neighbors_kernel, mode="same")
    board = board * (neighbors == 2) + (neighbors == 3)
    
    # print(f"{neighbors=}")


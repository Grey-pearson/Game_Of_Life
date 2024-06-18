import sys
import time
from collections import defaultdict, namedtuple
from copy import deepcopy
import pygame

Dimension = namedtuple("Dimension", ["width", "height"])
Grid = namedtuple("Grid", ["dimension", "cells"])
Neighbors = namedtuple("Neighbors", ["alive", "dead"])

GOSPER_GLIDER = Grid(
    Dimension(50, 50),
    {
        (22, 8),
        (12, 7),
        (36, 7),
        (17, 9),
        (11, 8),
        (1, 9),
        (25, 4),
        (2, 8),
        (16, 7),
        (25, 10),
        (21, 6),
        (23, 9),
        (14, 6),
        (36, 6),
        (22, 7),
        (14, 12),
        (17, 8),
        (11, 10),
        (25, 9),
        (35, 7),
        (1, 8),
        (18, 9),
        (22, 6),
        (21, 8),
        (23, 5),
        (12, 11),
        (17, 10),
        (11, 9),
        (35, 6),
        (25, 5),
        (2, 9),
        (13, 6),
        (13, 12),
        (15, 9),
        (16, 11),
        (21, 7),
    },
)

def get_neighbors(grid: Grid, x: int, y: int) -> Neighbors:
    # loops through all cells in GOSPER_GLIDER (all active) and figures out how many neighbors it has
    # that way we can decide if it stays active or dies
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    possible_neighbors = {(x + x_add, y + y_add) for x_add, y_add in offsets} # looping thorugh offsets
    alive = {(pos[0], pos[1]) for pos in possible_neighbors if pos in grid.cells}
    return Neighbors(alive, possible_neighbors - alive)


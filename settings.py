WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6
CELL_COUNT = GRID_SIZE ** 2
MINES_COUNT = (CELL_COUNT) // 10
CELL_HEIGHT = 4
CELL_WIDTH = 12


# Easy difficulty settings
EASY_DIFFICULTY_SETTINGS = {
    "GRID_SIZE": 6,
    "MINES_COUNT": (6**2) // 10,
    "CELL_HEIGHT": 4,
    "CELL_WIDTH": 12
}

# Medium difficulty settings
MEDIUM_DIFFICULTY_SETTINGS = {
    "GRID_SIZE": 8,
    "MINES_COUNT": (8**2) // 6,
    "CELL_HEIGHT": 3,
    "CELL_WIDTH": 9
}

# Hard difficulty settings
HARD_DIFFICULTY_SETTINGS = {
    "GRID_SIZE": 10,
    "MINES_COUNT": (10**2) // 4,
    "CELL_HEIGHT": 2,
    "CELL_WIDTH": 6
}
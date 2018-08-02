

BANNER = r"""
 ____        _   _   _           _     _
| __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __
|  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                        |_|
"""

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
# Using mdash instead of hyphen
HORIZONTAL_SHIP = '\u2014'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

BOARD_HEADING = ("   " + " ".join(
    [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

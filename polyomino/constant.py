MONOMINO = [(0, 0)]

DOMINO = [(0, 0), (0, 1)]

TROMINOS = {"Straight": [(0, 0), (0, 1), (0, 2)], "Right": [(0, 0), (0, 1), (1, 1)]}

ALL_TROMINOS = list(TROMINOS.values())

STRAIGHT_TROMINO = TROMINOS["Straight"]
RIGHT_TROMINO = TROMINOS["Right"]

TETROMINOS = {
    "Square": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(0, 0), (1, 1), (1, 0), (2, 0)],
    "S": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "Line": [(0, 0), (1, 0), (2, 0), (3, 0)],
    "J": [(0, 0), (1, 0), (1, 1), (1, 2)],
}

ALL_TETROMINOS = list(TETROMINOS.values())

ONESIDED_TETROMINOS = TETROMINOS
ONESIDED_TETROMINOS.update(
    {"Z": [(0, 1), (1, 0), (1, 1), (2, 0)], "L": [(0, 0), (0, 1), (0, 2), (1, 0)]}
)

PENTOMINOS = {
    "F": [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2)],
    "I": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    "L": [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)],
    "N": [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)],
    "P": [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
    "T": [(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)],
    "U": [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],
    "V": [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)],
    "W": [(0, 2), (0, 1), (1, 1), (1, 0), (2, 0)],
    "X": [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],
    "Y": [(0, 2), (1, 0), (1, 1), (1, 2), (1, 3)],
    "Z": [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)],
}

ALL_PENTOMINOS = list(PENTOMINOS.values())

ALL_UP_TO_PENTOMINOS = (
    [MONOMINO, DOMINO] + ALL_TROMINOS + ALL_TETROMINOS + ALL_PENTOMINOS
)

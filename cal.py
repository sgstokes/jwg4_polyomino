from polyomino.board import Rectangle


def main():
    combinations = {
        1: {
            "Z4A": [(0, 0), (1, 0), (1, 1), (2, 1)],
            "L4A": [(0, 0), (1, 0), (1, 1), (1, 2)],
        },
        2: {
            "Z4B": [(0, 1), (1, 0), (1, 1), (2, 0)],
            "L4B": [(0, 0), (0, 1), (0, 2), (1, 0)],
        },
        3: {
            "Z4A": [(0, 0), (1, 0), (1, 1), (2, 1)],
            "L4B": [(0, 0), (0, 1), (0, 2), (1, 0)],
        },
        4: {
            "Z4B": [(0, 1), (1, 0), (1, 1), (2, 0)],
            "L4A": [(0, 0), (1, 0), (1, 1), (1, 2)],
        },
    }

    base_tiles = {
        "O4": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "T4": [(0, 0), (1, 1), (1, 0), (2, 0)],
        "L5": [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)],
        "P5": [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
        "U5": [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],
        "X5": [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],
        "Z5": [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)],
    }

    missing_months = [(6, 0), (6, 1)]
    missing_days = [(0, 6), (1, 6), (5, 6), (6, 6)]
    missing_cells = missing_months + missing_days
    months = get_cells((0, 7), (0, 2), missing_months)
    days = get_cells((0, 7), (2, 7), missing_days)

    for m in months:
        month = m

        for d in days:
            day = d

            print(f"{month} {day}")

            board = Rectangle(7, 7)
            for m in missing_cells:
                board = board.remove(m)

            board = board.remove(month).remove(day)

            print(board.display())

            for k in combinations.keys():
                tiles = base_tiles.copy()
                tiles.update(combinations[k])

                problem = board.tile_with(list(tiles.values()))
                solution = problem.solve()

                if solution is None:
                    continue

            if solution is not None:
                print(solution.display())
            else:
                print("No solution found!")


def get_cells(x, y, missing=None):
    x_start, x_stop = x
    y_start, y_stop = y
    cells = []

    for i in range(x_start, x_stop):
        for j in range(y_start, y_stop):
            cells.append((i, j))

    for m in missing:
        cells.remove(m)

    return cells


# Run main program
if __name__ == "__main__":
    main()

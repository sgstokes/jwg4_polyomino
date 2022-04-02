import itertools as it

from numpy import tile

from polyomino.board import Rectangle


def main():
    base_tiles = {
        "O4": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "T4": [(0, 0), (1, 1), (1, 0), (2, 0)],
        "U5": [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],
        "X5": [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],
    }
    z4_tiles = [
        {"z4a": [(0, 0), (1, 0), (1, 1), (2, 1)]},
        {"z4b": [(0, 1), (1, 0), (1, 1), (2, 0)]},
    ]
    l4_tiles = [
        {"l4a": [(0, 0), (1, 0), (1, 1), (1, 2)]},
        {"l4b": [(0, 0), (1, 0), (0, 1), (0, 2)]},
    ]
    l5_tiles = [
        {"l5a": [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)]},
        {"l5b": [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)]},
    ]
    p5_tiles = [
        {"p5a": [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]},
        {"p5b": [(0, 0), (0, 1), (1, 2), (1, 1), (1, 2)]},
    ]
    z5_tiles = [
        {"z5a": [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]},
        {"z5b": [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]},
    ]
    tile_options = [z4_tiles, l4_tiles, l5_tiles, p5_tiles, z5_tiles]
    combinations = list(it.product([0, 1], repeat=5))

    missing_months = [(6, 0), (6, 1)]
    missing_days = [(0, 6), (1, 6), (5, 6), (6, 6)]
    missing_cells = missing_months + missing_days
    months = get_cells((0, 7), (0, 2), missing_months)
    days = get_cells((0, 7), (2, 7), missing_days)

    solutions_file = open("output/solutions.txt", "w")
    no_solutions_file = open("output/no_solutions.txt", "w")

    for m in months:
        month = m
        for d in days:
            day = d

            board = Rectangle(7, 7)
            board = board.remove(month).remove(day)
            for m in missing_cells:
                board = board.remove(m)

            for c in combinations:
                tiles = base_tiles.copy()
                for ix, i in enumerate(c):
                    tiles.update(tile_options[ix][i])

                problem = board.tile_with(list(tiles.values()))
                solution = problem.solve()
                if solution is not None:
                    break

            if solution is None:
                no_solutions_file.write(f"{month} {day}\n{board.display()}\n\n")
                print("No solution found!")
            else:
                solutions_file.write(f"{month} {day}\n{solution.display()}\n\n")
                print(f"{month} {day}\n{solution.display()}\n\n")

    solutions_file.close()
    no_solutions_file.close()


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

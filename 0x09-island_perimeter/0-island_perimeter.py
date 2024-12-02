#!/usr/bin/python3
"""Island perimeter module."""


def island_perimeter(grid):
    """Computes perimeter of an island with no lakes."""
    perimeter = 0
    if type(grid) != list:
        return 0
    no = len(grid)
    for i, row in enumerate(grid):
        ro = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == ro - 1 or (ro > j + 1 and row[j + 1] == 0),
                i == no - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter

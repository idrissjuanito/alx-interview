#!/usr/bin/python3
""" Island Perimeter module """


def island_perimeter(grid):
    """
    Finds and calculates the perimeter of an island in a grid
    """
    width = 0
    height = 0
    height_idx = 0
    if len(grid) > 100 or len(grid[0]) > 100:
        return 0
    for i in range(len(grid)):
        j = height_idx
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    width += 1
                if j == 0 or grid[i][j - 1] == 0:
                    height += 1
    perimeter = (width + height) * 2
    return perimeter

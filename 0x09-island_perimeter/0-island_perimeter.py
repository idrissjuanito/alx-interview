#!/usr/bin/python3
""" Island Perimeter module """


def island_perimeter(grid):
    """
    Finds and calculates the perimeter of an island in a grid
    """
    width = 0
    height = 0
    height_idx = 0
    for i in range(len(grid)):
        j = height_idx
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i + 1][j] == 0:
                    width += 1
                if grid[i][j - 1] == 0:
                    height += 1


    perimeter = (width + height) * 2
    return perimeter

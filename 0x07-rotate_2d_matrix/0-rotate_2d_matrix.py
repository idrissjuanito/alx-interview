#!/usr/bin/python3
""" 2D Matrix rotation """


def rotate_2d_matrix(matrix):
    """ Rotates a 2D matrix list """
    N = len(matrix)

    for i in range(int(N / 2)):
        for j in range(i, N - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp

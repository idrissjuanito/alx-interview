#!/usr/bin/python3
""" Solving the n queens """
import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]
if type(N) is not int:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("If N is smaller than 4, print ")
    sys.exit(1)

for i in range(N - 2):
    lst = []
    inc = i + 2
    decr = N - i - 1
    y = i + 1
    for x in range(N):
        if x > 0:
            prev_y = lst[x - 1][1]
            new_y = prev_y + inc
            if new_y >= N:
                y = prev_y - decr
            else:
                y = new_y
        lst.append([x, y])
    print(lst)

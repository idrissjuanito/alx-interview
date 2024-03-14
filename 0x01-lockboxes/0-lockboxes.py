#!/usr/bin/python3
""" breaking into lock boxes """


def canUnlockAll(boxes):
    """ functions unlock all boxes passed as param """
    keys = set([0])
    locked = list()
    for i in range(len(boxes)):
        if i in keys:
            keys.update(boxes[i])
        else:
            locked.append(i)

    if len(locked) > 0:
        locked_copy = [*locked]
        for i in locked_copy:
            if i in keys:
                locked.remove(i)
                keys.update(boxes[i])
    if len(locked) > 0:
        return False
    else:
        return True

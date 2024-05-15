#!/usr/bin/python3
""" Prime game module """


def play(roundSet, playing, potentialWinner):
    """ executes a players move """
    if len(roundSet) == 1:
        return potentialWinner
    prime = roundSet[1]
    for j in range(len(roundSet)):
        if j >= len(roundSet):
            break
        if roundSet[j] % prime == 0:
            roundSet.pop(j)
    return play(roundSet, potentialWinner, playing)


def isWinner(x, nums):
    """ Finds the winner after x number of rounds
    what if x is great than len nums
    what if len nums is greater that x
    """
    players = {
            "Maria": 0,
            "Ben": 0
            }
    round = 0
    while round < x and round < len(nums):
        roundSet = [i for i in range(1, nums[round] + 1)]
        roundWinner = play(roundSet, "Maria", "Ben")
        players[roundWinner] += 1
        round += 1
    if players["maria"] == players["Ben"]: return None
    return "Maria" if players["Maria"] > players["Ben"] else "Ben"

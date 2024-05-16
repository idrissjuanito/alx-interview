#!/usr/bin/python3
""" Prime game module """
primes = []


def play(roundSet, playing, potentialWinner):
    """ executes a players move """

    if len(roundSet) == 1:
        return potentialWinner
    prime = roundSet[1]
    primes.append(prime)
    for j in range(len(roundSet)):
        if j >= len(roundSet):
            break
        num = roundSet[j]
        if num % prime == 0:
            roundSet.pop(j)
    return play(roundSet, potentialWinner, playing)


def isWinner(x, nums):
    """ Finds the winner after x number of rounds
    what if x is great than len nums
    what if len nums is greater that x
    """
    players = {"Maria": 0, "Ben": 0}
    round = 0
    nums.sort()
    prev_n = 0
    while round < x:
        if round >= len(nums):
            n = nums[round - len(nums) - 1]
        else:
            n = nums[round]
        roundSet = [1] if prev_n > 0 else []
        roundSet += primes.copy()
        for i in range(prev_n + 1, n + 1):
            roundSet.append(i)
        primes.clear()
        roundWinner = play(roundSet, "Maria", "Ben")
        print(roundWinner)
        players[roundWinner] += 1
        prev_n = n
        round += 1
    if players["Maria"] == players["Ben"]:
        return None
    return "Maria" if players["Maria"] > players["Ben"] else "Ben"

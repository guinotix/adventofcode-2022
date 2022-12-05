import sys
from typing import *


def crates(fichero: List[str]) -> List[List[chr]]:
    stacks = [
        ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
        ['D', 'N', 'T', 'S', 'B', 'Z'],
        ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
        ['G', 'R', 'Z'],
        ['Z', 'N', 'R', 'H'],
        ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
        ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
        ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
        ['S', 'Q', 'P', 'W', 'N']
    ]

    for linea in fichero:
        current = linea.strip().split(' ')
        q_to_move, prev, target = int(current[1]), int(current[3]), int(current[5])
        while q_to_move > 0:
            crate = stacks[prev-1].pop()
            q_to_move -= 1
            stacks[target-1].append(crate)
    return stacks


def cratemover(fichero: List[str]):
    stacks = [
        ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
        ['D', 'N', 'T', 'S', 'B', 'Z'],
        ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
        ['G', 'R', 'Z'],
        ['Z', 'N', 'R', 'H'],
        ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
        ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
        ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
        ['S', 'Q', 'P', 'W', 'N']
    ]

    for linea in fichero:
        current = linea.strip().split(' ')
        quantity, prev, target = int(current[1]), int(current[3]), int(current[5])

        # index of the first item that will be held
        i = len(stacks[prev - 1]) - quantity

        # the brace of the robot
        holding = []

        # put all the crates from a stack to the robot
        while i < len(stacks[prev-1]):
            holding.append(stacks[prev-1][i])
            i += 1

        # remove the items of the robot from the stack
        while quantity > 0:
            stacks[prev-1].pop()
            quantity -= 1

        # put the items of the robot in the target stack
        for item in holding:
            stacks[target - 1].append(item)

    return stacks


if __name__ == '__main__':

    fichero = sys.stdin.readlines()
    solved = crates(fichero)
    cratemover = cratemover(fichero)

    resultA = []
    resultB = []
    for stack in solved:
        resultA.append(stack[-1])
    for stack in cratemover:
        resultB.append(stack[-1])
    print(resultA)
    print(resultB)
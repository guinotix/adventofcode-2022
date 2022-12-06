import sys
from typing import *


def part1(fichero: str) -> Tuple[List[str], int]:
    for i in range(len(fichero)):
        a, b, c, d = fichero[i], fichero[i+1], fichero[i+2], fichero[i+3]
        if a != b and b != c and c != d and d != a and a != c and b != d:
            return [a, b, c, d], i+4


def part2(fichero: str):
    for i in range(len(fichero)):
        substring = fichero[i:i+14]
        if check(substring):
            return substring, i+14


def check(substring: str):
    current = []
    for elem in substring:
        if elem not in current:
            current.append(elem)
        else:
            return False
    return True



if __name__ == '__main__':
    fichero = sys.stdin.readlines()[0]
    print(part1(fichero))
    print(part2(fichero))
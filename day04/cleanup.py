import sys
from typing import *


def cleanup(fichero: List[str]) -> int:
    overlaps = 0
    for linea in fichero:

        elf1: str = linea.strip().split(',')[0]
        elf2: str = linea.strip().split(',')[1]
        g1_init = int(elf1.split('-')[0])
        g1_end = int(elf1.split('-')[1])
        g2_init = int(elf2.split('-')[0])
        g2_end = int(elf2.split('-')[1])

        if g2_init >= g1_init and g2_end <= g1_end:
            overlaps += 1
        elif g1_init >= g2_init and g1_end <= g2_end:
            overlaps += 1

    return overlaps


def cleanup_maxmin(fichero: List[str]) -> int:
    overlaps = 0
    for linea in fichero:

        elf1: str = linea.strip().split(',')[0]
        elf2: str = linea.strip().split(',')[1]
        g1_init = int(elf1.split('-')[0])
        g1_end = int(elf1.split('-')[1])
        g2_init = int(elf2.split('-')[0])
        g2_end = int(elf2.split('-')[1])

        if max(g1_init, g2_init) <= min(g1_end, g2_end):
            overlaps += 1

    return overlaps


if __name__ == '__main__':
    fichero = sys.stdin.readlines()

    solapamientos = cleanup(fichero)
    solapamientos_maxmin = cleanup_maxmin(fichero)

    print(solapamientos)
    print(solapamientos_maxmin)
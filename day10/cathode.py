import sys
from typing import *


def read_file(fichero: List[str]):
    program = []
    for linea in fichero:
        program.append(linea.strip().split(' '))
    return program


def solve(program: List[List[str]]):
    register = 1
    cycles = 0
    signals = {}
    for instruction in program:
        if instruction[0] == "noop":
            cycles += 1
            signals[cycles] = cycles * register
        elif instruction[0] == "addx":
            cycles += 1
            signals[cycles] = cycles * register
            cycles += 1
            signals[cycles] = cycles * register
            register += int(instruction[1])
    return signals


def solve_part2(program: List[List[str]]):
    pixels = list("." * 40 * 6)
    register = 1
    cycles = 0
    for instruction in program:
        if instruction[0] == "noop":
            cycles += 1
            draw(register, cycles, pixels)
        elif instruction[0] == "addx":
            cycles += 1
            draw(register, cycles, pixels)
            cycles += 1
            draw(register, cycles, pixels)
            register += int(instruction[1])
    return pixels


def draw(register, cycles, pixels):
    if (cycles - 1) % 40 in [register-1, register, register+1]:
        pixels[cycles] = "#"


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    program = read_file(fichero)

    signals = solve(program)
    print(signals[20] + signals[60] + signals[100] + signals[140] + signals[180] + signals[220])

    pixels = solve_part2(program)
    for i in range(0, len(pixels), 40):
        print(" ".join(pixels[i:i+40]))
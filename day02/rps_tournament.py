import sys
from typing import *


def init_game():
    matrixrps = [[3, 0, 6], [6, 3, 0], [0, 6, 3]]
    addpoints = [1, 2, 3]
    return matrixrps, addpoints

def game_decrypted():
    matrixrps = [[0, 0, 0], [3, 3, 3], [6, 6, 6]]
    addpoints = [1, 2, 3]
    return matrixrps, addpoints


def read_file(fichero: List[str]) -> int:
    matriz, puntos = init_game()
    matriz_dec, _ = game_decrypted()
    suma = 0
    for linea in fichero:
        current = linea.strip().split(' ')
        # ronda = calculate_round(current[0], current[1], matriz, puntos)
        ronda = decrypted_round(current[0], current[1], matriz_dec, puntos)
        suma += ronda
    return suma

def decrypted_round(op: str, you: str, m: List[List[int]], p: List[int]) -> int:
    if op == "A":
        if you == "X":
            return m[0][0] + p[2]
        if you == "Y":
            return m[1][0] + p[0]
        else:
            return m[2][0] + p[1]
    if op == "B":
        if you == "X":
            return m[0][1] + p[0]
        if you == "Y":
            return m[1][1] + p[1]
        else:
            return m[2][1] + p[2]
    else:
        if you == "X":
            return m[0][2] + p[1]
        elif you == "Y":
            return m[1][2] + p[2]
        else:
            return m[2][2] + p[0]

def calculate_round(op: str, you: str, m: List[List[int]], p: List[int]) -> int:
    if op == "A":
        if you == "X":
            return m[0][0] + p[0]
        if you == "Y":
            return m[1][0] + p[1]
        else:
            return m[2][0] + p[2]
    if op == "B":
        if you == "X":
            return m[0][1] + p[0]
        if you == "Y":
            return m[1][1] + p[1]
        else:
            return m[2][1] + p[2]
    else:
        if you == "X":
            return m[0][2] + p[0]
        elif you == "Y":
            return m[1][2] + p[1]
        else:
            return m[2][2] + p[2]

if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    resultado = read_file(fichero)
    print(resultado)
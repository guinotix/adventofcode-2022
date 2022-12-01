import sys
from typing import *


def read_file(fichero: List[str]) -> List[int]:
    file_formatted = []
    for linea in fichero:
        current = linea.strip().split(' ')
        if current[0] == "":
            file_formatted.append(0)
        else:
            file_formatted.append(int(current[0]))
    return file_formatted

def calculate_elves_calories(fichero: List[int]) -> Dict[int, int]:
    elves = {}
    i = 1
    elf_sum = 0
    for elem in fichero:
        if elem == 0:
            elves[i] = elf_sum
            i += 1
            elf_sum = 0
        else:
            elf_sum += elem
    return elves

def find_elf(dic: Dict[int, int]) -> Tuple[int, int]:
    elf = 0
    calories = -1
    for k,v in dic.items():
        if k == 1:
            elf, calories = k, v
        else:
            if v > calories:
                elf, calories = k, v
    return elf, calories

def find_top_three(dic: Dict[int, int]) -> List[Tuple[int, int]]:
    l = []
    for k, v in dic.items():
        l.append((k, v))
    l.sort(key=lambda c: c[1], reverse=True)
    return l


if __name__ == '__main__':
    lineas = sys.stdin.readlines()
    fichero = read_file(lineas)

    elfos = calculate_elves_calories(fichero)
    elfo_calorico = find_elf(elfos)
    tres_mejores_elfos = find_top_three(elfos)

    print(elfo_calorico)
    print(f"{tres_mejores_elfos[0]} "
          f"{tres_mejores_elfos[1]} "
          f"{tres_mejores_elfos[2]}")

    print(tres_mejores_elfos[0][1]+tres_mejores_elfos[1][1]+tres_mejores_elfos[2][1])
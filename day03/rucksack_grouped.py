import sys
from typing import *


def read_file(fichero: List[str]) -> List[List[str]]:
    file, group = [], []
    i = 1
    for linea in fichero:
        group.append(linea.strip())
        if i == 3:
            i = 1
            file.append(group)
            group = []
        else:
            i += 1
    return file

def letters_in_one_group(group: List[str]) -> Tuple[List[chr], List[chr], List[chr]]:
    c1, c2, c3 = [], [], []
    for char in group[0]:
        if char not in c1:
            c1.append(char)
    for char in group[1]:
        if char not in c2:
            c2.append(char)
    for char in group[2]:
        if char not in c3:
            c3.append(char)
    return c1, c2, c3

def rucksack(items: List[List[str]]) -> int:
    sum_priorities = 0
    u, d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'
    for item in items:
        a, b, c = letters_in_one_group(item)
        common = list(set(a).intersection(b).intersection(c))
        for badge in common:
            if badge in u:
                val = ord(badge) - 64 + 26
                sum_priorities += val
            elif badge in d:
                val = ord(badge) - 96
                sum_priorities += val
    return sum_priorities


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    formateado = read_file(fichero)
    print(rucksack(formateado))
import sys
from typing import *


def read_file(fichero: List[str]) -> List[str]:
    file = []
    for linea in fichero:
        file.append(linea.strip())
    return file

def letters_in_one_line(line: str) -> Tuple[List[chr], List[chr]]:
    str1, str2 = line[0:len(line) // 2], line[len(line) // 2:]
    c1, c2 = [], []
    for char in str1:
        if char not in c1:
            c1.append(char)
    for char in str2:
        if char not in c2:
            c2.append(char)
    return c1, c2

def rucksack(items: List[str]) -> int:
    sum_priorities = 0
    u, d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'
    for item in items:
        left, right = letters_in_one_line(item)
        common = list(set(left).intersection(right))
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
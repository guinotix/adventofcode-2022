import sys
from typing import *


def read_file(fichero: List[str]):
    movements = []
    for linea in fichero:
        linea = linea.strip().split(' ')
        movements.append((linea[0], int(linea[1])))
    return movements


def update_position(head, tail, dir):
    head_previous_position = head.copy()
    if dir == 'L':
        head[0] -= 1
        if is_tail_attached(head, tail) == False:
            tail[0] = head_previous_position[0]
            tail[1] = head_previous_position[1]
    elif dir == 'R':
        head[0] += 1
        if is_tail_attached(head, tail) == False:
            tail[0] = head_previous_position[0]
            tail[1] = head_previous_position[1]
    elif dir == 'U':
        head[1] += 1
        if is_tail_attached(head, tail) == False:
            tail[0] = head_previous_position[0]
            tail[1] = head_previous_position[1]
    elif dir == 'D':
        head[1] -= 1
        if is_tail_attached(head, tail) == False:
            tail[0] = head_previous_position[0]
            tail[1] = head_previous_position[1]
    tail_v.append(tail.copy())


def is_tail_attached(head, tail):
    # check the distance between head and tail
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return False
    return True


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    movements = read_file(fichero)

    head, tail = [0, 0], [0, 0]
    tail_v = [[0, 0]]

    for direction, steps in movements:
        for _ in range(steps):
            update_position(head, tail, direction)

    set_visited_tail = set()
    for elem in tail_v:
        set_visited_tail.add(tuple(elem))
    print(len(set_visited_tail))
import sys
from typing import *


def read_file(fichero: List[str]):
    movements = []
    for linea in fichero:
        linea = linea.strip().split(' ')
        movements.append((linea[0], int(linea[1])))
    return movements


class Knot:
    def __init__(self, n):
        self.n = n
        self.position = [0, 0]
        self.visited = [[0, 0]]

    def move_head(self, dir):
        self.previous_position = self.position.copy()
        if dir == 'L':
            self.position[0] -= 1
        elif dir == 'R':
            self.position[0] += 1
        elif dir == 'U':
            self.position[1] += 1
        elif dir == 'D':
            self.position[1] -= 1
        self.visited.append(self.previous_position)

    def move_knot(self, target):
        self.position = target
        self.visited.append(target)

    def visited_positions(self):
        visited = set()
        for position in self.visited:
            visited.add(tuple(position))
        return visited


def update_position(knots, dir):

    knots[0].move_head(dir)

    for i in range(1, len(knots)):

        # check the distance between current knot and its previous
        if abs(knots[i].position[0] - knots[i-1].position[0]) > 1 or abs(knots[i].position[1] - knots[i-1].position[1]) > 1:
            # three options: knots moving in the same row, column or both (diagonally)

            # check how far is the current knot to the row/col
            posX = knots[i-1].position[0] - knots[i].position[0]
            posY = knots[i-1].position[1] - knots[i].position[1]

            # column
            if posX == 0:
                changeY = -1
                if posY >= 0:
                    changeY = 1
                knots[i].move_knot([knots[i].position[0], knots[i].position[1]+changeY])

            # row
            elif posY == 0:
                changeX = -1
                if posX >= 0:
                    changeX = 1
                knots[i].move_knot([knots[i].position[0]+changeX, knots[i].position[1]])

            # diagonal movement
            else:
                changeX, changeY = -1, -1
                if posX >= 0:
                    changeX = 1
                if posY >= 0:
                    changeY = 1
                knots[i].move_knot([knots[i].position[0]+changeX, knots[i].position[1]+changeY])


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    movements = read_file(fichero)

    knots = []
    for i in range(10):
        knots.append(Knot(i))

    for direction, steps in movements:
        for _ in range(steps):
            update_position(knots, direction)

    print(len(knots[9].visited_positions()))

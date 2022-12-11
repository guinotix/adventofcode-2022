import sys
from typing import *


def visible_trees(forest: List[List[int]]):

    # exterior perimeter initialized
    visibleTrees = len(forest)*2 + len(forest[0])*2 - 4

    for row in range(1, len(forest[0])-1):
        for col in range(1, len(forest)-1):
            # current tree in the interior sector
            tree = forest[row][col]

            # get line-adjacent trees
            leftTrees = forest[row][0:col]
            rightTrees = forest[row][col+1:]
            upTrees = [vert[col] for vert in forest][0:row]
            downTrees = [vert[col] for vert in forest][row+1:]

            # check in these directions if there are visibles trees
            if any([all(tree > otherTree for otherTree in adjacents) for adjacents in [leftTrees, rightTrees, upTrees, downTrees]]):
                visibleTrees += 1

    print(visibleTrees)


def scenic(forest: List[List[int]]):

    maxScore = 0

    for row in range(1, len(forest[0])-1):
        for col in range(1, len(forest)-1):
            tree = forest[row][col]
            scenics = [0, 0, 0, 0] # left, right, up, down

            # left
            for i in range(1, col+1):
                scenics[0] += 1
                if tree <= forest[row][col-i]:
                    break

            # right
            for i in range(col + 1, len(forest)):
                scenics[1] += 1
                if tree <= forest[row][i]:
                    break

            # up
            for i in range(1, row+1):
                scenics[2] += 1
                if tree <= forest[row-i][col]:
                    break

            # down
            for i in range(row+1, len(forest)):
                scenics[3] += 1
                if tree <= forest[i][col]:
                    break

            score = scenics[0] * scenics[1] * scenics[2] * scenics[3]
            maxScore = max(maxScore, score)

    print(maxScore)


def generate_forest(fichero: List[str]):
    forest = []
    for linea in fichero:
        linea = linea.strip()
        row = []
        for elem in linea:
            row.append(int(elem))
        forest.append(row)
    return forest


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    forest = generate_forest(fichero)
    visible_trees(forest)
    scenic(forest)
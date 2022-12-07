import sys
from typing import *
from math import inf


def sum_of_sizes(fichero: List[str]) -> dict:
    filesystem = dict()
    path = ""
    for linea in fichero:
        stripped = linea.strip().split(" ")
        if stripped[0] == "$":
            # go back to the previous directory
            if stripped[1] == "cd" and stripped[2] == "..":
                prevPath = path
                for i in range(len(path)-2, -1, -1):
                    if path[i] == "/":
                        path = path[0:len(path)-1]
                        break
                    else:
                        path = path[0:len(path)-1]
                filesystem[path] += filesystem[prevPath]
            # advance to next directory
            elif stripped[1] == "cd" and stripped[2] != "..":
                if stripped[2] == "/":
                    path = stripped[2]
                else:
                    path += stripped[2] + "/"
                # if visited for the first time
                if path not in filesystem.keys():
                    filesystem[path] = 0
        else:
            # it is a file
            if stripped[0] != "dir":
                filesystem[path] += int(stripped[0])
    return filesystem


def delete_directory(filesystem: dict):
    filesystem_size = 70000000
    target = 30000000
    current_size = filesystem["/"]
    unused = filesystem_size - current_size
    min_needed = target - unused
    to_delete = inf
    for v in filesystem.values():
        if v < to_delete and v >= min_needed:
            to_delete = v
    return to_delete


if __name__ == '__main__':
    fichero = sys.stdin.readlines()
    filesystem = sum_of_sizes(fichero)

    totalSize = 0
    for v in filesystem.values():
        if v <= 100000:
            totalSize += v

    print(totalSize)
    print(delete_directory(filesystem))
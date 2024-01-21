# import sys, time
#
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# zero = []
# start_time = time.perf_counter()
#
#
# def check(x, y, target):
#     sx, sy = x - x % 3, y - y % 3
#
#     for i in range(sy, sy + 3):
#         for j in range(sx, sx + 3):
#             if graph[i][j] == target:
#                 return False
#
#     for i in range(0, 9):
#         if graph[i][x] == target or graph[y][i] == target:
#             return False
#
#     return True
#
#
# def backtracking(index, depth):
#     global start_time
#     if depth == len(zero):
#         for g in graph:
#             print(*g)
#         end_time = time.perf_counter()
#         print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")
#         exit()
#
#     dx, dy = zero[index][0], zero[index][1]
#     for i in range(1, 10):
#         if check(dx, dy, i):
#             graph[dy][dx] = i
#             backtracking(index + 1, depth + 1)
#             graph[dy][dx] = 0
#
#
# for y in range(9):
#     for x in range(9):
#         if graph[y][x] == 0:
#             zero.append((x, y))
#
# backtracking(0, 0)

import sys, time

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = []
start_time = time.perf_counter()


def check(x, y):
    sx, sy = x - x % 3, y - y % 3
    reference = set([i for i in range(1, 10)])
    checked = set()

    for i in range(sy, sy + 3):
        for j in range(sx, sx + 3):
            checked.add(graph[i][j])

    for i in range(9):
        checked.add(graph[i][x])
        checked.add(graph[y][i])

    checked.remove(0)
    return reference.difference(checked)


def backtracking(index, depth):
    global start_time
    if depth == len(zero):
        for g in graph:
            print(*g)
        end_time = time.perf_counter()
        print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")
        exit()

    dx, dy = zero[index][0], zero[index][1]
    for i in check(dx, dy):
        graph[dy][dx] = i
        backtracking(index + 1, depth + 1)
        graph[dy][dx] = 0


for y in range(9):
    for x in range(9):
        if graph[y][x] == 0:
            zero.append((x, y))

backtracking(0, 0)

import sys
from itertools import combinations


def deepcopy(iterator):
    return [item[:] for item in iterator]


def get_ranger():
    return list(combinations(range(M), 3))


def attack(s, r, ct):
    result = []
    enemy = list(filter(lambda item: item[1] < s, ct))

    for rx, ry in r:
        target = [20, 20]
        distance = D

        for ex, ey in enemy:
            tmp = abs(rx - ex) + abs(ry - ey)
            if tmp == distance:
                if ex < target[0]:
                    target = [ex, ey]
            elif tmp < distance:
                target = [ex, ey]
                distance = tmp

        if target not in result and target != [20, 20]:
            result.append(target)

    return result


def solution():
    result = 0
    for ranger in get_ranger():
        kill_score = 0
        _map = deepcopy(board)
        copy_target = deepcopy(targets)

        for stage in range(N, 0, -1):
            rangers = [(r, stage) for r in ranger]

            dead = attack(stage, rangers, copy_target)
            copy_target = [ct for ct in copy_target if ct not in dead]

            kill_score += len(dead)
        result = max(result, kill_score)

    return result


N, M, D = map(int, sys.stdin.readline().split()) # 세로, 가로 = y, x
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

targets = []

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            targets.append([x, y])

answer = solution()
print(answer)
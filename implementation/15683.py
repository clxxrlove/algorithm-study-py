import sys


def deepcopy(iterable): # 2dx
    return [item[:] for item in iterable]


def check(x, y, d, item):
    for dir in d:
        nx, ny = x, y
        while True:
            nx += dx[dir]
            ny += dy[dir]

            if nx < 0 or ny < 0 or nx >= M or ny >= N or item[ny][nx] == 6:
                break
            if item[ny][nx] != 0:
                continue
            item[ny][nx] = "#"


def dfs(depth, original):
    copied = deepcopy(original)

    if depth == len(cctv):
        global answer
        tmp = 0

        for c in copied:
            tmp += c.count(0)

        answer = min(answer, tmp)
        return

    c_type, x, y = cctv[depth]

    for d in directions[c_type]:
        check(x, y, d, copied)
        dfs(depth + 1, copied)
        copied = deepcopy(original)


N, M = map(int, sys.stdin.readline().split()) # y, x
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

cctv = []
answer = 0

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            answer += 1
        elif 0 < board[y][x] <= 5:
            cctv.append((board[y][x], x, y))

dfs(0, board)
print(answer)
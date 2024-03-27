import sys


def backtracking(x, y, depth):
    global answer
    if check():
        answer = min(answer, depth)
        return
    if depth >= answer:
        return
    if depth >= 3:
        return

    for dx in range(x, M):
        tmp = 0
        if dx == x:
            tmp = y
        for dy in range(tmp, N - 1):
            if graph[dx][dy] == 0 and graph[dx][dy + 1] == 0:
                if dy > 0 and graph[dx][dy - 1]:
                    continue
                # if N >= dx + 1 >= 1 == graph[dy][dx + 1]:
                #     continue

                graph[dx][dy] = 1
                backtracking(dx, dy + 2, depth + 1)
                graph[dx][dy] = 0


def check():
    for x in range(N):
        current = x
        for y in range(M):
            if graph[y][current] == 1:
                current += 1
            elif current > 0 and graph[y][current - 1] == 1:
                current -= 1
        if current != x:
            return False
    return True


N, H, M = map(int, sys.stdin.readline().split())
graph = [[0] * N for _ in range(M)]

for _ in range(H):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

answer = 4
backtracking(0, 0, 0)
print(answer if answer < 4 else -1)
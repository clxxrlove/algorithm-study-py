# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10 ** 7)

T = int(sys.stdin.readline().rstrip())


def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    else:
        return False


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    result = 0
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if dfs(j, i):
                result += 1

    print(result)
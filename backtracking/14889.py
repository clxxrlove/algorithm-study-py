# https://www.acmicpc.net/problem/15663
import sys

N = int(sys.stdin.readline().rstrip())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = float("inf")
not_visited = [i for i in range(0, N)]
visited = []


def sum_stat():
    vs = 0
    ls = 0
    link = list(set(not_visited) - set(visited))
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            vs += stats[visited[i]][visited[j]] + stats[visited[j]][visited[i]]

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            ls += stats[link[i]][link[j]] + stats[link[j]][link[i]]

    return abs(vs - ls)


def backtracking(depth, start):
    global result
    if depth == N // 2:
        s = sum_stat()
        result = min(result, s)
        return

    for i in range(start, N):
        if i not in visited:
            visited.append(i)
            backtracking(depth + 1, i + 1)
            visited.remove(i)


backtracking(0, 0)
print(result)
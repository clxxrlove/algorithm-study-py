import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
print(graph)
result = 0


def dfs(x, y):
    if x >= N or x <= -1 or y >= M or y <= -1:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    else:
        return False


for x in range(N):
    for y in range(M):
        if dfs(x, y):
            result += 1

print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000
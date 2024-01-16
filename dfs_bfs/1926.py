import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def dfs(x, y):
    length = 1
    visited[y][x] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                length += dfs(nx, ny)
    return length


ans = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            if not visited[i][j]:
                ans.append(dfs(j, i))

print(len(ans))
print(max(ans) if len(ans) > 0 else 0)
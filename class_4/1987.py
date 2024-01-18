import sys

M, N = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
ans = 1


def bfs(x, y):
    global ans
    q = {(x, y, graph[0][0])}

    while q:
        qx, qy, acc = q.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = qx + dx, qy + dy
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] not in acc:
                q.add((nx, ny, acc + graph[ny][nx]))
                ans = max(ans, len(acc) + 1)


bfs(0, 0)
print(ans)

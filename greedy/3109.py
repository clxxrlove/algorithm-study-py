import sys

R, C = map(int, sys.stdin.readline().split()) # y, x
_map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
count = 0


def dfs(x, y):
    if x == C - 1:
        return True

    for dx, dy in [(1, 1), (1, 0), (1, -1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx] and _map[ny][nx] != 'x':
            visited[ny][nx] = True
            if dfs(nx, ny):
                return True


for y in range(R - 1, -1, -1):
    if _map[y][0] != 'x' and dfs(0, y):
        count += 1

print(count)
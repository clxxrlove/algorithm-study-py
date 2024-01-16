import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, target):
    queue = deque([[start, 1]])
    visited[start] = True

    while queue:
        q, count = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                if i == target: return count
                visited[i] = True
                queue.append([i, count + 1])

    return -1


ans = bfs(a, b)
print(ans)
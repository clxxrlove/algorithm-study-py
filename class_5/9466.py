import sys


def dfs(n):
    global answer

    visited[n] = True
    cycle.append(n)

    if visited[S[n]]:
        if S[n] in cycle:
            answer -= len(cycle[cycle.index(S[n]):])
        return
    else:
        dfs(S[n])


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    S = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [False] * (N + 1)
    answer = N

    for i in range(1, N + 1):
        cycle = []
        if not visited[i]: dfs(i)

    print(answer)

import sys

N, M = map(int, sys.stdin.readline().split())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
house = []
chicken = []
result = []
ans = 1e9


def backtracking(length, depth):
    global result, ans
    if depth == M:
        dist = 0
        for h in house:
            tmp = 1e9
            for _len in range(M):
                tmp = min(tmp, abs(h[0] - result[_len][0]) + abs(h[1] - result[_len][1]))
            dist += tmp
        ans = min(ans, dist)
        return

    for i in range(length, len(chicken)):
        if chicken[i] not in result:
            result.append(chicken[i])
            backtracking(i + 1, depth + 1)
            result.pop()


for i in range(N): # y
    for j in range(N): # x
        if _map[i][j] == 1:
            house.append((j, i)) # x y
        elif _map[i][j] == 2:
            chicken.append((j, i))

backtracking(0, 0)
print(ans)

import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
ans = 0

plan = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    plan.append([a, b, c])

plan.sort(key=lambda x: x[1])

box = [C] * N
for p in plan:
    _min = C
    for i in range(p[0], p[1]):
        _min = min(_min, box[i])
    _min = min(_min, p[2])

    for i in range(p[0], p[1]):
        box[i] -= _min

    ans += _min

print(ans)
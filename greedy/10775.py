import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
airplanes = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
parent = list(range(N + 1))
count = 0


def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])

    return parent[a]


for airplane in airplanes:
    gate = parent[find_root(airplane)]
    if parent[gate] == 0:
        break
    parent[gate] -= 1
    count += 1

print(count)

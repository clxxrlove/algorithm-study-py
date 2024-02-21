import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

sensors = list(map(int, sys.stdin.readline().split()))
sensors.sort()

dist = []
for i in range(N - 1):
    dist.append(sensors[i + 1] - sensors[i])

dist.sort()
print(sum(dist[: N - K]))
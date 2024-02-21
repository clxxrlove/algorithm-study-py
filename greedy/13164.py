import sys

N, K = map(int, sys.stdin.readline().split())
kids = list(map(int, sys.stdin.readline().split()))

gaps = []
for i in range(1, N):
    gaps.append(kids[i] - kids[i - 1])

gaps.sort()
print(sum(gaps[:-K + 1] if K > 1 else gaps))
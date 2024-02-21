import sys

N = int(sys.stdin.readline().rstrip())
weights = list(map(int, sys.stdin.readline().split()))
weights.sort()
tmp = weights[0]

if tmp - 1 >= 1:
    print(1)
    exit()

for weight in weights[1:]:
    if weight > tmp + 1:
        break
    tmp += weight

print(tmp + 1)
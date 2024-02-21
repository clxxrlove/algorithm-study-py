import sys

H, W = map(int, sys.stdin.readline().split()) # y, x
blocks = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(1, W - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])
    refer = min(left, right)

    if blocks[i] < refer:
        ans += refer - blocks[i]

print(ans)
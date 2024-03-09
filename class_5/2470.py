import sys

N = int(sys.stdin.readline().rstrip())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

start, end = 0, N - 1
total = abs(liquids[start] + liquids[end])
answer = [liquids[start], liquids[end]]

while start < end:
    left = liquids[start]
    right = liquids[end]

    _sum = left + right

    if abs(_sum) < total:
        total = abs(_sum)
        answer[0], answer[1] = left, right
        if total == 0:
            break

    if _sum > 0:
        end -= 1
    else:
        start += 1

print(*answer)
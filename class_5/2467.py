import sys

N = int(sys.stdin.readline().rstrip())
liquids = list(map(int, sys.stdin.readline().rstrip().split()))
liquids.sort()
answer = 4e9
left, right = 0, 0

s, e = 0, N - 1

while e > s:
    tmp = liquids[s] + liquids[e]
    if answer > abs(tmp):
        answer = abs(tmp)
        left, right = liquids[s], liquids[e]

    if tmp == 0:
        break

    if tmp > 0:
        e -= 1
    else:
        s += 1

print(left, right)
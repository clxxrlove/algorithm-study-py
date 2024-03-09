import sys


def decimal(n):
    result = []
    arr = [i for i in range(N + 1)]

    for i in range(2, N + 1):
        if arr[i] == 0: continue

        for j in range(i * 2, N + 1, i):
            arr[j] = 0

    for i in range(2, N + 1):
        if arr[i] > 0:
            result.append(i)

    return result


N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(0)
    exit()

dec = decimal(N)

answer = 0
result = dec[0]
s, e = 0, 0

while s <= e:
    if result == N:
        answer += 1

    if result <= N:
        e += 1
        if e == len(dec):
            break
        result += dec[e]
    else:
        if s == len(dec):
            break
        s += 1
        result -= dec[s - 1]

print(answer)
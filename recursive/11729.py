import sys

N = int(sys.stdin.readline().rstrip())


def hanoi(n, start, end):
    if n == 0:
        return
    tmp = 6 - start - end

    hanoi(n - 1, start, tmp)
    print(start, end)
    hanoi(n - 1, tmp, end)


print(2 ** N - 1)
hanoi(N, 1, 3)
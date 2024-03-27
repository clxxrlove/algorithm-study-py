import sys
from itertools import permutations


def scoring(order):
    score = 0
    inning = 0
    out = 0
    b1, b2, b3 = [0, 0, 0]

    while True:
        for i in range(9):
            now = player[inning][order[i]]

            if now == 0:
                out += 1
                if out == 3:
                    out = 0
                    b1, b2, b3 = 0, 0, 0
                    inning += 1
                    if inning == N:
                        return score
            elif now == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif now == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif now == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0


def solution():
    answer = 0
    case = permutations(range(1, 9), 8)

    for c in case:
        c = list(c)
        c = c[:3] + [0] + c[3:]
        answer = max(answer, scoring(c))

    return answer


N = int(sys.stdin.readline().rstrip())
player = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution())
sys.stdin.close()

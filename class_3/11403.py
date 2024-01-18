# floyd-warshall
import sys

N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def floyd_warshall(_matrix, limit):
    for peek in range(limit):
        for i in range(limit):
            for j in range(limit):
                if i != j and _matrix[i][j] == 0 and _matrix[i][peek] + _matrix[peek][j] == 2:
                    _matrix[i][j] = 1


floyd_warshall(matrix, N)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == matrix[j][i] == 1:
            matrix[i][i] = 1

for m in matrix:
    print(*m)

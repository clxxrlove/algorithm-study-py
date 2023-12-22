# https://www.acmicpc.net/problem/1932
import sys

N = int(sys.stdin.readline().rstrip())
triangle = []

for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))

memo = [[0 for _ in range(N)] for _ in range(N)]
memo[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if memo[i][j] == 0:
            if j == 0:
                memo[i][j] = memo[i - 1][j] + triangle[i][j]
            elif j == i:
                memo[i][j] = memo[i - 1][j - 1] + triangle[i][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1]) + triangle[i][j]

print(max(memo[N - 1]))

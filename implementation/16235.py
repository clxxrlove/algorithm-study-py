# (r, c) -> (y, x)
# r번째 줄의 c번째 값은 A[r][c] y, x
# x, y, z -> y, x, z -> A[y][x]

# 구현 - 시뮬레이션
# 전제조건 - 기본 양분 = 5

# 1. (봄) 나무는 자신의 나이만큼 양분을 먹음
#  1.1. 양분은 어린 나무가 우선적으로 먹음
#  1.2. 양분을 못 먹는 나무는 그 즉시 사망

# 2. (여름) 죽은 나무는 양분이 됨
#  -> 자신의 나이 // 2 (소수점 이하 버림)

# 3. (가을) 나이가 5의 배수인 나무는 번식함
#  -> 대각선까지 8방향에 나이가 1인 나무를 심음

# 4. (겨울) 겨울에는 기계가 특정 위치의 땅에 양분을 심음..

import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # N * N
tree = [[[] * N for _ in range(N)] for _ in range(N)]
meal = [[5] * N for _ in range(N)]

for _ in range(M):
    y, x, z = map(int, sys.stdin.readline().split())
    tree[y - 1][x - 1].append(z)

for _ in range(K):
    baby = []
    # 1번
    for y in range(N):
        for x in range(N):
            if len(tree[y][x]) > 0: # 안에 나무가 있음
                tmp = []
                dead = []
                for t in sorted(tree[y][x]): # 1.1. 어린 애들부터 처리
                    if meal[y][x] >= t:
                        tmp.append(t + 1)
                        meal[y][x] -= t
                        if (t + 1) % 5 == 0:
                            baby.append((x, y))
                    else: # 1.2. 사망
                        dead.append(t)

                for d in dead:
                    meal[y][x] += d // 2

                tree[y][x] = tmp # 사후처리

    # 3번
    for bx, by in baby:
        for dx, dy in [(bx - 1, by - 1), (bx - 1, by), (bx - 1, by + 1), (bx, by - 1), (bx, by + 1), (bx + 1, by - 1), (bx + 1, by), (bx + 1, by + 1)]:
            if 0 <= dx < N and 0 <= dy < N:
                tree[dy][dx].append(1)

    # 4번
    for y in range(N):
        for x in range(N):
            meal[y][x] += A[y][x]

answer = 0
for y in range(N):
    for x in range(N):
        answer += len(tree[y][x])

print(answer)
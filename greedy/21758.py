import sys

N = int(sys.stdin.readline().rstrip())
honey = list(map(int, sys.stdin.readline().rstrip().split()))
_sum = honey[:]
answer = 0

for i in range(1, N): # 누적합
    _sum[i] += _sum[i - 1]

# 벌벌꿀
for i in range(1, N - 1):
    answer = max(answer, _sum[-1] * 2 - _sum[i] - honey[0] - honey[i])

# 벌꿀벌
for i in range(1, N - 1):
    answer = max(answer, _sum[i] + _sum[-1] - _sum[i - 1] - honey[0] - honey[-1])

# 꿀벌벌
for i in range(1, N - 1):
    answer = max(answer, _sum[-1] + _sum[i - 1] - honey[-1] - honey[i])

print(answer)
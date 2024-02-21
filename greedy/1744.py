import sys

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = 0

positive = filter(lambda x: x > 0, nums)
negative = filter(lambda x: x < 0, nums)
zero = list(filter(lambda x: x == 0, nums))

tmp = 0
for num in sorted(positive, reverse=True):
    if tmp == 0:
        tmp += num
        continue
    tmp = tmp * num if tmp * num > tmp + num else tmp + num
    ans, tmp = ans + tmp, 0

ans, tmp = ans + tmp, 0

for num in sorted(negative):
    if tmp == 0:
        tmp += num
        continue
    ans += tmp * num
    tmp = 0

if tmp < 0:
    if len(zero) == 0:
        ans += tmp

print(ans)
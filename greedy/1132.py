import sys

N = int(sys.stdin.readline().rstrip())
strs = []
nums = list(range(0, 10))
ans = 0

for _ in range(N):
    strs.append(sys.stdin.readline().rstrip())

chars = {}
zeros = []

for s in strs:
    length = len(s) - 1
    for char in s:
        if char not in chars:
            chars[char] = 10 ** length
        else:
            chars[char] += 10 ** length
        length -= 1
    zeros.append(s[0])

alphas = list(map(lambda x: x[0], sorted(chars.items(), key=lambda x: -x[1])))

if len(alphas) == 10:
    tmp = ''
    for alpha in alphas:
        if alpha not in zeros:
            tmp = alpha

    if tmp:
        alphas.remove(tmp)
        alphas.append(tmp)

for alpha in alphas:
    ans += chars[alpha] * nums.pop()

print(ans)
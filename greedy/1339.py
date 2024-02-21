import sys

N = int(sys.stdin.readline().rstrip())

nums = [i for i in range(0, 10)]
words = [sys.stdin.readline().rstrip() for _ in range(N)]

digits = dict()
ans = 0

for word in words:
    for char in word:
        if char not in digits:
            digits[char] = 0

for i in range(N):
    length = len(words[i])
    for j in range(length):
        digits[words[i][j]] += 10 ** (length - j - 1)

for item, value in sorted(digits.items(), key=lambda x: x[1], reverse=True):
    ans += value * nums.pop()

print(ans)
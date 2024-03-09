import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

d = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j - 1] == str2[i - 1]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

i, j = len(str2), len(str1)

length = d[i][j]
answer = ''

while True:
    if len(answer) == length:
        break

    if d[i][j] == d[i - 1][j]:
        i -= 1
    elif d[i][j] == d[i][j - 1]:
        j -= 1
    else:
        answer += str1[j - 1]
        i, j = i - 1, j - 1

print(length)
print(answer[::-1])
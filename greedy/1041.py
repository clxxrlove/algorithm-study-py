import sys

N = int(sys.stdin.readline().rstrip())
dices = list(map(int, sys.stdin.readline().split()))
faces = []
ans = 0

if N == 1:
    print(sum(dices) - max(dices))
    exit()

for i in range(3):
    faces.append(min(dices[i], dices[5 - i]))

faces.sort()

# 1면만 보이는 친구
ans += faces[0] * (4 * (N - 1) * (N - 2) + (N - 2) ** 2)
# 2면
ans += (faces[0] + faces[1]) * (4 * (2 * N - 3))
ans += sum(faces) * 4

print(ans)
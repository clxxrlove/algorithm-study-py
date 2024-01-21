import sys

N, M = map(int, sys.stdin.readline().split())
key = list(sys.stdin.readline().split())
key.sort()
ans = []


def backtracking(index, depth):
    if depth == N:
        vowel = 0
        consonant = 0
        for a in ans:
            if a in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                consonant += 1
        if 1 <= vowel and 2 <= consonant:
            print("".join(ans))
        return

    for i in range(index, M):
        ans.append(key[i])
        backtracking(i + 1, depth + 1)
        ans.pop()


backtracking(0, 0)
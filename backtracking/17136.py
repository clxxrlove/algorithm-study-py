import sys
N = 10
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sizes = [0, 0, 0, 0, 0, 0]
ans = float("inf")


def backtracking(count):
    global ans
    if count >= ans:
        return
    if check_paper():
        ans = min(ans, sum(sizes))
        return

    for i in range(N): # y
        for j in range(N): # x
            if not paper[j][i]:
                continue
            for size in range(5, 0, -1):
                if i + size > N or j + size > N:
                    continue
                if not check_size(j, i, size):
                    continue
                if sizes[size] >= 5:
                    continue
                fill(j, i, size)
                backtracking(count + 1)
                restore(j, i, size)
            return


def check_paper():
    for i in range(N):
        for j in range(N):
            if paper[i][j]:
                return False
    return True


def check_size(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if not paper[i][j]:
                return False
    return True


def fill(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = 0
    sizes[size] += 1


def restore(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = 1
    sizes[size] -= 1


backtracking(0)
print(ans if not ans == float("inf") else -1)
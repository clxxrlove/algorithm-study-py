import sys

T = int(sys.stdin.readline().rstrip())


def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)

    return parent[a]


def union(_a, _b, parent, friendCnt):
    a = find(_a, parent)
    b = find(_b, parent)

    if a != b:
        parent[a] = b
        friendCnt[b] += friendCnt[a]
    else:
        return


def check(_a, _b, parent):
    a = find(_a, parent)
    b = find(_b, parent)

    if a != b:
        return False
    return True


for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    parent = dict()
    friendCnt = dict()

    for i in range(1, F + 1):
        a, b = sys.stdin.readline().split()

        if a not in parent:
            parent[a] = a
            friendCnt[a] = 1
        if b not in parent:
            parent[b] = b
            friendCnt[b] = 1

        union(a, b, parent, friendCnt)
        print(friendCnt[find(a, parent)])
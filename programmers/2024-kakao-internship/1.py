def solution(friends, gifts):
    length = len(friends)
    answer = [0] * length
    graph = [[0] * length for _ in range(length)]
    gift_point = [0] * length
    friends = dict((friend, i) for i, friend in enumerate(friends))

    for gift in gifts:
        x, y = gift.split()
        gift_point[friends[x]] += 1
        gift_point[friends[y]] -= 1
        graph[friends[x]][friends[y]] += 1

    for i in range(length):
        for j in range(i + 1, length):
            if graph[i][j] > graph[j][i]:
                answer[i] += 1
            elif graph[i][j] < graph[j][i]:
                answer[j] += 1
            else:
                if gift_point[i] > gift_point[j]:
                    answer[i] += 1
                elif gift_point[i] < gift_point[j]:
                    answer[j] += 1

    return max(answer)


f = [["muzi", "ryan", "frodo", "neo"], ["joy", "brad", "alessandro", "conan", "david"], ["a", "b", "c"]]
g = [["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"], 	["a b", "b a", "c a", "a c", "a c", "c a"]]
r = [2, 4, 0]

for i in range(3):
    if r[i] != solution(f[i], g[i]):
        print("err")
        exit(0)

print("pass")
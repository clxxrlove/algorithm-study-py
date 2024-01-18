def solution(edges):
    answer = [0, 0, 0, 0]
    exchange = {}
    for a, b in edges:
        if a not in exchange:
            exchange[a] = [0, 0]
        if b not in exchange:
            exchange[b] = [0, 0]

        exchange[a][0] += 1
        exchange[b][1] += 1

    for edge, exchange_count in exchange.items():
        if exchange_count[0] >= 2 and exchange_count[1] == 0:
            answer[0] = edge
        elif exchange_count[0] == 0 and exchange_count[1] > 0:
            answer[2] += 1
        elif exchange_count[0] >= 2 and exchange_count[1] >= 2:
            answer[3] += 1
    answer[1] = exchange[answer[0]][0] - answer[2] - answer[3]
    return answer


e = [[[2, 3], [4, 3], [1, 1], [2, 1]], [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]]
r = [[2, 1, 1, 0], [4, 0, 1, 2]]

for i in range(2):
    if r[i] != solution(e[i]):
        print("err")
        exit(0)
print("pass")
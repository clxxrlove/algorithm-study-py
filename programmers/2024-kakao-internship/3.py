from itertools import combinations, product, permutations


def solution(dice):
    length = len(dice)
    comb = list(combinations(range(length), length // 2))
    wins = [0] * len(comb)

    for index, c in enumerate(comb):
        my_dice = []
        enemy_dice = []
        for i in range(length):
            if i in c:
                my_dice.append(dice[i])
            else:
                enemy_dice.append(dice[i])

        my_score = dict()
        enemy_score = dict()

        for my in list(map(sum, product(*my_dice))):
            if my not in my_score:
                my_score[my] = 1
            else:
                my_score[my] += 1

        for enemy in list(map(sum, product(*enemy_dice))):
            if enemy not in enemy_score:
                enemy_score[enemy] = 1
            else:
                enemy_score[enemy] += 1

        for my_result in my_score.items():
            for enemy_result in enemy_score.items():
                if my_result[0] > enemy_result[0]:
                    wins[index] += my_result[1] * enemy_result[1]

    ans = list(map(lambda x: x + 1, comb[wins.index(max(wins))]))
    return ans


d = [[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]], [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]], [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]]
r = [[1, 4], [2], [1, 3]]

for i in range(len(d)):
    if r[i] != solution(d[i]):
        print("err")
        exit(0)
print("pass")
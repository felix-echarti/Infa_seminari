from itertools import product


def maximize(lists, m):
    k = len(lists)
    sets = []
    for j in range(k):
        nums = map(int, lists[j])
        sets.append(set([(num ** 2) % m for num in nums]))
    print(sorted(sum(trial) % m for trial in product(*sets))[-1])


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
maximize(lists, m=1000)
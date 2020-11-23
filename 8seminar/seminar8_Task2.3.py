from itertools import combinations


def get_combinations(s, k):
    s = "".join(sorted(s))
    M = []
    for i in range(k):
        L = list(combinations(s, i + 1))
        for l in L:
            M.append(''.join(l))
    return M


print(get_combinations("cat", 2))


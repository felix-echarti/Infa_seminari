from itertools import combinations_with_replacement


def get_combinations_with_r(s,n):
    M = []
    combfile = list(combinations_with_replacement(s, n))
    for i in combfile:
        M.append(''.join(i))
    return sorted(M)


print(get_combinations_with_r("cat", 2))
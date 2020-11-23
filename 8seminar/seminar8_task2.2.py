from itertools import permutations


def get_permutations(s,n):
    return list(sorted(permutations(s, n)))


print(get_permutations("cat", 2))
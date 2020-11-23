from itertools import product


def cartesian_product(arr1, arr2):
    return list(product(arr1, arr2))


print(cartesian_product([1, 2], [3, 4]))
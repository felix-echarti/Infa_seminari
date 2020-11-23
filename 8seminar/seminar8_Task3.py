# Реализовать аналоги zip map enumerate
def analog_map(func, lst):
    M = []
    for i in range(len(lst)):
        M.append(func(lst))
    return M


def analog_zip(iterables):
    zipfile = []
    ito = []
    n = len(iterables[1])
    for i in range(iterables):
        if len(iterables[i]) < n:
            n = len(iterables[i])
    for i in range(n):
        for k in range(iterables):
            ito.append(iterables[k][i])
        zipfile.append(ito)
        ito = []
    return zipfile


def analog_enumerate(iterable, start):
    enfile = []
    for i in range(len(iterable)):
        singlefile = [start + i, iterable[i]]
        enfile.append(singlefile)
    return enfile




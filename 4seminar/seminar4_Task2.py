def even(numbers):
    n = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            n += 1
    return n


@even
def testone(n):
    if n == 0:
        print('Нет')
    else:
        testtwo()


@even
@testone
def testtwo(n):
    if n > 10:
        print('Очень много')
    else:
        print(n)
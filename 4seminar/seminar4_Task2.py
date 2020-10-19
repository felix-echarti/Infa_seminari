def decorator(function):
    def test(numbers):
        n = function(numbers)
        if n == 0:
            print('Нет')
        if n > 10:
            print('Очень много')
        return
    return test


@decorator
def even(numbers):
    n = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            n += 1
    print(n)
    return n


A = []
m = -1
while m != 0:
    m = int(input())
    A.append(m)
A.pop()


even(A)
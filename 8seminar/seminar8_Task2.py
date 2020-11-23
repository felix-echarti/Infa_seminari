def fib_gen(number):
    fib1, fib2 = 0, 1
    for i in range(number):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


for i in range(7):
    print(fib_gen(i))

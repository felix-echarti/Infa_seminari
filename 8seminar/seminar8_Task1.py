def nofor(function,  iterable):
    a = range(iterable)
    iterator = iter(a)
    while iterator != iterable:
        print(function(next(iterator)))
    return




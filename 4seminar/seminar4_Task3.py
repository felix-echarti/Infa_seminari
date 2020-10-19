def swap(the_function):
    def wrapper(x, y, show):
        the_function(y, x, show)
        return
    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)
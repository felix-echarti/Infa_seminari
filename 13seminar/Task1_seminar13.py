import pickle


def file_read():
    words = 'hello world'
    file = open('filetask1', 'wb')
    pickle.dump(words, file)
    file.close()
    file = open('filetask1', 'rb')
    obj = pickle.load(file)
    file.close()
    return obj


print('file =', file_read())


class A(object):

    def __init__(self, some_var, some_function):
        self.some_function = some_function
        self.x = self.some_function(some_var)


def some_function(x):
    return x*x


a = A(some_var=2, some_function=some_function)
file = open('filetask2', 'wb')
pickle.dump(a, file)
file.close()
file = open('filetask2', 'rb')
obj = pickle.load(file)
print(obj)
file.close()


bytes = pickle.dumps(print())
func = pickle.loads(bytes)
func('df')
# не работает для встроенных функций

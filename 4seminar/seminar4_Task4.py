import time


def decorator(random_function):
    def read_and_write(args, way):
        start_time = time.time()
        b = random_function(args)
        end_time = time.time()
        return_values = []*5
        return_values[0], return_values[1], return_values[3], return_values[4] = start_time, args, end_time, end_time - start_time
        if b == None:
            return_values[2] = '-'
        else:
            return_values[2] = args
        print(return_values)
        with open("'", way, "'", "w") as output:
            for i in range(5):
                output.write(return_values[i])
        return
    return read_and_write


@decorator
def random_function(args):
    #Write your function with the arguments args
    return #something

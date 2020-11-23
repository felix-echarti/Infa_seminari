from itertools import compress


def compress_string(s):
    i = 1
    a = []
    count = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
            i += 1
        else:
            a.append((count, int(s[i - 1])))
            i += 1
            count = 1
    a.append((count, int(s[i - 1])))
    return a


print(compress_string('1222311'))
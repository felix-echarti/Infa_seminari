import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.argv[1] = int(sys.argv[1])
        a = 0
        b = 1
        c = 1
        if sys.argv[1] < 3:
            if sys.argv[1] == 1:
                b = a
        else:
            for i in range(sys.argv[1]-2):
                c = b + a
                a = b
                b = c
        if len(sys.argv) == 2:
            print(sys.argv[1])
        else:
            if len(sys.argv) < 4:
                print("Error, type a name")
                sys.exit(1)

            if len(sys.argv) == 4 and sys.argv[2] == '-n':
                print('Fibonachi:', c, 'from', sys.argv[3])
    else:
        print('type something')
        sys.exit(1)

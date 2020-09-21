with open("write.txt", "w") as output:
    for i in range(3):
        output.write("lets go to sleep\n")


with open("write.txt", "r") as input:
    for line in input:
        print(line)

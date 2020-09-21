file = open("infa.txt", "r", encoding="utf8")
text = file.read()
text.split(' ')
print(text)
for line in text:
    print(line)
file.close()

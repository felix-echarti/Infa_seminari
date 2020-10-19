import shutil
import os


def write_array(array, file_name):
    for line in range(len(array)):
        file_name.write(array[line])
        file_name.write('\n')
    return


shutil.unpack_archive('C:/Users/Win10 Pro x64/Desktop/phystech/3semestr/3seminar/main.zip',
                      'C:/Users/Win10 Pro x64/Desktop/phystech/3semestr/3seminar', 'zip')
a = []
for dirpath, dirnames, filenames in os.walk('C:/Users/Win10 Pro x64/Desktop/phystech/3semestr/3seminar/main'):
    for dirname in dirnames:
        for filename in filenames:
            if filename.endswith('.py'):
                a.append(dirname)
a.sort()


with open("3task.txt", 'w') as input:
    write_array(a, input)
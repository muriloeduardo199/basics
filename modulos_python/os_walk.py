import os 
from itertools import count

caminho = os.path.join('/home', 'murilo', 'basics', 'classe')
counter = count()



for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter ,root)


    for dir_ in dirs:
        print('  ', the_counter, ' dir', dir_)


    for file_ in files:
        print('  ', the_counter, ' file', file_)
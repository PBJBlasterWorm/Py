from random import *

ar_list = []

for i in range(10):
    rd = randint(1,10)
    
    while rd in ar_list:
        rd = randint(1,10)
    
    ar_list.append(rd)
print(ar_list)
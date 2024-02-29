from random import *

print(random())     # 0.0 ~ 1.0 미만의 실수
print(random()*10)      # 0.0 ~ 10.0 미만의 실수
print(int(random()*10))     # 0 ~ 10 미만의 정수
print(int(random()*10)+1)       # 1 ~ 10 까지의 정수
print(randrange(1,10))      # 1 ~ 10 미만까지 정수
print(randint(1,10))      # 1~ 10 까지의 정수
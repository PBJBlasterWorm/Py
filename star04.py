for i in range(19,0,-2):
    print('{:^40}'.format('☆ '*i))
    
for i in range(3,19,2):
    print('{:^40}'.format('☆ '*i))
    
# ^:가운데를 기준으로 양넓이 정하는 코드
# ex) ^60이면 좌우 30칸의 공백이 주어진다
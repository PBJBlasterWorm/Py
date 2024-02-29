import random

num = range(1,46)
lotto = random.sample(range(1,46),6)

print(list(num))
print(lotto)

while True:
    
    inp = input("로또 구매건수(q입력시 종료) : ")
    
    if inp == "q":
        print("종료합니다.")
        break
    
    elif int(inp) <= 0:
        print("0보다 큰 숫자를 입력하시오.")
        continue
    
    
    cnt = int(inp)
    lotto_set = list()
    
    for i in range(cnt):
        num = random.sample(range(1,46),6)
        num.sort()
        lotto_set.append(num)

    lotto_set.sort()
        
    print(f"번호 갯수 : {cnt}개")
        
    for element in lotto_set:
        print(f"{element}")
        print(f"구매비용 : {cnt*1000}원")
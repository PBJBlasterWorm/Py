print("첫번째 숫자를 입력하시오 : ")
cnt = int(input())

#for x in range(1,10):
  #  print(cnt,"X",x,"=",(cnt*x))
#    print(f"{cnt} X {x} = {cnt*x}")
    
for x in range(cnt,10):
    for y in range(1,10):
        print(x,"X",y,"=",(x*y),'\t',end='')
        print('')
        
        for i in range(2,10):
            su = [i*x for x in range(1,10)]
            for j in range(1,10):
                print(f'{i:2d} X {j:2d} = {su[j-i]:2d}',end=' ')
# print 형식
# C언어 형
print("올해는 %d년 입니다." % 2024)
print("장래희망은 %s 입니다."% '지구정복')
print("%d년은 %s의 해 입니다"%(2024,'청룡'))
a = 2023
print("작년은 %d년 입니다."% a)

# format 형
print("가장 좋아하는 동물은 {}와, {}입니다.".format('강아지','고양이'))
print("가장 좋아하는 동물은 {0}와, {1}입니다.".format('강아지','고양이'))
print("가장 좋아하는 동물은 {1}와, {0}입니다.".format('강아지','고양이'))
print("가장 좋아하는 동물은 {am1}와, {am2}입니다.".format(am1='강아지',am2='고양이'))
animal1 = '호랑이'
animal2 = '사자'
print(f"1위 동물 : {animal1}, 2위 동물 : {animal2}")


str = "가나다라","마바사아"

print(str[1])
print(str[1][1])
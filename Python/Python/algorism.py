# def hap(S, n):
#     result = 0
#     for i in range(1, n):
#         result += S[i]
#     return result

# S = [7, -5, 11, 2, -1, 15, 9]
# sum1 = hap(S, len(S))
# print(sum1)

# 재귀 함수
def recursion(n):
    if n <= 0:
        print("히히 발싸~~~~~~~")
    else:
        print(n)
        recursion(n-1)
        
recursion(10)

# return값 (생각해보니 switch문이랑 뭐가 다른거지?)
def odd(n):
    n = 0
    if n % 2 == 0:
        return 0
    elif n == 11:
        return "니 엄마다"
    else:
        return 1
    
print(odd(11))

# 딕셔너리 구조
dict = {1: "하하하하핳하",
        2: "ㅈㄱㅊㅇ",
        3: "ㅁㄷㅊㅇ",
        4: "부모님이 사라지는 마술하나 보여줄까",
        5: "",
        "default": "ㅈㅈ"}
    
print(dict["default"])

# 재귀 함수 2
def countdown_num(n):
    if n <= 0:
        return 0
    
    else:
        print(n, "이 양수인 경우")
        result = countdown_num(n-1) + 1
        return result

print("반환값 : ", countdown_num(10))




        
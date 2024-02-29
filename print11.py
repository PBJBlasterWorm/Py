str_a = "son is best soccer player"
print(str_a.upper())    #대문자로
print(str_a.lower())    #소문자로

str_b = str_a.replace("soccer","football")
print(str_b)

print(str_b.index("football"))
print(str_b.find("football"))
print(str_b.find("FOOTBALL"))   # 검색되지 않을때 -1

print(str_a.count("o"))
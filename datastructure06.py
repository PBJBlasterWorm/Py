city = {'a':"서울",'b':"제주",3:"화성",4:"동탄",5:"병점"}
print(city)
print(city['b'])
print(city.get(4))
print(city.get(6))
print(city.get(3,"해당없음"))
print(city.get(6,"해당없음"))
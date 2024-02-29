for i in range(1,6):
    for j in range(0,i):
        print("☆",end=' ')
    print("")

#for i in range(6,11):
 #   for j in range(i):
  #      print("  "*5,end=" ")
   #     print("☆")
    
for i in range(5):
    print('{} '.format('  '*(4-i)),end="")
    print('{} '.format('☆ '*(i+1)))
    
#for i in range(5):
 #   print('{} '.format('  '*(i)),end="")
  #  print('{} '.format('☆ '*(5-i)))
    
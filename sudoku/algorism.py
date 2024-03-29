game = [[0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]
        [0,0,0,0,0,0,0,0,0]]

temp = [[] for i in range(81)]

def starttree(count): #트리형 구조
    if count == 81:
        return 7
    y0 = count // 9
    x0 = count % 9
    findpossibility(x0, y0)
    
    tt = 1
    while True:
        if tt == 7:
            return 7
        elif tt == 0:
            if temp[count - 1] != [0]:
                game[(count - 1) // 9][(count-1) % 9] = 0
                return 1
            else:
                return 0
            
        if temp[count] == []:
            tt = 0
            continue
        elif temp[count] != [0]:
            game[y0][x0] = temp[count][0]
            del temp[count][0]
        tt = starttree(count+1)
        if temp[count] == [0] and tt != 7:
            tt = 0
            
def findbase(location): # 기본 사각형 위치 초기화
    if location <= 2:
        return 0
    elif location > 2 and location <= 5:
        return 3
    else:
        return 6
    
def findpossibility(x1, y1): # 해당좌표 가능성 검사 
    ytemp = findbase(y1)
    xtemp = findbase(x1)
    temp[y1*9+x1] = []
    
    
    
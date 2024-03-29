import copy

start= '집'
end = '은행'
print ("-----------[", start, "->", end,"]----------")

landscape = {
    '집':             {'미용실':5, '슈퍼마켓':10, '학원':9},
    '미용실' :        {'집':5 ,'슈퍼마켓':3, '은행':11},
    '슈퍼마켓' :     {'미용실':3, '집':10, '학원':7, '레스토랑':3},
    '학원':          {'집':9, '슈퍼마켓':7, '학교':12},
    '레스토랑' :      {'슈퍼마켓':3, '은행':4},
    '은행' :            {'미용실':11, '레스토랑':4, '학원':7, '학교':2},
    '학교' :          {'은행':2, '학원':12}
    }

routing = {}
for place in landscape.keys():
    routing[place]={'shortestDist':0, 'route':[], 'visited':0}

def visitPlace(visit):
    routing[visit]['visited'] = 1
    for toGo, betweenDist in landscape[visit].items():
        toDist = routing[visit]['shortestDist'] + betweenDist
        if (routing[toGo]['shortestDist'] >= toDist) or  not routing[toGo]['route']:
            routing[toGo]['shortestDist'] = toDist
            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
            routing[toGo]['route'].append(visit)
            

            
visitPlace(start)

while 1 :
    minDist = max(routing.values(), key=lambda x:x['shortestDist'])['shortestDist']
    toVisit = ''
    for name, search in routing.items():
        if 0 < search['shortestDist'] <= minDist and not search['visited']:
            minDist = search['shortestDist']
            toVisit = name
    
    if toVisit == '':
        break
    
    visitPlace(toVisit)

    print ("["+toVisit+"]")
    print ("거리 :", minDist)

print ("\n", "[", start, "->", end,"]")
print ("Route : ", routing[end]['route'])
print ("ShortestDistance : ", routing[end]['shortestDist'])

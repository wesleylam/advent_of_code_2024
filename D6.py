import time
def deepCopy(dictOfLst):
    newDict = {}
    for i, lst in dictOfLst.items():
        newDict[i] = lst.copy()
        
    return newDict

def getAllTravelled(blockedI, blockedJ, startLoc, endI, endJ, exploreBlocked = False, 
                    direction = 0, ani = False):
    
    # direction = 0 # 0: north, 1: east, 2: south, 3: west 
    travelled = {(startLoc, direction)}
    
    newBlocked = set()
    
    while True:
        newLoc = moveUntilBlocked(startLoc, direction, blockedI, blockedJ, endI, endJ)
        
        if(startLoc != newLoc and (newLoc, direction) in travelled):
            return None, travelled
                
        for i in range(1, abs(newLoc[0] - startLoc[0]) + abs(newLoc[1] - startLoc[1]) + 1):
            tempLoc = move(startLoc, direction, i)
            travelled.add((tempLoc, direction))
            
            if (ani):
                printLoc(tempLoc, direction, blockedI, blockedJ)
            
            if exploreBlocked:
                blockedIcopy, blockedJcopy = blockedCopyWithExtra(blockedI, blockedJ, tempLoc)
                
                newDir = 0 if (direction == 4) else direction
                altTravelled = getAllTravelled(blockedIcopy, blockedJcopy, startLoc, endI, endJ, 
                                            direction=newDir)
                if type(altTravelled) == tuple and altTravelled[0] == None:
                    
                    # getAllTravelled(blockedIcopy, blockedJcopy, startLoc, endI, endJ, 
                    #                 direction=newDir, ani=True)
                    # print(" new BLOCKED added", tempLoc, newDir)
                    # input("WAITING INPUT")
                    assert tempLoc[1] not in blockedJ or tempLoc[0] not in blockedJ[tempLoc[1]], tempLoc
                    assert tempLoc[0] not in blockedI or tempLoc[1] not in blockedI[tempLoc[0]], tempLoc
                    newBlocked.add(tempLoc)
                # print()
            
        startLoc = newLoc
        direction += 1
        direction = 0 if direction == 4 else direction
        # print(travelled, direction)
        
        if startLoc[0] <= 0 or startLoc[0] >= endI \
            or startLoc[1] <= 0 or startLoc[1] >= endJ:
            break
    
    if (exploreBlocked):
        print("newBlocked", len(newBlocked))
    return travelled

    
def blockedCopyWithExtra(oriBlockedI, oriBlockedJ, newBlocked):
    putNewObstI, putNewObstJ = newBlocked
    blockedIcopy = deepCopy(oriBlockedI)
    blockedJcopy = deepCopy(oriBlockedJ)
    if putNewObstI not in blockedIcopy: 
        blockedIcopy[putNewObstI] = []
    if (putNewObstJ not in blockedIcopy[putNewObstI]):
        blockedIcopy[putNewObstI].append(putNewObstJ)
        blockedIcopy[putNewObstI].sort()
        
        if putNewObstJ not in blockedJcopy: 
            blockedJcopy[putNewObstJ] = []  
        assert (putNewObstI not in blockedJcopy[putNewObstJ])  
        blockedJcopy[putNewObstJ].append(putNewObstI)
        blockedJcopy[putNewObstJ].sort()
    else:
        assert (putNewObstJ in blockedIcopy[putNewObstI])
        
    return blockedIcopy, blockedJcopy
    
def move(startLoc, direction, step = 1):
    if direction % 4 == 0:
        return startLoc[0] - step, startLoc[1]
    if direction % 4 == 1:
        return startLoc[0], startLoc[1] + step
    if direction % 4 == 2:
        return startLoc[0] + step, startLoc[1]
    if direction % 4 == 3:
        return startLoc[0], startLoc[1] - step

def moveUntilBlocked(startLoc, direction, blockedI, blockedJ, endI, endJ):

    assert startLoc[0] not in blockedI or blockedI[startLoc[0]] == sorted(blockedI[startLoc[0]])
    assert startLoc[1] not in blockedJ or blockedJ[startLoc[1]] == sorted(blockedJ[startLoc[1]])
    
    if direction % 4 == 0:
        if startLoc[1] not in blockedJ:
            return 0 , startLoc[1]

        for k, i in enumerate(blockedJ[startLoc[1]][::-1]):
            if i < startLoc[0]:
                return i+1, startLoc[1]
            
        return 0, startLoc[1] 
                
    if direction % 4 == 1:
        if startLoc[0] not in blockedI:
            return startLoc[0], endJ

        for k, j in enumerate(blockedI[startLoc[0]]):
            if j > startLoc[1]:
                return startLoc[0], j-1
            
        return startLoc[0], endJ
            
    if direction % 4 == 2:
        if startLoc[1] not in blockedJ:
            return endI, startLoc[1]
            
        for k, i in enumerate(blockedJ[startLoc[1]]):
            if i > startLoc[0]:
                return i-1, startLoc[1]
            
        return endI, startLoc[1] 
    
    if direction % 4 == 3:
        if startLoc[0] not in blockedI:
            return startLoc[0], 0
            
        for k, j in enumerate(blockedI[startLoc[0]][::-1]):
            if j < startLoc[1]:
                return startLoc[0], j+1
            
        return startLoc[0], 0
    
    return 
       
def isBlocked(loc, blockedI, blockedJ):
    if loc[0] in blockedJ[loc[1]]:
        assert loc[1] in blockedI[loc[0]]
        return True
    
def printLoc(loc, direction, blockedI, blockedJ):
    mapStr = "\n\n"
    for i in range (loc[0]-9, loc[0] + 10):
        for j in range (loc[1]-50, loc[1] + 50):
            if (i, j) == loc:
                mapStr += '@'
            elif i < 0 or j < 0 or i > 129 or j > 129:
                mapStr += ' '
                
            elif isBlocked((i, j), blockedI, blockedJ):
                mapStr += '#'
            else:
                mapStr += '.'
        mapStr += "\n"
        
    print(mapStr, end='')
    time.sleep(0.01)
    
    
def part1(blockedI, blockedJ, startLoc, endI, endJ):
    travelled = getAllTravelled(blockedI, blockedJ, startLoc, endI, endJ, True)
    print(len({l for (l, d) in travelled})) 

def part2(blockedI, blockedJ, startLoc, endI, endJ):
    ## bruteforce
    looped = 0
    for i in range(endI + 1):
        for j in range(endJ + 1):
            # print(i, j)
            blockedIcopy, blockedJcopy = blockedCopyWithExtra(blockedI, blockedJ, (i, j))
            travelled = getAllTravelled(blockedIcopy, blockedJcopy, startLoc, endI, endJ, False)
            if type(travelled) == tuple and travelled[0] == None:
                looped += 1
    print("looped:", looped)

def main():
    # parse
    blockedI = {}
    blockedJ = {}
    with open("source/D6.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            blockedI[i] = []
            for j, c in enumerate(line):
                if c == "#":
                    if j not in blockedJ: blockedJ[j] = []
                    blockedI[i].append(j)
                    blockedJ[j].append(i)
                elif c == "^":
                    startLoc = (i, j)
            endJ = j        
        endI = i
    
    for col in blockedJ.values():
        col.sort()
    print(startLoc)
    print(endI, endJ)
                    
    part1(blockedI, blockedJ, startLoc, endI, endJ) # 4696
    part2(blockedI, blockedJ, startLoc, endI, endJ) # 1443

if __name__ == "__main__":
    main()
    
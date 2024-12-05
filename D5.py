def main():
    rulesEnd = False
    rules = []
    updates = []
    
    # parse
    with open("source/D5.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "": 
                rulesEnd = True
                continue
            
            if not rulesEnd:
                rules.append(line.split('|'))
            else:
                updates.append(line.split(','))
    # part1(rules, updates)
    part2(rules, updates)
    
def part1(rules, updates):
    sumMid = 0
    for update in updates:
        prohibitList = []
        valid = True
        for num in update:
            if num in prohibitList:  
                valid = False
                break
            else:
                prohibitList += findProhibit(num, rules)

        if valid:
            sumMid += int(update[int(len(update)/2-0.5)])
    
    print(sumMid)

def part2(rules, updates):
    sumMid = 0
    reorderedCount = 0
    for update in updates:
        reordered = recurSort(update, rules)
        if reordered != update:
            reorderedCount += 1
            sumMid += int(reordered[int(len(reordered)/2-0.5)])
    
    # print(len(updates))
    # print(reorderedCount)
    print(sumMid)
    
def findProhibit(num, rules):
    return [first for first, second in rules if second == num]

def recurSort(update, rules):
    if len(update) == 1:
        return update
    
    ps = findProhibit(update[0], rules)
    
    prohitSet = []
    normalSet = []
    for n in update[1:]:
        if n in ps:
            prohitSet.append(n)
        else:
            normalSet.append(n)
    if len(prohitSet) == 0:
        return [update[0]] + recurSort(update[1:], rules)
    return recurSort(prohitSet + [update[0]] + normalSet, rules)
    
if __name__ == "__main__":
    main()
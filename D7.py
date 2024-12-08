def calculate(numbers, result):
    if len(numbers) == 1:
        return numbers[0] == result
    
    ## assume + 
    return calculate(numbers[1:], result - numbers[0]) \
        or calculate(numbers[1:], result / numbers[0]) ## assume *
    
def calculateP2(numbers, result):
    if (int(result) != result):
        return False
    if len(numbers) == 1:
        return numbers[0] == result

    return calculateP2(numbers[1:], result - numbers[0]) \
        or calcP2ForConcat(numbers, result) \
            or calculateP2(numbers[1:], result / numbers[0]) ## assume *

def calcP2ForConcat(numbers, result): # calcP2ForConcat
    nStr = str(int(numbers[0]))
    resultStr = str(int(abs(result)))
    if (len(resultStr) <= len(nStr)) \
        or result < 0 \
        or resultStr[len(resultStr)-len(nStr):] != nStr:
        return False
    else: 
        return calculateP2(numbers[1:], int(resultStr[:-(len(nStr))]));
    
    
def calculateDebug(numbers, result):
    if (int(result) != result ):
        return False, "?"
    if len(numbers) == 1:
        return numbers[0] == result, f"{numbers[0]}"
    
    ## assume + 
    plusResult = calculateDebug(numbers[1:], result - numbers[0])
    pStr = f"{plusResult[1]} + {numbers[0]}"
    timesResult = calculateDebug(numbers[1:], result / numbers[0])
    tStr = f"{timesResult[1]} * {numbers[0]}"
    concatResult = calcP2ForConcatDebug(numbers, result)
    cStr = f"{concatResult[1]}{numbers[0]}"
    if (plusResult[0]):
        return True, pStr
    elif timesResult[0]: ## assume *
        return True, tStr
    elif concatResult[0]: ## assume ||
        return True, cStr
    else: 
        return False, f"{timesResult[1]} ? {numbers[0]}"

def calcP2ForConcatDebug(numbers, result): # calcP2ForConcat
    nStr = str(int(numbers[0]))
    resultStr = str(int(abs(result)))
    if (len(resultStr) <= len(nStr)) \
        or result < 0 \
        or resultStr[len(resultStr)-len(nStr):] != nStr:
        return False, f"?"
    else: 
        print(numbers, result)
        print(nStr, resultStr)
        print(int(resultStr[:-(len(nStr))]))
        return calculateDebug(numbers[1:], int(resultStr[:-(len(nStr))]))

def main():
    # parse
    lines = []
    with open("source/D7.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if line == "": continue
            tokens = line.split(": ")
            assert len(tokens) == 2
            lines.append(
                (
                    int(tokens[0]), 
                    [int(n) for n in tokens[1].split(' ')]
                )
            )
    test()
        
    numOfPossible = 0
    sumOfPossible = 0
    for (result, numbers) in lines:
        # possible = calculate(numbers[::-1], result)
        possible = calculateP2(numbers[::-1], result)
        # possible, p = calculateDebug(numbers[::-1], result)
        if (possible):
            numOfPossible += 1
            sumOfPossible += result
    print(numOfPossible, sumOfPossible)

def test():
    assert calculate([6,16,11,2][::-1], 35) # all + 
    assert calculate([6,16,11,2][::-1], 66)   # ++*
    assert calculate([6,16,11,2][::-1], 484)  # +**
    assert calculate([6,16,11,2][::-1], 214)  # *+*
    assert calculate([6,16,11,2][::-1], 244)  # +*+
    assert calculate([6,16,11,2][::-1], 1058) # **+
    assert calculate([6,16,11,2][::-1], 109)  # *++
    assert calculate([6,16,11,2][::-1], 2112) # all *
    
    assert calculate([6,16,11,2][::-1], 1058) # +**+
    assert calculate([6,16,11,2,3,2][::-1], 224)
    assert calculate([6,16,11,2,3,2,5][::-1], 229)
    
    assert calculateP2([6,8,6,15][::-1], 7290)
    assert calculateP2([17,8,14][::-1], 192)
    assert calculateP2([15,6][::-1], 156)
    

if __name__ == "__main__":
    main()
    
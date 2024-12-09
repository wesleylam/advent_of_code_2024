def main():
    # parse
    decoded = []
    fileChunks = [] 
    freeChunks = []
    line = ""
    with open("source/D9.txt", "r") as f:
        for l in f.readlines():
            l = l.strip()
            line = l
            
            i = 0 
            for j, c in enumerate(line):
                if j % 2 == 0: # mem block
                    decoded += [f"{i}"] * int(c)
                    fileChunks.append(int(c))
                    
                    i += 1
                else:
                    decoded += [f"."] * int(c)
                    freeChunks.append(int(c))
    part1(decoded)
    part2(fileChunks, freeChunks)

def part2(fileChunks, freeChunks):
    newInFree = {}
    for k, fileChunk in enumerate(fileChunks[::-1]):
        i = 0
        id = len(fileChunks) - 1 - k
        while i < id:
            if fileChunk <= freeChunks[i]:
                freeChunks[i] -= fileChunk
                
                if i not in newInFree: newInFree[i] = []
                newInFree[i].append((id, fileChunk))
                
                fileChunks[id] = -fileChunk
                break
            i += 1

    compress(fileChunks, freeChunks, newInFree)

def compress(fileChunks, freeChunks, newInFree):
    compressed = []
    for i in range(len(fileChunks)):
        if fileChunks[i] < 0:
            # print(fileChunks[i])
            compressed += ["."] * -fileChunks[i]
        else:
            compressed += [f"{i}"] * fileChunks[i]
        if i in newInFree:
            for (id, num) in newInFree[i]:
                compressed += [f"{id}"] * num
        if i < len(freeChunks):
            compressed += ["."] * freeChunks[i]
    
    # print(compressed)
    checksum(compressed)

def part1(decoded):
    ## compress
    k = len(decoded)
    for i in range(len(decoded)):
        if i >= k:
            break
        c = decoded[i]
        if c == '.':
            k -= 1
            while i < k and decoded[k] == '.':
                k -= 1
            decoded[i] = decoded[k]
            decoded[k] = '.'

    decoded = decoded[:k]
    # print("".join(decoded))
    checksum(decoded)
    
def checksum(decoded):
    ## checksum
    total = 0
    for i, c in enumerate(decoded):
        if c != '.':
            total += i * int(c)
    print(total)
    
if __name__ == "__main__":
    main()
    
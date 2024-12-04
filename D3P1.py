
if __name__ == "__main__":
    total = 0
    with open("source/D3.txt", "r") as f:
        for line in f.readlines():
            for i in range(len(line)):
                # print(i, end="")
                if line[i:i+4] == "mul(":
                    end = i + 14 if i + 14 < len(line) else len(line) - 1
                    search = line[i+4:end]
                    if ',' not in search or ')' not in search : # no comma
                        continue
                    else:
                        commaSplit = search.split(',')
                        bracketSplit = commaSplit[1].split(')')
                        if (commaSplit[0].isdigit() and bracketSplit[0].isdigit()):
                            total += int(commaSplit[0]) * int(bracketSplit[0])
                    
    print(total)
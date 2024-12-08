from itertools import combinations

def printGrid(grid, marked = []):
    for i, row in grid.items():
        s = "".join([('#' if (i, j) in marked else c) for j, c in row.items()])
        print(s)

def main():
    # parse
    grid = {}
    charSets = {}
    with open("source/D8.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            grid[i] = {}
            for j, c in enumerate(line):
                grid[i][j] = c
                if c == '.': # skip .
                    continue
                if c not in charSets:
                    charSets[c] = []
                charSets[c].append((i,j))
    
    highFreq = set()
    for c, locs in charSets.items():
        for l in locs:
            highFreq.add(l)
            
        for (i1, j1), (i2, j2) in combinations(locs, 2):
            iDiff = abs(i1 - i2)
            jDiff = abs(j1 - j2)
            
            multiplier = 0
            added = 1
            while added != 0:
                multiplier += 1
                if i1 > i2:
                    newI1 = i1 + iDiff * multiplier
                    newI2 = i2 - iDiff * multiplier
                else:
                    newI1 = i1 - iDiff * multiplier
                    newI2 = i2 + iDiff * multiplier
                if j1 > j2:
                    newJ1 = j1 + jDiff * multiplier
                    newJ2 = j2 - jDiff * multiplier
                else:
                    newJ1 = j1 - jDiff * multiplier
                    newJ2 = j2 + jDiff * multiplier
                    
                added = 0
                if not (newI1 < 0 or newI1 > i or newJ1 < 0 or newJ1 > j):
                    highFreq.add((newI1, newJ1))
                    added += 1
                if not (newI2 < 0 or newI2 > i or newJ2 < 0 or newJ2 > j):
                    highFreq.add((newI2, newJ2))
                    added += 1
            
    printGrid(grid, highFreq)
    print(len(highFreq))
    
if __name__ == "__main__":
    main()
    
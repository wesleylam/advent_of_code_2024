
def findpath(grid, loc, target, endI, endJ, found=[]):
    total = 0
    if target == 9:
        if type(found) != list or loc not in found:
            total += 1

    if type(found) == list: found.append(loc)
    # return if 9
    if total == 1:
        return total
    
    if loc[0] > 0: # top
        moved = (loc[0] - 1, loc[1])
        if (grid[moved] == target + 1): 
            total += findpath(grid, moved, target + 1, endI, endJ, found)
      
    if loc[0] < endI: # bottom
        moved = (loc[0] + 1, loc[1])
        if (grid[moved] == target + 1): 
            total += findpath(grid, moved, target + 1, endI, endJ, found)
      
    if loc[1] > 0: # left
        moved = (loc[0], loc[1] - 1)
        if (grid[moved] == target + 1): 
            total += findpath(grid, moved, target + 1, endI, endJ, found)
      
    if loc[1] < endJ: # right
        moved = (loc[0], loc[1] + 1)
        if (grid[moved] == target + 1): 
            total += findpath(grid, moved, target + 1, endI, endJ, found)
    
    return total

def main():
    # parse
    grid = {}
    zeros = []
    with open("source/D10.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            for j, c in enumerate(line):
                if c == '.':
                    c = '-1'
                if c == '0':
                    zeros.append((i, j))
                grid[(i,j)] = int(c)

    ## part 1
    print(sum([ findpath(grid, zero, 0, i, j, []) for zero in zeros ]))
    ## part 2
    print(sum([ findpath(grid, zero, 0, i, j, None) for zero in zeros ]))
    
if __name__ == "__main__":
    main()
    
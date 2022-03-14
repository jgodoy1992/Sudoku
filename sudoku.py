def findNextCelltofill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y]==0:
                return x,y

    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y]:
                return x,y

    return -1,1

def isValid(grid,i,j,e):
    rowOk=all([e!=grid[x][j] for x in range(9)])
    if rowOk:
        columnOk=all([e!=grid[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY=3*(i//3),3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y]==e:
                        return False
            return True
    return False

def solveSudoku(grid,i=0,j=0):
    i,j=findNextCelltofill(grid,i,j)
    if i==-1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j]=e
            if solveSudoku(grid,i,j):
                return True
            grid[i][j]=0
    return False
input = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]
print(solveSudoku(input))

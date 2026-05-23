class grid:
    def __init__(self,TheSudokuMatrix):
        self.TheSudokuMatrix = TheSudokuMatrix
    def validator(self,column,row,candidate):
            checker = True
            for x in range(0,9):
                if self.TheSudokuMatrix[row][x] == candidate or self.TheSudokuMatrix[x][column] == candidate:
                    checker = False
            boxcord = (3*(row // 3),3*(column // 3))   
            for y in range (0,3):
                for z in range(0,3):
                    if boxcord[0] + y == row and boxcord[1] + z == column:
                        pass
                    elif self.TheSudokuMatrix[boxcord[0] + y][boxcord[1] + z] == candidate:
                            checker = False  
            if checker:
                return checker
            else:
                return False
    def Solver(self):
        shouldwefalseit=True
        inputs = [1,2,3,4,5,6,7,8,9]
        #PossibleCords = []
        for p in range (0,9):
            for x in range (0,9):
                 
                if self.TheSudokuMatrix[p][x] == 0:
                    #doing work here instead of appending to the list
                    for o in inputs:
                        if self.validator(x,p,o):
                            self.TheSudokuMatrix[p][x] = o
                            if not self.Solver():
                                self.TheSudokuMatrix[p][x] = 0
                            else:
                                return True
                    return False                          
                  
                            
                               
gridz = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve = grid(gridz)
result = solve.Solver()
print(result)

        
        
        
        
        
        

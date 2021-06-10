def isValid(i,j,x,board):
    #check row
    for col in range(9):
        if board[i][col]==x:
            return False
    
    #check column
    for row in range(9):
        if board[row][j]==x:
            return False
    
    #check block
    startrow=i-i%3
    startcol=j-j%3
    
    p=startrow  
    while p<=startrow+2:
        l=startcol
        while l<=startcol+2:
            if board[p][l]==x:      
                return False
            l+=1
        p+=1
    
    return True
def solveSudokuHelper(i,j,board):
    if i==8 and j==8:
        if board[i][j]!=0:
            for row in board:
                for ele in row:
                    print(ele, end=" ")
                print()
        else:
            for x in range(1,10):
                if isValid(i,j,x,board) is True:
                    board[i][j]=x
                    for row in board:
                        for ele in row:
                            print(ele, end=" ")
                        print()
                    board[i][j]=0
        print()
        return
    
    if j>8:
        solveSudokuHelper(i+1,0,board)  
        return
    
    if board[i][j]==0:
        for x in range(1,10):
            if isValid(i,j,x,board) is True:
                board[i][j]=x
                solveSudokuHelper(i,j+1,board) 
                board[i][j]=0
    else:
        solveSudokuHelper(i,j+1,board)
    return
def solveSudoku(board):
    solveSudokuHelper(0,0,board)


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
solveSudoku(board)

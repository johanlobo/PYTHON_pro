sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def sud(sudoku,rno:int,cno:int,num:int):
    tr=rno-1                                 #use sudoku[row_index][col_index] = num directly
                                                 #dont complicate with loops

    tc=cno-1
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if i==tr and j==tc:             
                sudoku[i][j]=num
    return sudoku

gridnew=sud(sudoku,3,5,8)
gridnew=sud(sudoku,5,7,9)

for i in gridnew:
    print(i)

    
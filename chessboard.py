def chessboard(size):
    rowsize=0
    while rowsize<size:
        colsize=0
        while colsize<size:
            if (rowsize+colsize)%2==0:
                print("1",end="")
            else:
                print("0",end="")
            colsize+=1
        print()
        rowsize+=1

chessboard(6)
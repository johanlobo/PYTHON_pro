board={
     'tl':' ','tm':' ','tr':' ',
     'ml':' ','mm':' ','mr':' ',
     'bl':' ','bm':' ','br':' '
}
def printboard(board):
    print(board['tl']+'|'+board['tm']+'|'+board['tr'])
    print('-+-+-')
    print(board['ml']+'|'+board['mm']+'|'+board['mr'])
    print('-+-+-')
    print(board['bl']+'|'+board['bm']+'|'+board['br'])


turn='x'
for i in range(9):
    printboard(board)
    print(f'turn for {turn}. make your move!')
    move=input()
    board[move]=turn
    if turn=='x':
        turn='o'
    else:
        turn='x'

print('final board:')
printboard(board)
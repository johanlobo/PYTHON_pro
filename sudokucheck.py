def sud(m,row:int,col:int):
    emp=[]
    for i in range(row,row+3):
        for j in range(col,col+3):
            n=m[i][j]

            if n>0:
                if n in emp:
                    return False
                else:
                    emp.append(n)
    return True

m=[
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sud(m, 0, 0)) # Should print False (two 2s in the block)
print(sud(m, 1, 2)) # Should print True

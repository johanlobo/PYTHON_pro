l=[[1, 2, 1], [0, 3, 4], [1, 0, 0]]
def match(l,n):
    count=0
    for i in l:
         for j in i:
            if j==n:
                count+=1
    return count
print(match(l,1))

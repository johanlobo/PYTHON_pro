m=[
    [1,3,5],
    [5,8,12],
    [1,77,32]
]

def trans(m):
    tm=[]
    for i in range(len(m[0])):
        r=[]
        for j in range(len(m)):
            r.append(m[j][i])
        tm.append(r)
    
    return tm

c=trans(m)
for i in c:
   print(*i) #unpacking the list to print the elements without brackets and commas

print()

for i in c:
    print(i)
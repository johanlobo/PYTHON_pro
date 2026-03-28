def loy(pattern:str, size:int):
    r=0
    while r<size:
        c=0
        while c<size:
            print(pattern,end="")
            c+=1
        print()
        r+=1
p=input('enter a pattern:')
s=int(input('enter size:'))
loy(p,s)
print()
loy('o',18)
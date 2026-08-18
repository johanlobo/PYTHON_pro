def tria(pattern:str,rows:int):
    i=0
    while i<rows:
        j=0
        while j<=i:
            print(pattern,end='')
            j+=1
        print()
        i+=1

tria('%',5)

#recognize pattern

    
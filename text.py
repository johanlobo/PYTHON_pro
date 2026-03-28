def loy(text, size):

    i=0
    row=0
    while row<size:
        col=0
        while col<size:
            print(text[i],end="")
            i+=1

            if i==len(text):
                i=0
            col+=1
        print()
        row+=1

z=input('enter a string:')
y=int(input('enter size:'))
loy(z,y)

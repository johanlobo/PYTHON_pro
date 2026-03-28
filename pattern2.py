y=input('enter a string:')
if len(y)>0:
    print(y[0])
i=0
while i<=len(y)-1:
    if y[i]==" ":
        if(y[i+1]!=' '):
            print(y[i+1])
    i+=1
        
    
n=int(input('enter the upper limit:'))
b=int(input('enter the base:'))
i=1
while i<=n:
    print(i)
    i=i*b

#NOTE: (LEARNING POINT)
    #for i in range(1,n+1):
    #    print(i)
    #    i=i*b   
    #this would never give u the ans u want coz of the range() function. the op i=i*b is ignored. 
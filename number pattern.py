n=int(input('enter a number:'))
while n>0:
    i=0
    while i<=n:
        print(i, end=' ')
        i+=1
    print()
    n-=1

    #vertical(outer loop) horizontal(inner loop). remember the pattern
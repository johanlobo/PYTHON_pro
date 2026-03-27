n=int(input('enter the level of pyramid:'))
r='*'
while n>0:
    print(" "*n+r)
    r+='**'
    n-=1
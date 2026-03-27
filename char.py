c=input('enter:')
if len(c)==20:
    print(c)
else:
    stars='*'*(20-len(c))
    print(stars+c)
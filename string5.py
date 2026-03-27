z=input('type a word:')
t=input('please type a character:')
if t in z:
    i=z.find(t)
    y=t+z[i+1:i+3]
    print(y)
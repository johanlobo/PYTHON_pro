n=input("enter a string:")
c={}
for i in n:
    c.setdefault(i,0)
    c[i]+=1

for k,v in c.items():
    print(k,'and',v)
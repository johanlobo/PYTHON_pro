import pprint,operator

f=open('c:\\lobo.txt')
w=f.read().lower()
cont=w.split()
d={}
for i in cont:
    d.setdefault(i,0)
    d[i]+=1
pprint.pprint(d)

sort=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
pprint.pprint(sort)
for i in sort[:10]:
    print(i)

f.close()

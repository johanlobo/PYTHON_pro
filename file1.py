import pprint,operator
f=open(r'C:\Users\demo.txt')
content=f.read().lower()
w=content.split()
d={}
for i in w:
    d.setdefault(i,0)
    d[i]+=1
pprint.pprint(d)

sorted=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
pprint.pprint(sorted)
print('Descending order:')
for i in sorted:
    print(i)
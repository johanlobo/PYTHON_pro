with open(r'C:\Users\Juvie Leona\Documents\age.txt') as newfile:
   li=[]
   for i in newfile:
      s=i.replace('\n',"")
      w=s.split(";")
      li.append((w[0],int(w[1]),w[2]))
print('names:')
for p in li:
   print(p[0])

oldest=-1
name=''
for p in li:
   if p[1]>oldest:
      oldest=p[1]
      name=p[0]
print('oldest:',name,oldest)
with open(r'C:\Users\Juvie Leona\Documents\loy.txt') as newfile:
   count=0
   tl=0

   for i in newfile:
      s=i.replace('\n',"")
      count+=1
      print("line",count,s)
      l=len(s)
      tl+=l
print("total characters",tl)
list=[]
i=0
while True:

    
    print('the list is now', list)
    z=str(input('a(d)d, r(emove),  e(x)it:'))
    if z=='d':
      i+=1
                       #careful!!!
      list.append(i)
        
    elif z=='r':
        list.pop()
    elif z=='x':
        break
 
        

    

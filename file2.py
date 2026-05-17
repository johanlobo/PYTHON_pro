with open(r'C:\Users\Juvie Leona\Documents\loy.txt') as newfile:
    c=0
    tl=0

    for i in newfile:
        i =i.replace('\n','')
        c+=1
        print('line',c,i)
        l=len(i)
        tl+=l
    print('total lines:',c)
    print('total characters:',tl)
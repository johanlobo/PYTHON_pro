lst=[]
with open(r'C:\Users\Juvie Leona\Desktop\college\lobo.txt') as newfile:
    for i in newfile:
        w=i.split(';')
        if w[0]=='first':
            continue
        lst.append(w[1].strip())
        
print(lst)

#here strip function is used to remove the newline character at the end of the string.
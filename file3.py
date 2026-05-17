with open(r'C:\Users\Juvie Leona\Documents\grades.txt') as newfile:
    for i in newfile:
        i=i.replace('\n','')
        w=i.split(';')
        name=w[0]
        grades=w[1:]
        print(name+':')
        print(grades)
print()

grad={}
with open(r'C:\Users\Juvie Leona\Documents\grades.txt') as newfile:
    for i in newfile:
        i=i.replace('\n','')
        w=i.split(';')
        name=w[0]
        grad[name]=w[1:]


print(grad)
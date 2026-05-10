
#to remove the smallest element from the list and print the remaining list
u=[2,5,8,6,99,-34]
def sm(u):
    sml=u[0]
    for i in u:
        if i<sml:
            sml=i
    u.remove(sml)
    print(u)

sm(u)
print(u)



#to double the elements of the list and print the new list without changing the original list
m=[1,3,5,7]
def doub(m):
    nl=[]
    for i in m:
        if i in nl:
            continue
        else:
            nl.append(i*2)
    return nl   #can use print too
z=doub(m)
print(z)
print(m)


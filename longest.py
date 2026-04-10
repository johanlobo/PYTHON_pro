l=['loy','lobo','johan','juvieleona']
def longest(l:list):
    longest=''
    for i in range(len(l)):
        n=len(l[i])
        if n>len(longest):
            longest=l[i]
    return longest
print(longest(l))

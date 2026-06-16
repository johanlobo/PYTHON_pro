def divexp(a,b):

    assert a>0
    if b!=0:
     return a/b
    else:
       raise ZeroDivisionError("division by zero is not allowed")
    
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=divexp(a,b)
print(c)
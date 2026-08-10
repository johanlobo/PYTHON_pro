class loy:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
#class lobo:
def hello(abc:loy,newname:str):  #this is a concept of passing objects as parameters(args) to a function.
    abc.name=newname             #if this func is inside a class(lobo) then its called objects as parameters(args)to METHODS

L1=loy('day')
print(L1)
hello(L1, 'night')  #either give the name here or in the function itself but
                    #the object must be specified in the function parameter. 
print(L1)

L2=loy('day')
print(L2)
hello(L2,'fight')
print(L2)
print(L1)     #so one object wont affect the other object. Each object is independent of each other.


#OR,

#def hello(abc:loy)
  #  abc.name='night'

#in main function,

#L1=loy('day')
#print(L1)
#hello(L1)
#print(L1)     will print day and then 'night'.



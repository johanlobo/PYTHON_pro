from random import randint,choice

class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def __str__(self):
        return f'{self.name} ({self.id})'

def identity():
    names=['ricky','virat','mahendra','rohit','kapil','ravindra']
    sirname=['ponting','kohli','singh','sharma','jadeja']

    newname= choice(names)+' '+choice(sirname)
    stuid=str(randint(2221,9999))

    return student(newname,stuid) # ->concept:#It is also possible to create objects within functions.
                                  #  If a function returns a reference to the newly created object,
                                  #  it is also accessible within the main function:
loy=[]
for i in range(6):
    loy.append(identity())

for i in loy:
    print(i)








    
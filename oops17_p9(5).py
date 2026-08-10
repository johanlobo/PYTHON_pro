class old:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def older(self,p1:'old'): # here is a v.imp concept of instances. if class used within same class,
                              # then enclose it in quotations. 
                              # here function is inside class
        if self.age>p1.age:
            return True

muhammad=old('muhammad',45)
ramanand=old('ramanand',72)

if muhammad.older(ramanand):
    print (f'{muhammad.name} is older')
else:
    print(f'{ramanand.name} is older')

print()

#example 2:
class Person:
    def __init__(self, name: str, year_of_birth: int):
        self.name = name
        self.year_of_birth = year_of_birth

def older_than(person1: Person, person2: Person):
    if person1.year_of_birth < person2.year_of_birth:     #here function is outside class so no quotations required.
        return True
    else:
        return False

muhammad = Person("Muhammad ibn Musa al-Khwarizmi", 780)
pascal = Person("Blaise Pascal", 1623)
grace = Person("Grace Hopper", 1906)

if older_than(muhammad, pascal):
    print(f"{muhammad.name} is older than {pascal.name}")
else:
    print(f"{muhammad.name} is not older than {pascal.name}")

if older_than(grace, pascal):
    print(f"{grace.name} is older than {pascal.name}")
else:
    print(f"{grace.name} is not older than {pascal.name}")


        
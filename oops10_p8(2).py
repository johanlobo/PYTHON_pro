from datetime import date

class persoon:

    def __init__(self,name:str,day:int,month:int,year:int,points:int):
        self.name=name
        self.date=date(year,month,day)
        self.points=0

        if self.nok(name):
            self.name=name

        if self.isdate(day,month,year):
            self.date=date(year,month,day)

        if self.pp(points):
            self.points=points

    def __str__(self):
        return f'{self.name}, {self.date}, {self.points}'


    def nok(self,name:str):
        return len(name)>=3

    def isdate(self,day,month,year):
        try:
            date(year,month,day)
            return True
        except ValueError:
            return False

    def pp(self,points):
        return points>=0


loy=persoon('loy',2,6,2007,2536)

print(loy)
print(loy.date)
print(loy.points)

#using conditions in the constructor to check if input data is correct using different methods.
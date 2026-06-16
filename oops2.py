import copy
class movie:
    def __init__(self,title,year,actors):
        self.title=title
        self.year=year
        self.actors=actors
    def display(self):
        print('title:',self.title)
        print('year:',self.year)
        print('actors:',self.actors)

movie1=movie('JAWAN',2023,['Shah Rukh Khan','Nayanthara','Vijay Sethupathi'])
movie2=copy.copy(movie1)
movie3=copy.deepcopy(movie1)

movie1.display()
print()

movie2.actors.append('deepika padukone')
print('original:')
movie1.display()

print('after shallow copy:')
movie2.display()

movie3.actors.append('sanya malhotra')
print('original:')
movie1.display()
print('after deep copy:')
movie3.display()


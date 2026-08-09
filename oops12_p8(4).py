class mov:
    total=0
    count=0
    avg=0
    def __init__(self,name:str,seasons:int,genre:list):
        self.name=name
        self.seasons=seasons
        self.genre=genre

    def __str__(self):
        return f'{self.name} ({self.seasons})\ngenres:{','.join(self.genre)}\naverage rating:{self.avg:.1f}'

    def rate(self,num:int):
        self.total+=num
        self.count+=1
        self.avg=self.total/self.count

#def min(num:int,series:list):
        
      # for i in series:               #The return statement absolutely does not care if it is inside a for loop, a while loop, or ten nested loops. The exact microsecond Python executes a return line, the function is done and dusted.
       #    if i.avg>=num:
       #       return i.name
       #return None

#def includesgenre(genre:str,series:list):
     
    #for i in series:
      #   if genre in i.genre:
       #       return i.name
    #return None

def min(num: float, series: list):
    result = []
    for i in series:
        if i.avg >= num:
            result.append(i.name)
    return result


def includesgenre(genre: str, series: list):
    result = []
    for i in series:
        if genre in i.genre:
            result.append(i.name)
    return result

watch=mov("Breaking Bad", 5, ["Crime", "Drama",'thriller'])
print(watch)
watch.rate(8)
watch.rate(6)
watch.rate(9)
print()
print(watch)

s1 = mov("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = mov("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = mov("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

s4= mov("The Office", 9, ["Comedy"])
s4.rate(5)

serieslist=[s1,s2,s3,s4]
print()
print("a minimum grade of 4.5:")
for i in min(4.5,serieslist):
     print(i)
print()
print("genre Comedy:")
for i in includesgenre("Comedy",serieslist):
     print(i)
print()


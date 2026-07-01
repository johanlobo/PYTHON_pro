class book:
    def __init__(self,name:str,author,genre,year):
        self.name=name
        self.author=author
        self.genre=genre
        self.year=year

def comp(book1:book,book2:book):
    if book1.year> book2.year:
        print(f"{book1.name}-{book1.year} is newer than {book2.name}-{book2.year}.")
    elif book1.year< book2.year:
        print(f"{book2.name}-{book2.year} is newer than {book1.name}-{book1.year}.")
    else:
        print(f"{book1.name}-{book1.year} and {book2.name}-{book2.year} are of the same year.")

def genre(book:list,genre:str):
    for i in book:
        if i.genre==genre:
            yield i   

python = book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = book("Norma", "Sofi Oksanen", "crime", 2015)
fuji=book("Fuji", "Yukio Mishima", "crime", 1962)
books=[python,everest,norma,fuji]

for i in genre(books,"crime"):
    print(f"{i.name} is a {i.genre} book.")

#learnt abt yield

#or use:
#def genre(book:list,genre:str):
#  gen=[]
#  for i in book:
#    if i.genre==genre:
#      gen.append(i)
#  return gen
     

#for i in genre(books,"crime"):
#    print(f"{i.name} is a {i.genre} book.")

#remember that in this for loop the output of genre is evaluated first and then a loop is run through its result.




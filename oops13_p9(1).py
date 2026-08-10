class voc:
    def __init__(self):
        self.store=[]

    def add(self, word:str): 
        self.store.append(word)

    def lon(self):
        longest=''      #OR self.longest
        lengthlong=0    #OR self.lengthlong

        for i in self.store:
            if len(i)>lengthlong:
                lengthlong=len(i)
                longest=i
        return longest


loy=voc()
loy.add('goodmorning_pineapple_looking_very_good_very_nice!')
loy.add('johaaann')
loy.add('twinkle twinkle')
print(loy.lon())

# this is a concept of self and no self. its always better to reduce as much self as possible to avoid confusion.
# here self isnt used for longest and lengthlong because they are not attributes of the class,
# they are just variables used in the method. anyhow, using self on these also would work
# but it is not a good practice to use self for variables that are not attributes of the class.
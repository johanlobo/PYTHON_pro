class rec:
    def __init__(self,lu:tuple,rb:tuple):
        self.lu=lu
        self.rb=rb
        self.width=lu[0]-rb[0]
        self.height=abs(rb[1]-lu[1])

    def area(self):
        return abs(self.width*self.height)
    def perimeter(self):
        return abs(2*(self.width+self.height))
    
    def move(self,c:tuple,d:tuple):
        self.lu= (self.lu[0]+c[0], self.lu[1]+c[1])
        self.rb= (self.rb[0]+d[0], self.rb[1]+d[1])
        return
    

m=rec((4,6),(8,3))
print(m.lu)
print(m.rb)
print('area is:',m.area())
print('perimeter is:',m.perimeter())



m.move((5,8),(2,4))
print('after moving:','left upper:',m.lu,'\nright bottom:',m.rb)
 
#important to understand graphs in machine learning and computer vision wrt how we can move the points of a closed area
#also note that here the input values wrt rectangle on a coordinate plane may be wrong. its randomly given.
#so, the x axis increases as in normal math
#but y axis is inverted as in computer graphics.
#which means, closer the y point is to the x axis, higher is the value of y and vice versa.

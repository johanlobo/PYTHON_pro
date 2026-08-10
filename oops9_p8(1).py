class dec:
    def __init__(self,num):
        self.num=num
        self.v=num

    def disp(self):
        print(self.num)

    def decrease(self):
        self.num-=1

    def set(self):
        self.num=0

    def res(self):
        self.num=self.v


loy=dec(5)
loy.disp()
loy.decrease()
loy.decrease()
loy.disp()
loy.set()
loy.disp()
loy.res()
loy.disp()
print()
loy=dec(40)
loy.disp()
loy.decrease()
loy.disp()
loy.res()
loy.disp()



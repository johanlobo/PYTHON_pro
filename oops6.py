class sho:
    def __init__(self):
        self.products=[]
    
    def nofi(self):
        return len(self.products)
    def add(self,product,num:int):
       self.products.append((product,num))

    def amount(self,n:int):
        return self.products[n-1][1]
    
mysho=sho()

def totalamount(mysho):
    total=0
    for i in range(0,mysho.nofi()):
        total+=mysho.amount(i)
    return total

mysho.add('apple',5)
mysho.add('banana',10)
print('total amount:',totalamount(mysho))



    
         
    
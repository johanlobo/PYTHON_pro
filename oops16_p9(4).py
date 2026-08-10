class lunch:
    def __init__(self,balance:float):
        self.balance=balance

    def deposit(self,amt:float):
        self.balance+=amt

    def withdraw(self,amount:float):
        if amount>self.balance:
            return 'not enough balance to withdraw'
        else:
            self.balance-=amount

    def __str__(self):
        return str(self.balance)


class terminal:
    def __init__(self):
        self.amount=2000
        self.lunchspecial=0
        self.eatlunch=0

    def eatlunch1(self,amt:float):  
        if amt<2.50:
            return amt
        elif amt>=2.50:
            z=amt-2.50
            self.amount+=2.50
            self.eatlunch+=1
        return f'{z:.2f}'
    
    def lunchspecial1(self,amt:float):     
        if amt<4.50:
            return amt
        elif amt>=4.50:
            z=(amt-4.50)
            self.amount+=4.50
            self.lunchspecial+=1
        return f'{z:.2f}'

    def eatlunchcard(self,card:lunch):
        if card.balance<2.50:
            return 'insufficient balance'
        elif card.balance>=2.50:
            card.balance-=2.50
            self.eatlunch+=1
            return 'payment successful'

    def eatspecialcard(self,card:lunch):
        if card.balance<4.50:
            return 'insufficient balance'
        elif card.balance>=4.50:
              card.balance-=4.50
              self.lunchspecial+=1
              return 'payment successful'

    def depositmoney(self,loy:lunch,amt:float):
        loy.balance+=amt
        self.amount+=amt  #giving cash to cashier to top up money on lunchcard.

    

juvie=lunch(1000)

lobo=terminal()
print(lobo.eatlunch1(3.5))
print(lobo.eatspecialcard(juvie))
print(lobo.lunchspecial1(5.22))
print(lobo.lunchspecial1(112.457))
print('only lunch:',lobo.eatlunch)
print('special lunch:',lobo.lunchspecial)
print(juvie.balance)
lobo.depositmoney(juvie,4.55)
print(juvie.balance)


        
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        rp=self.real+other.real
        ip=self.imag+other.imag
        return complex(rp,ip)
    
    def __str__(self):
        return str(self.real)+'+'+str(self.imag)+'i'
    
    n=int(input('enter the no.of complex numbers:'))
    total=complex(0,0)
    for i in range(n):
        r=int(input('enter the real part:'))
        im=int(input('enter the imaginary part:'))
        c=complex(r,im)
        total=total+c
    print('The sum of the complex numbers is:', total)
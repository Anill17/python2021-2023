class cmplx(object):
    def __init__(self,real,imag):
        self.real = real 
        self.imag = imag

    def __add__(self,other):
        return cmplx(self.real + other.real, self.imag + other.imag)
    def __mult__(self,other):
        return cmplx(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)
    def terminate(self):
        if self.real == 0 and self.imag == 0:
            return -1 
    
n1 = cmplx(1,2)
n2 = cmplx(2,3)

print(n1+n2)
        
    

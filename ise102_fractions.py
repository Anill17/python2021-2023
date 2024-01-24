def gcd(a,b):
    if b == 0:
        return a 
    else:
        return gcd(b,a%b)

class fractions(object):
    def __init__(self,num,denum):
        self.num = num // gcd(num,denum)
        self.denum = abs(denum // gcd(denum,num))
        

    def __str__(self):
        return "{} / {}".format(self.num, self.denum)
    
    def __add__(self,other):
        num =self.num * other.denum + other.num * self.denum
        denum = self.denum  * other.denum
        return fractions(num, denum)
    
    def __sub__(self,other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        return fractions(num, denum)
    
    def __float__(self):
        return self.num / self.denum
    
    def inverse(self):
        return fractions(self.denum, self.num)
    
    

n1 = fractions(2,5)
n2 = fractions(3,5)
print(n1+n2)
print(n2-n1)
n3 = n1+n2
print(float(n3))

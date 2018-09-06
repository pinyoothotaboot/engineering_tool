
class Convert:

    def __init__(self,n):
        if type(n) not in [int,float]:
            raise TypeError("The value must be a non-negative real number.")
        elif n<0:
            raise ValueError("The value cannot be negative.")
        else:
            self.n = n

    def ToPico(self):
        return self.n * 1000000000000
    
    def ToNano(self):
        return self.n * 1000000000
    
    def ToMicro(self):
        return self.n * 1000000
    
    def ToMilli(self):
        return self.n * 1000
    
    def ToCentri(self):
        return self.n * 100
    
    def ToDeci(self):
        return self.n * 10
    
    def ToUnit(self):
        return self.n
    
    def ToDeca(self):
        return self.n * (1/10)
    
    def ToHecto(self):
        return self.n * (1/100)
    
    def ToKilo(self):
        return self.n * (1/1000)
    
    def ToMega(self):
        return self.n * (1/1000000)
    
    def ToGiga(self):
        return self.n * (1/1000000000)
    
    def ToTera(self):
        return self.n * (1/1000000000000)

class Unit:

    def __init__(self,n):
        if type(n) not in [int,float]:
            raise TypeError("The value must be a non-negative real number.")
        elif n<0:
            raise ValueError("The value cannot be negative.")
        else:
            self.n = n
    
    def CentrimetreToInch(self):
        return Convert(self.n * 0.393701)
    
    def CentrimetreToFoot(self):
        return Convert(self.n * 0.0328084)
    
    def CentrimetreToYard(self):
        return Convert(self.n * 0.010936133333333)
    
    def InchToCentrimetre(self):
        return Convert(self.n / 0.393701)





    


    
    

    
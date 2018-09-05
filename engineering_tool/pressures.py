import math

a = 100000
b = 101325
c = 760
d = 13.5951
e = 9.80665
g = 9.8   #m/s^2

class Pressure:
    
    """
        Function    : BarToPascal
        Description : This function to convert pressure from Bar to Pascal.
        Formula     : bar x 100000
        Input       : 
                      - Bar number type integer or float
        Return      : Pressure pascal in type interger or float
        Example     : BarToPascal(1)
                    >> 1000000
    """
    def BarToPascal(bar):
        if type(bar) not in [int,float]:
            raise TypeError("The Bar must be a non-negative real number.")
        
        return bar * a
    
    """
        Function    : AtmToPascal
        Description : This function to convert pressure from ATM to Pascal.
        Formula     : atm x 101325
        Input       : 
                      - ATM number type integer or float
        Return      : Pressure pascal in type interger or float
        Example     : AtmToPascal(1)
                    >> 101325
    """
    def AtmToPascal(atm):
        if type(atm) not in [int,float]:
            raise TypeError("The ATM must be a non-negative real number.")

        return atm * b
    
    """
        Function    : TorrToPascal
        Description : This function to convert pressure from Torr to Pascal.
        Formula     : torr x ( 101325 / 760 )
        Input       : 
                      - Torr number type integer or float
        Return      : Pressure pascal in type interger or float
        Example     : TorrToPascal(1)
                    >> 133.322
    """
    def TorrToPascal(torr):
        if type(torr) not in [int,float]:
            raise TypeError("The Torr must be a non-negative real number.")

        return torr * (b/c)
    
    """
        Function    : mmHgToPascal
        Description : This function to convert pressure from mmHg to Pascal.
        Formula     : mmHg x 13.5952 x 9.80665
        Input       : 
                      - mmHg number type integer or float
        Return      : Pressure pascal in type interger or float
        Example     : mmHgToPascal(1)
                    >> 133.32
    """
    def mmHgToPascal(mmHg):
        if type(mmHg) not in [int,float]:
            raise TypeError("The mmHg must be a non-negative real number.")

        return mmHg * d * e
    
    """
        Function    : PascalToBar
        Description : This function to convert pressure from Pascal to Bar.
        Formula     : pascal x (1/100000)
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure bar in type interger or float
        Example     : PascalToBar(1)
                    >> 0.000001
    """
    def PascalToBar(pascal):
        if type(pascal) not in [int,float]:
            raise TypeError("The Pascal must be a non-negative real number.")

        return pascal * (1 / a)
    
    """
        Function    : AtmToBar
        Description : This function to convert pressure from ATM to Bar.
        Formula     : atm x (101325/100000)
        Input       : 
                      - ATM number type integer or float
        Return      : Pressure bar in type interger or float
        Example     : AtmToBar(1)
                    >> 1.01325
    """
    def AtmToBar(atm):
        if type(atm) not in [int,float]:
            raise TypeError("The ATM must be a non-negative real number.")

        return atm * ( b/a )
    
    """
        Function    : TorrToBar
        Description : This function to convert pressure from Torr to Bar.
        Formula     : torr x ( 101325 / ( 100000 x 760 ))
        Input       : 
                      - Torr number type integer or float
        Return      : Pressure bar in type interger or float
        Example     : TorrToBar(1)
                    >> 0.00133322
    """
    def TorrToBar(torr):
        if type(torr) not in [int,float]:
            raise TypeError("The Torr must be a non-negative real number.")

        return torr * (b/(a*c))

    """
        Function    : mmHgToBar
        Description : This function to convert pressure from mmHg to Bar.
        Formula     : mmHg x (( 13.5951 x 9.80665 ) / 100000 )
        Input       : 
                      - mmHg number type integer or float
        Return      : Pressure bar in type interger or float
        Example     : mmHgToBar(1)
                    >> 0.00133322
    """
    def mmHgToBar(mmHg):
        if type(mmHg) not in [int,float]:
            raise TypeError("The mmHg must be a non-negative real number.")

        return mmHg * ((d*e)/a)
    
    """
        Function    : PascalToAtm
        Description : This function to convert pressure from Pascal to ATM.
        Formula     : pacal x ( 1 / 101325 )
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure ATM in type interger or float
        Example     : PascalToAtm(1)
                    >> 0.00000987
    """
    def PascalToAtm(pascal):
        if type(pascal) not in [int,float]:
            raise TypeError("The Pascal must be a non-negative real number.")

        return pascal * (1/b)
    
    """
        Function    : BarToAtm
        Description : This function to convert pressure from Bar to ATM.
        Formula     : bar x ( 100000 / 101325 )
        Input       : 
                      - Bar number type integer or float
        Return      : Pressure ATM in type interger or float
        Example     : BarToAtm(1)
                    >> 0.9869
    """
    def BarToAtm(bar):
        if type(bar) not in [int,float]:
            raise TypeError("The Bar must be a non-negative real number.")

        return bar * (a/b)
    
    """
        Function    : TorrToAtm
        Description : This function to convert pressure from Torr to ATM.
        Formula     : torr x ( 1 / 760 )
        Input       : 
                      - Torr number type integer or float
        Return      : Pressure ATM in type interger or float
        Example     : TorrToAtm(760)
                    >> 1
    """
    def TorrToAtm(torr):
        if type(torr) not in [int,float]:
            raise TypeError("The Torr must be a non-negative real number.")

        return torr * (1/c)

    """
        Function    : mmHgToAtm
        Description : This function to convert pressure from mmHg to ATM.
        Formula     : mmHg x (( 13.5951 x 9.80665) / 101325)
        Input       : 
                      - mmHg number type integer or float
        Return      : Pressure ATM in type interger or float
        Example     : mmHgToAtm(0)
                    >> 0
    """
    def mmHgToAtm(mmHg):
        if type(mmHg) not in [int,float]:
            raise TypeError("The mmHg must be a non-negative real number.")

        return mmHg * ((d*e)/b)
    
    """
        Function    : PascalToTorr
        Description : This function to convert pressure from Pascal to Torr.
        Formula     : pascal x ( 760 / 101325)
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure Torr in type interger or float
        Example     : PascalToTorr(0)
                    >> 0
    """
    def PascalToTorr(pascal):
        if type(pascal) not in [int,float]:
            raise TypeError("The Pascal must be a non-negative real number.")

        return pascal * (c/b)

    """
        Function    : BarToTorr
        Description : This function to convert pressure from Bar to Torr.
        Formula     : bar x (( 100000 x 760 ) / 101325 )
        Input       : 
                      - Bar number type integer or float
        Return      : Pressure Torr in type interger or float
        Example     : BarToTorr(0)
                    >> 0
    """
    def BarToTorr(bar):
        if type(bar) not in [int,float]:
            raise TypeError("The Bar must be a non-negative real number.")

        return bar * ((a*c)/b)
    
    """
        Function    : AtmToTorr
        Description : This function to convert pressure from ATM to Torr.
        Formula     : atm x 760
        Input       : 
                      - ATM number type integer or float
        Return      : Pressure Torr in type interger or float
        Example     : AtmToTorr(1)
                    >> 760
    """
    def AtmToTorr(atm):
        if type(atm) not in [int,float]:
            raise TypeError("The ATM must be a non-negative real number.")

        return atm * c
    
    """
        Function    : mmHgToTorr
        Description : This function to convert pressure from mmHg to Torr.
        Formula     : mmHg x (( 760 x 13.5951 x 9.80665) / 101325 )
        Input       : 
                      - mmHg number type integer or float
        Return      : Pressure Torr in type interger or float
        Example     : mmHgToTorr(0)
                    >> 0
    """
    def mmHgToTorr(mmHg):
        if type(mmHg) not in [int,float]:
            raise TypeError("The mmHg must be a non-negative real number.")

        return mmHg * ((c*d*e)/b)
    
    """
        Function    : PascalTommHg
        Description : This function to convert pressure from Pascal to mmHg.
        Formula     : pascal x ( 1 / ( 13.5951 x 9.80665 ))
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure mmHg in type interger or float
        Example     : PascalTommHg(0)
                    >> 0
    """
    def PascalTommHg(pascal):
        if type(pascal) not in [int,float]:
            raise TypeError("The Pascal must be a non-negative real number.")

        return pascal * (1/(d*e))
    
    """
        Function    : BarTommHg
        Description : This function to convert pressure from Pascal to mmHg.
        Formula     : bar x (100000/(13.5951 x 9.80665))
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure mmHg in type interger or float
        Example     : BarTommHg(0)
                    >> 0
    """
    def BarTommHg(bar):
        if type(bar) not in [int,float]:
            raise TypeError("The Bar must be a non-negative real number.")

        return bar * (a/(d*e))
    
    """
        Function    : AtmTommHg
        Description : This function to convert pressure from ATM to mmHg.
        Formula     : atm x ( 101325 / ( 13.5951 x 9.80665 ))
        Input       : 
                      - ATM number type integer or float
        Return      : Pressure mmHg in type interger or float
        Example     : AtmTommHg(0)
                    >> 0
    """
    def AtmTommHg(atm):
        if type(atm) not in [int,float]:
            raise TypeError("The ATM must be a non-negative real number.")

        return atm * (b/(d*e))
    
    """
        Function    : TorrTommHg
        Description : This function to convert pressure from Torr to mmHg.
        Formula     : torr x ( 101325 / ( 760 x 13.5951 x 9.80665 ))
        Input       : 
                      - Torr number type integer or float
        Return      : Pressure mmHg in type interger or float
        Example     : TorrTommHg(0)
                    >> 0
    """
    def TorrTommHg(torr):
        if type(torr) not in [int,float]:
            raise TypeError("The Torr must be a non-negative real number.")

        return torr * (b/(c*d*e))
    
    """
        Function    : PsiToPascal
        Description : This function to convert pressure from PSI to Pascal.
        Formula     : psi x 6894.8
        Input       : 
                      - PSI number type integer or float
        Return      : Pressure pascal in type interger or float
        Example     : PsiToPascal(1)
                    >> 6894.8
    """
    def PsiToPascal(psi):
        if type(psi) not in [int,float]:
            raise TypeError("The PSI must be a non-negative real number.")

        return psi * 6894.8
    
    """
        Function    : PsiToBar
        Description : This function to convert pressure from PSI to Bar.
        Formula     : psi x ( 6.8948 / 100 )
        Input       : 
                      - PSI number type integer or float
        Return      : Pressure bar in type interger or float
        Example     : PsiToBar(1)
                    >> 0.068948
    """
    def PsiToBar(psi):
        if type(psi) not in [int,float]:
            raise TypeError("The PSI must be a non-negative real number.")

        return psi * (6.8948/100)
    
    """
        Function    : PsiToAtm
        Description : This function to convert pressure from PSI to ATM.
        Formula     : psi x ( 6.8048 / 100 )
        Input       : 
                      - PSI number type integer or float
        Return      : Pressure ATM in type interger or float
        Example     : PsiToAtm(0)
                    >> 0
    """
    def PsiToAtm(psi):
        if type(psi) not in [int,float]:
            raise TypeError("The PSI must be a non-negative real number.")

        return psi * (6.8046/100)
    
    """
        Function    : PsiToTorr
        Description : This function to convert pressure from PSI to Torr.
        Formula     : psi x 51.71493
        Input       : 
                      - PSI number type integer or float
        Return      : Pressure Torr in type interger or float
        Example     : PsiToTorr(1)
                    >> 51.71493
    """
    def PsiToTorr(psi):
        if type(psi) not in [int,float]:
            raise TypeError("The PSI must be a non-negative real number.")

        return psi * 51.71493
    
    """
        Function    : PascalToPsi
        Description : This function to convert pressure from Pascal to PSI.
        Formula     : pascal x ( 1.450377 / 100000 )
        Input       : 
                      - Pascal number type integer or float
        Return      : Pressure PSI in type interger or float
        Example     : PascalToPsi(0)
                    >> 0

    """
    def PascalToPsi(pascal):
        if type(pascal) not in [int,float]:
            raise TypeError("The Pascal must be a non-negative real number.")

        return pascal * (1.450377/10000)
    
    """
        Function    : BarToPsi
        Description : This function to convert pressure from Bar to PSI.
        Formula     : bar x 14.50377
        Input       : 
                      - Bar number type integer or float
        Return      : Pressure PSI in type interger or float
        Example     : BarToPsi(1)
                    >> 14.50377
    """
    def BarToPsi(bar):
        if type(bar) not in [int,float]:
            raise TypeError("The Bar must be a non-negative real number.")

        return bar * 14.50377
    
    """
        Function    : AtmToPsi
        Description : This function to convert pressure from ATM to PSI.
        Formula     : atm x 14.69595
        Input       : 
                      - ATM number type integer or float
        Return      : Pressure PSI in type interger or float
        Example     : AtmToPsi(1)
                    >> 14.69595
    """
    def AtmToPsi(atm):
        if type(atm) not in [int,float]:
            raise TypeError("The ATM must be a non-negative real number.")

        return atm * 14.69595
    
    """
        Function    : TorrToPsi
        Description : This function to convert pressure from Torr to PSI.
        Formula     : torr x ( 1.933678 / 100 )
        Input       : 
                      - Torr number type integer or float
        Return      : Pressure PSI in type interger or float
        Example     : TorrToPsi(0)
                    >> 0
    """
    def TorrToPsi(torr):
        if type(torr) not in [int,float]:
            raise TypeError("The Torr must be a non-negative real number.")

        return torr * (1.933678/100)
    
    """
        Function    : ForceAndArea
        Description : This function to calculate pressure
                      when you know Force , Area.
        Formula     : F / A
        Input       : 
                      - Force(F) number type integer or float
                      - Area(A)  number type integer or float
        Return      : Pressure in type interger or float
        Example     : ForceAndArea(1,1)
                    >> 1
    """
    def ForceAndArea(force,area):
        if type(force) not in [int,float]:
            raise TypeError("The Force must be a non-negative real number.")
        if type(area) not in [int,float]:
            raise TypeError("The Area must be a non-negative real number.")
        
        if area <= 0:
            raise ValueError("The Area cannot be negative.")

        return force / area
    
    """
        Function    : EnergyAndVolume
        Description : This function to calculate pressure
                      when you know Energy , Volume.
        Formula     : W / V
        Input       : 
                      - Energy(W) number type integer or float
                      - Volume(V)  number type integer or float
        Return      : Pressure in type interger or float
        Example     : EnergyAndVolume(1,1)
                    >> 1
    """
    def EnergyAndVolume(energy,volume):
        if type(energy) not in [int,float]:
            raise TypeError("The Energy must be a non-negative real number.")
        if type(volume) not in [int,float]:
            raise TypeError("The Volume must be a non-negative real number.")
        
        if volume <= 0:
            raise ValueError("The Volume cannot be negative.")

        return energy / volume
    
    """
        Function    : Gas
        Description : This function to calculate Gas pressure
                      when you know n mole ,Volume , R constant , Temperature.
        Formula     : (n x r x temp) / volume
        Input       : 
                      - Temperatue(T) number type integer or float
                      - Volume(V)  number type integer or float
                      - N mole(n) number type integer or float
                      - Constant gas (R) number type integer or float
        Return      : Pressure in type interger or float
        Example     : Gas(1,1,1,1)
                    >> 1
    """
    def Gas(volume,n,r,temp):
        if type(volume) not in [int,float]:
            raise TypeError("The Volume must be a non-negative real number.")
        if type(n) not in [int,float]:
            raise TypeError("The n Mole must be a non-negative real number.")
        if type(r) not in [int,float]:
            raise TypeError("The Gas constant must be a non-negative real number.")
        if type(temp) not in [int,float]:
            raise TypeError("The Temperature must be a non-negative real number.")
        
        if volume <= 0:
            raise ValueError("The Volume cannot be negative.")
        if r < 0:
            raise ValueError("The Gas constant cannot be negative.")
        if n < 0:
            raise ValueError("The n Mole cannot be negative.")

        return (n * r * temp) / volume
    
    """
        Function    : KineticMass
        Description : This function to calculate Kinetic pressure
                      when you know Volume,Velocity,Mass.
        Formula     : ( 1/2 x Mass x Velocity^2 ) / Volume
        Input       : 
                      - Mass number type integer or float
                      - Volume(V)  number type integer or float
                      - Velocity number type integer or float
        Return      : Pressure in type interger or float
        Example     : KineticMass(1,1,1)
                    >> 0.5
    """
    def KineticMass(volume,velocity,mass):
        if type(volume) not in [int,float]:
            raise TypeError("The Volume must be a non-negative real number.")
        if type(velocity) not in [int,float]:
            raise TypeError("The Velocity must be a non-negative real number.")
        if type(mass) not in [int,float]:
            raise TypeError("The Mass must be a non-negative real number.")
        
        if volume <= 0:
            raise ValueError("The Volume cannot be negative.")
        if mass <= 0:
            raise ValueError("The Mass cannot be negative.")
        if velocity < 0:
            raise ValueError("The Velocity cannot be negative.")

        return (0.5 * mass * velocity**2)/volume
    
    """
        Function    : KineticRho
        Description : This function to calculate Kinetic pressure
                      when you know Density(rho) , Velocity.
        Formula     : ( 1/2 x rho x velocity^2 )
        Input       : 
                      - Density(rho) number type integer or float
                      - Velocity number type integer or float
        Return      : Pressure in type interger or float
        Example     : KineticRho(1,1)
                    >> 0.5
    """
    def KineticRho(velocity,rho):
        if type(velocity) not in [int,float]:
            raise TypeError("The Velocity must be a non-negative real number.")
        if type(rho) not in [int,float]:
            raise TypeError("The Density must be a non-negative real number.")
        
        if rho <= 0:
            raise ValueError("The Density cannot be negative.")
        if velocity <= 0:
            raise ValueError("The Velocity cannot be negative.")

        return 0.5 * rho * velocity**2
    
    """
        Function    : PotentialMass
        Description : This function to calculate Potential pressure
                      when you know Volume , Mass , Height.
        Formula     : ( mass x g x height ) / volume
        Input       : 
                      - Mass number type integer or float
                      - Volume number type integer or float
                      - Height number type integer or float
        Return      : Pressure in type interger or float
        Example     : PotentialMass(1,1,1)
                    >> 1
    """
    def PotentialMass(volume,mass,height):

        if type(volume) not in [int,float]:
            raise TypeError("The Volume must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The Height must be a non-negative real number.")
        if type(mass) not in [int,float]:
            raise TypeError("The Mass must be a non-negative real number.")
        
        if volume <= 0:
            raise ValueError("The Volume cannot be negative.")
        if mass <= 0:
            raise ValueError("The Mass cannot be negative.")
        if height <= 0:
            raise ValueError("The Height cannot be negative.")

        return (mass * g * height) / volume
    
    """
        Function    : PotentialRho
        Description : This function to calculate Potential pressure
                      when you know Density(rho) , Height.
        Formula     : rho x g x height
        Input       : 
                      - Density number type integer or float
                      - Height number type integer or float
        Return      : Pressure in type interger or float
        Example     : PotentialRho(1,1)
                    >> 9.8
    """
    def PotentialRho(rho,height):
  
        if type(height) not in [int,float]:
            raise TypeError("The Height must be a non-negative real number.")
        if type(rho) not in [int,float]:
            raise TypeError("The Density must be a non-negative real number.")

        if rho <= 0:
            raise ValueError("The Density cannot be negative.")
        if height <= 0:
            raise ValueError("The Height cannot be negative.")

        return rho * g * height


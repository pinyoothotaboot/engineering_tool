

class Temperature:

    """
        Function    : CelsiusToFahrenheit
        Description : This function to convert temperature in celsius degree to fahrenheit
        Formula     : 9/5 x C + 32
        Input       : Celsius number temperature type integer or float
        Return      : Fahrenheit number temperature in type interger or float
        Example     : CelsiusToFahrenheit(0)
                    >> 33.8
    """
    def CelsiusToFahrenheit(celsius):

        if type(celsius) not in [int,float]:
            raise TypeError("The celsius must be a non-negative real number.")

        return (9/5) * celsius + 32
    
    """
        Function    : KelvinToFahrenheit
        Description : This function to convert temperature in kelvin degree to fahrenheit
        Formula     : 9/5 x (K - 273.15) + 32
        Input       : Kelvin number temperature type integer or float
        Return      : Fahrenheit number temperature in type interger or float
        Example     : KelvinToFahrenheit(0)
                    >> -239.35
    """
    def KelvinToFahrenheit(kelvin):
        if type(kelvin) not in [int,float]:
            raise TypeError("The kelvin must be a non-negative real number.")

        return (9/5) * (kelvin - 273.15) + 32
    
    """
        Function    : FahrenheitToCelsius
        Description : This function to convert temperature in fahrenheit degree to celsius
        Formula     : 5/9 x ( F - 32)
        Input       : Fahrenheit number temperature type integer or float
        Return      : Celsius number temperature in type interger or float
        Example     : FahrenheitToCelsius(0)
                    >> -31.444444
    """
    def FahrenheitToCelsius(fahrenheit):
        if type(fahrenheit) not in [int,float]:
            raise TypeError("The fahrenheit must be a non-negative real number.")

        return (5/9) * (fahrenheit - 32)
    
    """
        Function    : CelsiusToKelvin
        Description : This function to convert temperature in celsius degree to kelvin
        Formula     : C + 273.15
        Input       : Celsius number temperature type integer or float
        Return      : Kelvin number temperature in type interger or float
        Example     : CelsiusToKelvin(0)
                    >> 273.15
    """
    def CelsiusToKelvin(celsius):
        if type(celsius) not in [int,float]:
            raise TypeError("The celsius must be a non-negative real number.")

        return celsius + 273.15
    
    """
        Function    : KelvinToCelsius
        Description : This function to convert temperature in kelvin degree to celsius
        Formula     : K - 273.15
        Input       : Kelvin number temperature type integer or float
        Return      : Celsius number temperature in type interger or float
        Example     : KelvinToCelsius(0)
                    >> -273.15
    """
    def KelvinToCelsius(kelvin):
        if type(kelvin) not in [int,float]:
            raise TypeError("The kelvin must be a non-negative real number.")

        return kelvin - 273.15
    
    """
        Function    : FahrenheitToKelvin
        Description : This function to convert temperature in fahrenheit degree to kelvin
        Formula     : 5/9 x ( F - 32) + 273.15
        Input       : Fahrenheit number temperature type integer or float
        Return      : Kelvin number temperature in type interger or float
        Example     : FahrenheitToKelvin(0)
                    >> 255.372222
    """
    def FahrenheitToKelvin(fahrenheit):
        if type(fahrenheit) not in [int,float]:
            raise TypeError("The fahrenheit must be a non-negative real number.")
            
        return (5/9) * (fahrenheit - 32) + 273.15
    
    """
        Function    : Gas
        Description : This function to calculate temperature gas
        Formula     : PV/nR
        Input       : 
                      - Pressure number temperature type integer or float
                      - Volume number temperature type integer or float
                      - Constant R number temperature type integer or float
                      - N mole number temperature type integer or float
        Return      : Temperature number temperature in type interger or float
        Example     : Gas(1,1,1,1)
                    >> 1
    """
    def Gas(pressure,volume,n,R):

        if type(pressure) not in [int,float]:
            raise TypeError("The pressure must be a non-negative real number.")
        if type(volume) not in [int,float]:
            raise TypeError("The volume must be a non-negative real number.")
        if type(n) not in [int,float]:
            raise TypeError("The n mole must be a non-negative real number.")
        if type(R) not in [int,float]:
            raise TypeError("The Gas constant must be a non-negative real number.")
        
        if volume <= 0:
            raise ValueError("The volume cannot be negative.")
        if n <= 0:
            raise ValueError("The n mole cannot be negative.")
        if R <= 0:
            raise ValueError("The Gas constant cannot be negative.")

        return (pressure * volume)/(n * R)

    

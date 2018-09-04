import math

class Area:

    """
        Function    : circle
        Description : This function to calculate area of circle.
        Formula     : PI * Radius^2
        Input       : Radius number type integer or float
        Return      : Area of circle in type interger or float
        Example     : circle(1)
                    >> 3.1416
    """
    def circle(radius):
        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")
        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        return math.pi * (radius**2)
    
    """
        Function    : rectangle
        Description : This function to calculate area of rectangle.
        Formula     : Base x Height
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
        Return      : Area of rectangle in type interger or float
        Example     : rectangle(2,2)
                    >> 4
    """
    def rectangle(base,height):

        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")

        if type(height) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")

        if base < 0:
            raise ValueError("The base cannot be negative.")

        if height < 0:
            raise ValueError("The height cannot be negative.")
        
        return base * height
    
    """
        Function    : square
        Description : This function to calculate area of square.
        Formula     : val^2
        Input       : Val number type integer or float
        Return      : Area of square in type interger or float
        Example     : square(2)
                    >> 4
    """
    def square(val):
        if type(val) not in [int,float]:
            raise TypeError("The value must be a non-negative real number.")
        if val<0:
            raise ValueError("The val cannot be negative.")
        return val*val
    
    """
        Function    : triangle
        Description : This function to calculate area of triangle.
        Formula     : 0.5 x Base x Height
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
        Return      : Area of triangle in type interger or float
        Example     : rectangle(2,2)
                    >> 2
    """
    def triangle(base,height):

        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")

        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if base < 0:
            raise ValueError("The base cannot be negative.")
        if height < 0:
            raise ValueError("The height cannot be negative.")

        return 0.5 * base * height
    
    """
        Function    : parallelogram
        Description : This function to calculate area of parallelogram.
        Formula     : Base x Height
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
        Return      : Area of parallelogram in type interger or float
        Example     : parallelogram(2,2)
                    >> 4
    """
    def parallelogram(base,height):

        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")

        if type(height) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")

        if base < 0:
            raise ValueError("The base cannot be negative.")

        if height < 0:
            raise ValueError("The height cannot be negative.")
        
        return base * height
    
    """
        Function    : trapezoid
        Description : This function to calculate area of trapezoid.
        Formula     : 0.5 x (Base1+Base2) x Height
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
        Return      : Area of trapezoid in type interger or float
        Example     : trapezoid(2,2,2)
                    >> 4
    """
    def trapezoid(base1,base2,height):
        if type(base1) not in [int,float]:
            raise TypeError("The base 1 must be a non-negative real number.")
        if type(base2) not in [int,float]:
            raise TypeError("The base 2 must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if base1 < 0:
            raise ValueError("The base 1 cannot be negative.")
        if base2 < 0:
            raise ValueError("The base 2 cannot be negative.")
        if height < 0:
            raise ValueError("The height cannot be negative.")

        return 0.5 * (base1+base2) * height



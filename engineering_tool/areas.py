import math

class Area:

    """
        Function    : circularsector
        Description : This function to calculate area of circular sector.
        Formula     : angle/2 x radius^2
        Input       : 
                      - Radius number type integer or float
                      - Angle number type integer or float
        Return      : Area of circle sector in type interger or float
        Example     : circularsector(1,0)
                    >> 3.1416
    """
    def circularsector(radius,angle):
        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")
        if type(angle) not in [int,float]:
            raise TypeError("The degree must be a non-negative real number.")

        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        if angle < 0:
            raise ValueError("The degree cannot be negative.")

        return (angle/2)*(radius**2)
    
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
        Function    : equilateral
        Description : This function to calculate area of equilateral triangle.
        Formula     : sqrt(3)/4 x s^2
        Input       : 
                      - S number type integer or float
        Return      : Area of equilateral triangle in type interger or float
        Example     : equilateral(0)
                    >> 0
    """
    def equilateral(s):

        if type(s) not in [int,float]:
            raise TypeError("The s side must be a non-negative real number.")
        
        if s < 0:
            raise ValueError("The s side cannot be negative.")

        return (math.sqrt(3)/4) * (s**2)

    """
        Function    : isosceles
        Description : This function to calculate area of isosceles triangle.
        Formula     : b/4 x sqrt(4a^2 - b^2)
        Input       : 
                      - A  number type integer or float
                      - B  number type integer or float
        Return      : Area of isosceles triangle in type interger or float
        Example     : isosceles(0,0)
                    >> 0
    """
    def isosceles(a,b):
        if type(a) not in [int,float]:
            raise TypeError("The a side must be a non-negative real number.")

        if type(b) not in [int,float]:
            raise TypeError("The b side must be a non-negative real number.")

        if a < 0:
            raise ValueError("The a side cannot be negative.")

        if b < 0:
            raise ValueError("The b side cannot be negative.")

        return (1/4)*b*math.sqrt(4*(a**2)-(b**2))
    
    """
        Function    : hexagon
        Description : This function to calculate area of regular hexagon.
        Formula     : 3/2 x sqrt(3) x s^2
        Input       : 
                      - S number type integer or float
        Return      : Area of regular hexagon in type interger or float
        Example     : hexagon(0)
                    >> 0
    """
    def hexagon(s):
        if type(s) not in [int,float]:
            raise TypeError("The s side must be a non-negative real number.")
        
        if s < 0:
            raise ValueError("The s side cannot be negative.")

        return (3/2)*math.sqrt(3)*(s**2)
    
    """
        Function    : octagon
        Description : This function to calculate area of regular octagon.
        Formula     : 2 x (1+sqrt(2)) x s^2
        Input       : 
                      - S number type integer or float
        Return      : Area of regular octagon in type interger or float
        Example     : octagon(0)
                    >> 0
    """
    def octagon(s):
        if type(s) not in [int,float]:
            raise TypeError("The s side must be a non-negative real number.")
        
        if s < 0:
            raise ValueError("The s side cannot be negative.")

        return 2 * (1+math.sqrt(2))*(s**2)
    
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
    
    """
        Function    : cylinder
        Description : This function to calculate area of surface cylinder.
        Formula     : 2 x pi x radius x(radius+height)
        Input       : 
                      - Radius number type integer or float
                      - Height number type integer or float
        Return      : Area of surface cylinder in type interger or float
        Example     : cylinder(0,0)
                    >> 0
    """
    def cylinder(radius,height):
        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        if height < 0:
            raise ValueError("The height cannot be negative.")

        return 2 * math.pi * radius * (radius+height)
    
    """
        Function    : sphere
        Description : This function to calculate area of surface sphere.
        Formula     : 4 x pi x radius^2
        Input       : 
                      - Radius number type integer or float
        Return      : Area of surface sphere in type interger or float
        Example     : sphere(0)
                    >> 0
    """
    def sphere(radius):
        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")

        if radius < 0:
            raise ValueError("The radius cannot be negative.")

        return 4 * math.pi * (radius**2)
    
    """
        Function    : pyramid
        Description : This function to calculate area of surface pyramid.
        Formula     : B + PL/2
        Input       : 
                      - B number type integer or float
                      - P number type integer or float
                      - L number type integer or float
        Return      : Area of surface pyramid in type interger or float
        Example     : pyramid(1,0,0)
                    >> 1
    """
    def pyramid(B,P,L):
        if type(B) not in [int,float]:
            raise TypeError("The Base area must be a non-negative real number.")
        if type(P) not in [int,float]:
            raise TypeError("The Petimeter base must be a non-negative real number.")
        if type(L) not in [int,float]:
            raise TypeError("The Slant height must be a non-negative real number.")

        if B < 0:
            raise ValueError("The Base area cannot be negative.")
        if P < 0:
            raise ValueError("The Petimeter base cannot be negative.")
        if L < 0:
            raise ValueError("The Slant height cannot be negative.")

        return B + (P*L)/2



import math

class Volume:
    """
        Function    : sphere
        Description : This function to calculate volume of sphere.
        Formula     : 4/3 x PI x radius^3
        Input       : Radius number type integer or float
        Return      : Volume of sphere in type interger or float
        Example     : sphere(1)
                    >> 4.1888
    """
    def sphere(radius):

        if type(radius) not in [int,float]:
            raise TypeError("The radius cannot be negative.")

        if radius < 0:
            raise ValueError("The radius must be a non-negative real number.")

        return (4/3)*math.pi*(radius**3)
    
    """
        Function    : cube
        Description : This function to calculate volume of cube.
        Formula     : value^3
        Input       : Value number type integer or float
        Return      : Volume of cube in type interger or float
        Example     : cube(1)
                    >> 1
    """
    def cube(val):
        if type(val) not in [int,float]:
            raise TypeError("The value cannot be negative.")
        if val < 0:
            raise ValueError("The value must be a non-negative real number.")

        return val**3
    
    """
        Function    : rectangular
        Description : This function to calculate volume of rectangular.
        Formula     : base x height x wide
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
                      - Wide number type integer or float
        Return      : Volume of rectangular in type interger or float
        Example     : rectangular(2,2,2)
                    >> 8
    """
    def rectangular(wide,base,height):

        if type(wide) not in [int,float]:
            raise TypeError("The wide must be a non-negative real number.")
        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if wide < 0:
            raise ValueError("The wide must be a non-negative real number.")
        if base < 0:
            raise ValueError("The base must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")

        return wide * base * height
    
    """
        Function    : cylinder
        Description : This function to calculate volume of cylinder.
        Formula     : radius^2 x height x PI
        Input       : 
                      - Radius number type integer or float
                      - Height number type integer or float
        Return      : Volume of cylinder in type interger or float
        Example     : cylinder(1,1)
                    >> 3.1416
    """
    def cylinder(radius,height):
        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if radius < 0:
            raise ValueError("The radius must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")

        return math.pi * (radius**2) * height
    
    """
        Function    : pyramid
        Description : This function to calculate volume of pyramid.
        Formula     : 1/3 x base^2 x height
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
        Return      : Volume of pyramid in type interger or float
        Example     : pyramid(1,1)
                    >> 0.3333
    """
    def pyramid(base,height):

        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if base < 0:
            raise ValueError("The base must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")

        return (1/3) * (base**2) * height
    
    """
        Function    : cone
        Description : This function to calculate volume of cone.
        Formula     : 1/3 x PI x radius^2 x height
        Input       : 
                      - Radius number type integer or float
                      - Height number type integer or float
        Return      : Volume of cone in type interger or float
        Example     : cone(1,1)
                    >> 1.0472
    """
    def cone(radius,height):

        if type(radius) not in [int,float]:
            raise TypeError("The radius must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")

        if radius < 0:
            raise ValueError("The radius must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")

        return (1/3) * math.pi * (radius**2) * height
    
    """
        Function    : triangular
        Description : This function to calculate volume of triangular.
        Formula     : 1/2 x base x height x wide
        Input       : 
                      - Base number type integer or float
                      - Height number type integer or float
                      - Wide number type integer or float
        Return      : Volume of triangular in type interger or float
        Example     : triangular(1,1,1)
                    >> 0.5
    """
    def triangular(base,height,wide):
        if type(base) not in [int,float]:
            raise TypeError("The base must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")
        if type(wide) not in [int,float]:
            raise TypeError("The wide must be a non-negative real number.")
        if base < 0:
            raise ValueError("The base must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")
        if wide < 0:
            raise ValueError("The wide must be a non-negative real number.")
        return 0.5 * base * height * wide
    
    """
        Function    : ellipsoid
        Description : This function to calculate volume of ellipsoid.
        Formula     : 4/3 x PI x radius1 x radius2 x radius3
        Input       : 
                      - Radius 1 number type integer or float
                      - Radius 2 number type integer or float
                      - Radius 3 number type integer or float
        Return      : Volume of ellipsoid in type interger or float
        Example     : ellipsoid(1,1,1)
                    >> 4.1888
    """
    def ellipsoid(radius1,radius2,radius3):

        if type(radius1) not in [int,float]:
            raise TypeError("The radius 1 must be a non-negative real number.")
        if type(radius2) not in [int,float]:
            raise TypeError("The radius 2 must be a non-negative real number.")
        if type(radius3) not in [int,float]:
            raise TypeError("The radius 3 must be a non-negative real number.")
        
        if radius1 < 0:
            raise ValueError("The radius 1 must be a non-negative real number.")
        if radius2 < 0:
            raise ValueError("The radius 2 must be a non-negative real number.")
        if radius3 < 0:
            raise ValueError("The radius 3 must be a non-negative real number.")

        return (4/3) * math.pi * radius1 * radius2 * radius3
    
    """
        Function    : irregular
        Description : This function to calculate volume of irregular.
        Formula     : area x height
        Input       : 
                      - Area number type integer or float
                      - Height number type integer or float
        Return      : Volume of irregular in type interger or float
        Example     : irregular(1,2)
                    >> 2
    """
    def irregular(area,height):
        if type(area) not in [int,float]:
            raise TypeError("The area must be a non-negative real number.")
        if type(height) not in [int,float]:
            raise TypeError("The height must be a non-negative real number.")
        
        if area < 0:
            raise ValueError("The area must be a non-negative real number.")
        if height < 0:
            raise ValueError("The height must be a non-negative real number.")

        return area * height

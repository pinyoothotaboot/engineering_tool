
from engineering_tool.areas import *
from engineering_tool.units import Unit,Convert


value = 12 # inch

 
print("1 Centrimeter = %.9f"%Unit(value).InchToCentrimetre().ToUnit())


base = 10 
height = 20

area = Area.triangle(base,height)

print("Area triangle is %.2f"%area)

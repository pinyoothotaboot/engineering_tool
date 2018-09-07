# Definition
**Area** is the quantity that expresses the extent of a two-dimensional figure or shape or planar lamina, in the plane. Surface area is its analog on the two-dimensional surface of a three-dimensional object. Area can be understood as the amount of material with a given thickness that would be necessary to fashion a model of the shape, or the amount of paint necessary to cover the surface with a single coat. It is the two-dimensional analog of the length of a curve (a one-dimensional concept) or the volume of a solid (a three-dimensional concept).[wiki](https://en.wikipedia.org/wiki/Area)

# Reference
**1.Equilateral triangle area**

![area = \frac{\sqrt{3}}{4}{s^2}](https://latex.codecogs.com/svg.latex?area%20=%20\frac{\sqrt{3}}{4}{s^2})
	
**s** is the length of one side of the triangle.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/9/96/Triangle.Equilateral.svg)
```python
from engineering_tool.areas import Area
s = 2.5 # cm
equilateral_area = Area.equilateral(s)
print("Equilateral triangle area is %.2f cm2"%equilateral_area)
```
**2.Triangle area**

![area = \frac{1}{2}bh](https://latex.codecogs.com/svg.latex?area%20=%20\frac{1}{2}bh)
	
**b** and  **h** are the base and height (measured perpendicular to the base), respectively.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/7/72/Triangle.Right.svg)

```python
from engineering_tool.areas import Area
base = 3 # cm
height = 4 # cm 
triangle_area = Area.triangle(base,height)
print("Triangle area is %.2f cm2"%triangle_area)
```

**3.Isosceles triangle area**

![area = \frac{b}{4}\sqrt(4{a^2}-{b^2})](https://latex.codecogs.com/svg.latex?area%20=%20\frac{b}{4}\sqrt(4{a^2}-{b^2}))

**a** is the length of one of the two equal sides and **b** is the length of a different side.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/1/14/Triangle.Isosceles.svg)

```python
from engineering_tool.areas import Area
a = 5 # cm
b = 3 # cm 
isosceles_area = Area.isosceles(a,b)
print("Isosceles triangle area is %.2f cm2"%isosceles_area)
```

**4.Parallelogram area**

![area = bh](https://latex.codecogs.com/svg.latex?area%20=%20bh)

**b** is the length of the base and  **h** is the perpendicular height.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/4/41/Parallelogram.svg)

```python
from engineering_tool.areas import Area
base = 7 # cm
height = 8 # cm 
parallelogram_area = Area.parallelogram(base,height)
print("Parallelogram area is %.2f cm2"%parallelogram_area)
```
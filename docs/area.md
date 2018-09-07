# Definition
**Area** is the quantity that expresses the extent of a two-dimensional figure or shape or planar lamina, in the plane. Surface area is its analog on the two-dimensional surface of a three-dimensional object. Area can be understood as the amount of material with a given thickness that would be necessary to fashion a model of the shape, or the amount of paint necessary to cover the surface with a single coat. It is the two-dimensional analog of the length of a curve (a one-dimensional concept) or the volume of a solid (a three-dimensional concept).[wiki](https://en.wikipedia.org/wiki/Area)

# Reference
**Equilateral triangle area**

![area = \frac{\sqrt{3}}{4}{s^2}](https://latex.codecogs.com/svg.latex?area%20=%20\frac{\sqrt{3}}{4}{s^2})
	
**s** is the length of one side of the triangle.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/9/96/Triangle.Equilateral.svg)
```python
from engineering_tool.areas import Area
s = 2.5 # cm
equilateral_area = Area.equilateral(s)
print("Equilateral triangle area is %.2f cm2"%equilateral_area = Area.equilateral(s)
)
```
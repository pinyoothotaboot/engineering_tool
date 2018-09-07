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

**5.Trapezoid**

![area =  \frac{1}{2}(a+b)h](https://latex.codecogs.com/svg.latex?area%20=%20\frac{1}{2}(a+b)h)

**a** and **b** are the parallel sides and  **h** the distance (height) between the parallels.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/1/11/Trapezoid.svg)

```python
from engineering_tool.areas import Area
a_base = 7 # cm
b_base = 10 # cm
height = 9 # cm 
trapezoid_area = Area.trapezoid(a_base,b_base,height)
print("Trapezoid area is %.2f cm2"%trapezoid_area)
```

**6.Hexagon**

![area=\frac{3}{2}\sqrt(3){s^2}](https://latex.codecogs.com/svg.latex?area=\frac{3}{2}\sqrt(3){s^2})

**s** is the length of one side of the hexagon.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/3/38/Regular_polygon_6_annotated.svg)

```python
from engineering_tool.areas import Area
s = 7 # cm
hexagon_area = Area.hexagon(s)
print("Hexagon area is %.2f cm2"%hexagon_area)
```

**7.Octagon**

$$area={2}(1+\sqrt(2)){s^2}$$

**s** is the length of one side of the octagon.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/e/e5/Regular_polygon_8_annotated.svg)

```python
from engineering_tool.areas import Area
s = 7 # cm
octagon_area = Area.octagon(s)
print("Octagon area is %.2f cm2"%octagon_area)
```

**8.Circle**

![area = \pi{r^2}](https://latex.codecogs.com/svg.latex?area%20=%20\pi\cdot{r^2})

**r** is the radius

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/0/03/Circle-withsegments.svg)

```python
from engineering_tool.areas import Area
radius = 7 # cm
circle_area = Area.circle(radius)
print("Circle area is %.2f cm2"%circle_area)
```

**9.Circular sector**

![area = \frac{\theta}{2}{r^2}](https://latex.codecogs.com/svg.latex?area%20=%20\frac{\theta}{2}{r^2})

The radius and angle (in radians).

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/d/da/Circle_arc.svg)

```python
from engineering_tool.areas import Area
radius = 7 # cm
angle = 0.5 # radian
circularsector_area = Area.circularsector(radius,angle)
print("Circular sector area is %.2f cm2"%circularsector_area)
```

**10.Cylinder**

![area={2}\pi{r}(r+h)](https://latex.codecogs.com/svg.latex?area={2}\pi{r}(r+h))

**r** and **h** are the radius and height, respectively.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/3/36/Circular_cylinder_rh.svg)

```python
from engineering_tool.areas import Area
radius = 7 # cm
height = 20 # cm
cylinder_area = Area.cylinder(radius,height)
print("Cylinder area is %.2f cm2"%cylinder_area)
```

**11.Sphere**

![area = {4}\pi{r^2}](https://latex.codecogs.com/svg.latex?area%20=%20{4}\pi{r^2})

**r** the radius, respectively.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/0/07/Sphere_and_Ball.png)

```python
from engineering_tool.areas import Area
radius = 7 # cm
sphere_area = Area.sphere(radius)
print("Sphere area is %.2f cm2"%sphere_area)
```

**12.Pyramid**

![area = {B}+\frac{PL}{2}](https://latex.codecogs.com/svg.latex?area%20=%20{B}+\frac{PL}{2})

**B** is the base area, **P** is the base perimeter and **L** is the slant height.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/9/91/Pyramid.svg)

```python
from engineering_tool.areas import Area
base = 7 # cm
perimeter = 8 # cm
height = 10 # cm
pyramid_area = Area.pyramid(base,perimeter,height)
print("Pyramid area is %.2f cm2"%pyramid_area)
```

**13.Square**

![area = {s^2}](https://latex.codecogs.com/svg.latex?area%20=%20{s^2})

**s** is the length of one side of the square.

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/6/60/Five_Squared.svg)

```python
from engineering_tool.areas import Area
s = 7 # cm
square_area = Area.square(s)
print("Square area is %.2f cm2"%square_area)
```

**14.Rectangle**

![area = {b}{h}](https://latex.codecogs.com/svg.latex?area%20=%20{b}{h})

**b**  and **h** is base length and height

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/d/d7/Rectangle_Geometry_Vector.svg)

```python
from engineering_tool.areas import Area
base = 7 # cm
height = 9 # cm
rectangle_area = Area.rectangle(base,height)
print("Rectangle area is %.2f cm2"%rectangle_area)
```


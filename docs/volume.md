# Definition

**Volume** is the quantity of three-dimensional space enclosed by a closed surface, for example, the space that a substance solid liquid, gas, plasma Volume is often quantified numerically using the SI derived unit, the cubic metre. The volume of a container is generally understood to be the capacity of the container; i. e., the amount of fluid (gas or liquid) that the container could hold, rather than the amount of space the container itself displaces. Three dimensional mathematical shapes are also assigned volumes. Volumes of some simple shapes, such as regular, straight-edged, and circular shapes can be easily calculated using arithmetic  formulas. Volumes of complicated shapes can be calculated with integral calculus if a formula exists for the shape's boundary. One-dimensional figures (such as lines) and two-dimensional shapes (such as squares) are assigned zero volume in the three-dimensional space.[wiki](https://en.wikipedia.org/wiki/Volume)

# Reference

**1.Cube**
	
![volume = {s^3}](https://latex.codecogs.com/svg.latex?volume%20=%20{s^3})

**s** = length of any side (or edge)	

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/7/78/Hexahedron.jpg)

```python
from engineering_tool.volumes import Volume
s = 4 # cm
cube_volume = Volume.cube(s)
print("Cube volume is %.2f cm2"%cube_volume)
```

**2.Cylinder**

![volume = \pi{r^2}h](https://latex.codecogs.com/svg.latex?volume%20=%20\pi{r^2}h)

**r**  = radius of circular base,  **h**  = height

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/3/36/Circular_cylinder_rh.svg)

```python
from engineering_tool.volumes import Volume
radius = 4 # cm
height = 5 # cm
cylinder_volume = Volume.cylinder(radius,height)
print("Cylinder volume is %.2f cm2"%cylinder_volume)
```

**3.Sphere**

![volume = \frac{4}{3}\pi{r^3}](https://latex.codecogs.com/svg.latex?volume%20=%20\frac{4}{3}\pi{r^3})

**r** = radius of sphere

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/7/7e/Sphere_wireframe_10deg_6r.svg)

```python
from engineering_tool.volumes import Volume
radius = 4 # cm
sphere_volume = Volume.sphere(radius)
print("Sphere volume is %.2f cm2"%sphere_volume)
```

**4.Rectangular**

![volume = bwh](https://latex.codecogs.com/svg.latex?volume%20=%20bwh)

**b** = base, **w** = width, **h** = height

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/3/32/Cuboid_simple.svg)

```python
from engineering_tool.volumes import Volume
base = 4 # cm
width = 5 # cm
height = 6 # cm
rectangular_volume = Volume.rectangular(width,base,height)
print("Rectangular volume is %.2f cm2"%rectangular_volume)
```

**5.Pyramid**

![volume = \frac{1}{3}{b^2}h](https://latex.codecogs.com/svg.latex?volume%20=%20\frac{1}{3}{b^2}h)

**B** = area of the base, **h** = height of pyramid

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/9/91/Pyramid.svg)

```python
from engineering_tool.volumes import Volume
base = 4 # cm2
height = 5 # cm
pyramid_volume = Volume.pyramid(base,height)
print("Pyramid volume is %.2f cm2"%pyramid_volume)
```

**6.Cone**

![volume = \frac{1}{3}\pi{r^2}h](https://latex.codecogs.com/svg.latex?volume%20=%20\frac{1}{3}\pi{r^2}h)

**r** = radius of circle at base, **h** = distance from base to tip or height

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/d/d2/Cone_3d.png)

```python
from engineering_tool.volumes import Volume
radius = 4 # cm
height = 7 # cm
cone_volume = Volume.cone(radius,height)
print("Cone volume is %.2f cm2"%cone_volume)
```

**7.Triangular**

![volume = \frac{1}{2}bwh](https://latex.codecogs.com/svg.latex?volume%20=%20\frac{1}{2}bwh)

**b**  = base length of triangle,  **h**  = height of triangle,  **w**  = length of prism or distance between the triangular bases

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/8/8c/TruncatedTriangularPrism.png)

```python
from engineering_tool.volumes import Volume
base = 4 # cm
width = 5 # cm
height = 7 # cm
triangular_volume = Volume.triangular(base,height,width)
print("Triangular volume is %.2f cm2"%triangular_volume)
```

**8.Ellipsoid**

![volume = \frac{4}{3}\pi{a}{b}{c}](https://latex.codecogs.com/svg.latex?volume%20=%20\frac{4}{3}\pi{a}{b}{c})

**a**,**b**,**c** = semi-axes of ellipsoid

**Example**

![](https://upload.wikimedia.org/wikipedia/commons/0/0e/Ellipsoid-affin.svg)

```python
from engineering_tool.volumes import Volume
a = 4 # cm
b = 5 # cm
c = 7 # cm
ellipsoid_volume = Volume.ellipsoid(a,b,c)
print("Ellipsoid volume is %.2f cm2"%ellipsoid_volume)
```

**9.Irregular**

![volume = Ah](https://latex.codecogs.com/svg.latex?volume%20=%20Ah)

**A** is area base  , **h** is height

**Example**

![](/docs/images/irregular.gif)

```python
from engineering_tool.volumes import Volume
area = 4 # cm
height = 5 # cm
irregular_volume = Volume.irregular(area,height)
print("Irregular volume is %.2f cm2"%irregular_volume)
```



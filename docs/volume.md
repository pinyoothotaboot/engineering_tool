# Definition

**Volume** is the quantity of three-dimensional space enclosed by a closed surface, for example, the space that a substance solid liquid, gas, plasma Volume is often quantified numerically using the SI derived unit, the cubic metre. The volume of a container is generally understood to be the capacity of the container; i. e., the amount of fluid (gas or liquid) that the container could hold, rather than the amount of space the container itself displaces. Three dimensional mathematical shapes are also assigned volumes. Volumes of some simple shapes, such as regular, straight-edged, and circular shapes can be easily calculated using arithmetic  formulas. Volumes of complicated shapes can be calculated with integral calculus if a formula exists for the shape's boundary. One-dimensional figures (such as lines) and two-dimensional shapes (such as squares) are assigned zero volume in the three-dimensional space.[wiki](https://en.wikipedia.org/wiki/Volume)

# Formula

- Sphere

	![V = \frac{4}{3}\pi{r^3}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{4}{3}\pi{r^3})

	- r : Radius
- Cube

	![V = {s^3}](https://latex.codecogs.com/svg.latex?V%20=%20{s^3})

	- s : Length base or height or wide
- Rectangular

	![V = bwh](https://latex.codecogs.com/svg.latex?V%20=%20bwh)

	- b : Base
	- w : Wide
	- h : Height
- Cylinder

	![V = \pi{r^2}h](https://latex.codecogs.com/svg.latex?V%20=%20\pi{r^2}h)

	- r : Radius
	- h : Height
- Pyramid

	![V = \frac{1}{3}{b^2}h](https://latex.codecogs.com/svg.latex?V%20=%20\frac{1}{3}{b^2}h)

	- b : Length of base
	- h : height
- Cone

	![V = \frac{1}{3}\pi{r^2}h](https://latex.codecogs.com/svg.latex?V%20=%20\frac{1}{3}\pi{r^2}h)

	- r : Radius
	- h : Height
- Triangular
	![V = \frac{1}{2}bwh](https://latex.codecogs.com/svg.latex?V%20=%20\frac{1}{2}bwh)

	- b : Base
	- w : Wide
	- h : Height
- Ellipsoid

	![V = \frac{4}{3}\pi{r1}{r2}{r3}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{4}{3}\pi{r1}{r2}{r3})

	- r1 : Radius 1
	- r2 : Radius 2
	- r3 : Radius 3
- Irregular

	![V = Ah](https://latex.codecogs.com/svg.latex?V%20=%20Ah)

	- A : Area
	- h : Height

# Example

**from** engineering_tool.volumes **import** *

radius1 = 15.5         # cm

radius2 = 16.7         # 

radius3 =  17.8        # cm

base =  20                # cm

height = 30              # cm

wide     = 40             # cm

A   =    10                  # cm2

**print**("Sphere is %.3f cm3"%Volume.sphere(radius1))

**print**("Cube is %.3f cm3"%Volume.cube(base))

**print**("Rectangular is %.3f cm3"%Volume.rectangular(wide,base,height))

**print**("Cylinder is %.3f cm3"%Volume.cylinder(radius2,height))

**print**("Pyramid is %.3f cm3"%Volume.pyramid(base,height))

**print**("Cone is %.3f cm3"%Volume.cone(radius3,height))

**print**("Triangular is %.3f"%Volume.triangular(base,height,wide))

**print**("Ellipsoid is %.3f"%Volume.ellipsoid(radius1,radius2,radius3))

**print**("Irregular is %.3f"%Volume.irregular(A,height))

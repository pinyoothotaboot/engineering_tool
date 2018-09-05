# Definition

**Area** is the quantity that expresses the extent of a two-dimensional figure or shape or planar lamina, in the plane. Surface area is its analog on the two-dimensional surface of a three-dimensional object. Area can be understood as the amount of material with a given thickness that would be necessary to fashion a model of the shape, or the amount of paint  necessary to cover the surface with a single coat. It is the two-dimensional analog of the length  of a curve  (a one-dimensional concept) or the volume of a solid (a three-dimensional concept).[wiki](https://en.wikipedia.org/wiki/Area)

# Formula
- Circle area
	
    ![Area = \pi{r^2}](https://latex.codecogs.com/svg.latex?Area%20=%20\pi\cdot{r^2})
		
    - r : Radius
- Rectangle area

	![Area = bh](https://latex.codecogs.com/svg.latex?Area%20=%20bh)
		
    - b : Base
	- h : Height
- Square area

	![Area = {s^2}](https://latex.codecogs.com/svg.latex?Area%20=%20{s^2})
		
    - s : Length base or height or wide
- Triangle area

	![Area = \frac{1}{2}bh](https://latex.codecogs.com/svg.latex?Area%20=%20\frac{1}{2}bh)

- Parallelogram area

	![Area = bh](https://latex.codecogs.com/svg.latex?Area%20=%20bh)

- trapezoid

	![Area =  \frac{1}{2}(b1+b2)h](https://latex.codecogs.com/svg.latex?Area%20=%20\frac{1}{2}(b1+b2)h)

	- b1 : Base parallel sides
	- b2 : Base parallel sides

# Example

**from** engineering_tool.areas **import** *

radius = 15.5         # cm

base1 =  20           # cm

base2 =  25           # cm

height = 30           # cm

**print**("Circle area is %.2f cm2"%Area.circle(radius))

**print**("Rectangle area is %.2f cm2"%Area.rectangle(base1,height))

**print**("Square area is %.2f cm2"%Area.square(base2))

**print**("Triangle area is %.2f cm2"%Area.triangle(base2,height))

**print**("Parallelogram area is %.2f cm2"%Area.parallelogram(base1,height))

**print**("Trapezoid area is %.2f cm2"%Area.trapezoid(base1,base2,height))
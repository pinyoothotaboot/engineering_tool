import unittest
import sys
import math
sys.path.append('..')

from engineering_tool.areas import Area

class TestArea(unittest.TestCase):

    def test_circleArea(self):
        self.assertAlmostEqual(Area.circle(1),math.pi)
        self.assertAlmostEqual(Area.circle(0),0)
        self.assertAlmostEqual(Area.circle(2.1),math.pi*(2.1**2))
    
    def test_circleValue(self):
        self.assertRaises(ValueError,Area.circle,-2)

    def test_circleType(self):
        self.assertRaises(TypeError,Area.circle,3+5j)
        self.assertRaises(TypeError,Area.circle,True)
        self.assertRaises(TypeError,Area.circle,"Radius")

    def test_rectangleArea(self):
        self.assertAlmostEqual(Area.rectangle(0,0),0)
        self.assertAlmostEqual(Area.rectangle(2,2),2*2)
    
    def test_rectangleValue(self):
        self.assertRaises(ValueError,Area.rectangle,-2,1)
        self.assertRaises(ValueError,Area.rectangle,1,-2)
    
    def test_rectangleType(self):
        self.assertRaises(TypeError,Area.rectangle,3+5j,2)
        self.assertRaises(TypeError,Area.rectangle,2,3+5j)
        self.assertRaises(TypeError,Area.rectangle,True,2)
        self.assertRaises(TypeError,Area.rectangle,2,True)
        self.assertRaises(TypeError,Area.rectangle,"base",2)
        self.assertRaises(TypeError,Area.rectangle,2,"height")
    
    def test_squareArea(self):
        self.assertAlmostEqual(Area.square(0),0)
        self.assertAlmostEqual(Area.square(2),-2*-2)
    
    def test_squareValue(self):
        self.assertRaises(ValueError,Area.square,-1)
    
    def test_squareType(self):
        self.assertRaises(TypeError,Area.square,2+5j)
        self.assertRaises(TypeError,Area.square,True)
        self.assertRaises(TypeError,Area.square,"S")
    
    def test_triangleArea(self):
        self.assertAlmostEqual(Area.triangle(0,0),0)
        self.assertAlmostEqual(Area.triangle(2,2),2*2*0.5)
        self.assertAlmostEqual(Area.triangle(1,1),0.5)
    
    def test_triangleValue(self):
        self.assertRaises(ValueError,Area.triangle,-2,2)
        self.assertRaises(ValueError,Area.triangle,2,-2)
    
    def test_triangleType(self):
        self.assertRaises(TypeError,Area.triangle,3+5j,1)
        self.assertRaises(TypeError,Area.triangle,1,3+5j)
        self.assertRaises(TypeError,Area.triangle,True,5)
        self.assertRaises(TypeError,Area.triangle,5,True)
        self.assertRaises(TypeError,Area.triangle,"base",1)
        self.assertRaises(TypeError,Area.triangle,1,"height")

    def test_parallelogramArea(self):
        self.assertAlmostEqual(Area.parallelogram(0,0),0)
        self.assertAlmostEqual(Area.parallelogram(2,2),2*2)
    
    def test_parallelogramValue(self):
        self.assertRaises(ValueError,Area.parallelogram,-2,1)
        self.assertRaises(ValueError,Area.parallelogram,1,-2)
    
    def test_parallelogramType(self):
        self.assertRaises(TypeError,Area.parallelogram,3+5j,2)
        self.assertRaises(TypeError,Area.parallelogram,2,3+5j)
        self.assertRaises(TypeError,Area.parallelogram,True,2)
        self.assertRaises(TypeError,Area.parallelogram,2,True)
        self.assertRaises(TypeError,Area.parallelogram,"base",2)
        self.assertRaises(TypeError,Area.parallelogram,2,"height")
    
    def test_trapezoidArea(self):
        self.assertAlmostEqual(Area.trapezoid(0,0,0),0)
        self.assertAlmostEqual(Area.trapezoid(1,2,2),0.5*(1+2)*2)
    
    def test_trapezoidValue(self):
        self.assertRaises(ValueError,Area.trapezoid,-2,2,2)
        self.assertRaises(ValueError,Area.trapezoid,2,-2,2)
        self.assertRaises(ValueError,Area.trapezoid,2,2,-2)
    
    def test_trapezoidType(self):
        self.assertRaises(TypeError,Area.trapezoid,3+5j,2,2)
        self.assertRaises(TypeError,Area.trapezoid,2,3+5j,2)
        self.assertRaises(TypeError,Area.trapezoid,2,2,3+5j)

        self.assertRaises(TypeError,Area.trapezoid,True,2,2)
        self.assertRaises(TypeError,Area.trapezoid,2,True,2)
        self.assertRaises(TypeError,Area.trapezoid,2,2,True)

        self.assertRaises(TypeError,Area.trapezoid,"base1",2,2)
        self.assertRaises(TypeError,Area.trapezoid,2,"base2",2)
        self.assertRaises(TypeError,Area.trapezoid,2,2,"height")




        



        
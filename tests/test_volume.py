import unittest
import sys
import math
sys.path.append('..')

from engineering_tool.volumes import Volume

class TestVolume(unittest.TestCase):

    def test_sphereVolume(self):
        self.assertEqual(Volume.sphere(0),0)
        self.assertEqual(Volume.sphere(1),math.pi*(4/3))
        self.assertEqual(Volume.sphere(2.5),(4/3)*math.pi*2.5**3)
    
    def test_sphereValue(self):
        self.assertRaises(ValueError,Volume.sphere,-2)
    
    def test_sphereType(self):
        self.assertRaises(TypeError,Volume.sphere,2+2j)
        self.assertRaises(TypeError,Volume.sphere,True)
        self.assertRaises(TypeError,Volume.sphere,"Radius")

    def test_cubeVolume(self):
        self.assertEqual(Volume.cube(0),0)
        self.assertEqual(Volume.cube(1),1)
        self.assertEqual(Volume.cube(2),8)
    
    def test_cubeValue(self):
        self.assertRaises(ValueError,Volume.cube,-2)
    
    def test_cubeType(self):
        self.assertRaises(TypeError,Volume.cube,2+2j)
        self.assertRaises(TypeError,Volume.cube,True)
        self.assertRaises(TypeError,Volume.cube,"Value")
    
    def test_rectangularVolume(self):
        self.assertEqual(Volume.rectangular(0,1,2),0)
        self.assertEqual(Volume.rectangular(1,0,3),0)
        self.assertEqual(Volume.rectangular(1,2,0),0)
        self.assertEqual(Volume.rectangular(1,1,1),1)
        self.assertEqual(Volume.rectangular(2,2,2),2*2*2)
    
    def test_rectangularValue(self):
        self.assertRaises(ValueError,Volume.rectangular,-2,2,2)
        self.assertRaises(ValueError,Volume.rectangular,2,-2,2)
        self.assertRaises(ValueError,Volume.rectangular,2,2,-2)
    
    def test_rectangularType(self):
        self.assertRaises(TypeError,Volume.rectangular,2+2j,2,2)
        self.assertRaises(TypeError,Volume.rectangular,2,2+2j,2)
        self.assertRaises(TypeError,Volume.rectangular,2,2,2+2j)

        self.assertRaises(TypeError,Volume.rectangular,True,2,2)
        self.assertRaises(TypeError,Volume.rectangular,2,True,2)
        self.assertRaises(TypeError,Volume.rectangular,2,2,True)

        self.assertRaises(TypeError,Volume.rectangular,"Value",2,2)
        self.assertRaises(TypeError,Volume.rectangular,2,"Value",2)
        self.assertRaises(TypeError,Volume.rectangular,2,2,"Value")
    
    def test_cylinderVolume(self):
        self.assertAlmostEqual(Volume.cylinder(0,1),0)
        self.assertAlmostEqual(Volume.cylinder(1,0),0)
        self.assertAlmostEqual(Volume.cylinder(1,1),math.pi)
        self.assertAlmostEqual(Volume.cylinder(2.5,2),math.pi*(2.5**2)*2)
    
    def test_cylinderValue(self):
        self.assertRaises(ValueError,Volume.cylinder,-2,2)
        self.assertRaises(ValueError,Volume.cylinder,2,-2)
    
    def test_cylinderType(self):
        self.assertRaises(TypeError,Volume.cylinder,3+5j,2)
        self.assertRaises(TypeError,Volume.cylinder,2,3+5j)

        self.assertRaises(TypeError,Volume.cylinder,True,2)
        self.assertRaises(TypeError,Volume.cylinder,2,True)

        self.assertRaises(TypeError,Volume.cylinder,"radius",2)
        self.assertRaises(TypeError,Volume.cylinder,2,"height")
    
    def test_pyramidVolume(self):
        self.assertAlmostEqual(Volume.pyramid(0,1),0)
        self.assertAlmostEqual(Volume.pyramid(0,0),0)
        self.assertAlmostEqual(Volume.pyramid(1,0),0)

        self.assertAlmostEqual(Volume.pyramid(1,1),1/3)

        self.assertAlmostEqual(Volume.pyramid(2,2),(1/3)*(2**2)*2)
    
    def test_pyramidValue(self):
        self.assertRaises(ValueError,Volume.pyramid,-2,2)
        self.assertRaises(ValueError,Volume.pyramid,2,-2)
    
    def test_pyramidType(self):
        self.assertRaises(TypeError,Volume.pyramid,2+2j,2)
        self.assertRaises(TypeError,Volume.pyramid,2,2+2j)

        self.assertRaises(TypeError,Volume.pyramid,True,2)
        self.assertRaises(TypeError,Volume.pyramid,2,True)

        self.assertRaises(TypeError,Volume.pyramid,"base",2)
        self.assertRaises(TypeError,Volume.pyramid,2,"height")
    
    def test_coneVolume(self):
        self.assertAlmostEqual(Volume.cone(0,1),0)
        self.assertAlmostEqual(Volume.cone(1,0),0)
        self.assertAlmostEqual(Volume.cone(1,1),math.pi*(1/3))
        self.assertAlmostEqual(Volume.cone(2.5,2),(1/3)*math.pi*(2.5**2)*2)
    
    def test_coneValue(self):
        self.assertRaises(ValueError,Volume.cone,-2,2)
        self.assertRaises(ValueError,Volume.cone,2,-2)
    
    def test_coneType(self):
        self.assertRaises(TypeError,Volume.cone,3+5j,2)
        self.assertRaises(TypeError,Volume.cone,2,3+5j)

        self.assertRaises(TypeError,Volume.cone,True,2)
        self.assertRaises(TypeError,Volume.cone,2,True)

        self.assertRaises(TypeError,Volume.cone,"radius",2)
        self.assertRaises(TypeError,Volume.cone,2,"height")
    
    def test_triangularVolume(self):
        self.assertAlmostEqual(Volume.triangular(0,1,1),0)
        self.assertAlmostEqual(Volume.triangular(1,0,1),0)
        self.assertAlmostEqual(Volume.triangular(1,1,0),0)

        self.assertAlmostEqual(Volume.triangular(1,1,1),0.5)
        self.assertAlmostEqual(Volume.triangular(2,2,2),0.5*2*2*2)
    
    def test_triangularValue(self):
        self.assertRaises(ValueError,Volume.triangular,-2,2,2)
        self.assertRaises(ValueError,Volume.triangular,2,-2,2)
        self.assertRaises(ValueError,Volume.triangular,2,2,-2)
    
    def test_triangularType(self):
        self.assertRaises(TypeError,Volume.triangular,2+2j,2,2)
        self.assertRaises(TypeError,Volume.triangular,2,2+2j,2)
        self.assertRaises(TypeError,Volume.triangular,2,2,2+2j)

        self.assertRaises(TypeError,Volume.triangular,True,2,2)
        self.assertRaises(TypeError,Volume.triangular,2,True,2)
        self.assertRaises(TypeError,Volume.triangular,2,2,True)

        self.assertRaises(TypeError,Volume.triangular,"base",2,2)
        self.assertRaises(TypeError,Volume.triangular,2,"height",2)
        self.assertRaises(TypeError,Volume.triangular,2,2,"wide")
    
    def test_ellipsoidVolume(self):
        self.assertAlmostEqual(Volume.ellipsoid(0,1,1),0)
        self.assertAlmostEqual(Volume.ellipsoid(1,0,1),0)
        self.assertAlmostEqual(Volume.ellipsoid(1,1,0),0)

        self.assertAlmostEqual(Volume.ellipsoid(1,1,1),(4/3)*math.pi)
        self.assertAlmostEqual(Volume.ellipsoid(2,2.5,5),(4/3)*math.pi*2*2.5*5)
    
    def test_ellipsoidValue(self):
        self.assertRaises(ValueError,Volume.ellipsoid,-2,2,2)
        self.assertRaises(ValueError,Volume.ellipsoid,2,-2,2)
        self.assertRaises(ValueError,Volume.ellipsoid,2,2,-2)
    
    def test_ellipsoidType(self):
        self.assertRaises(TypeError,Volume.ellipsoid,2+2j,2,2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,2+2j,2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,2,2+2j)

        self.assertRaises(TypeError,Volume.ellipsoid,True,2,2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,True,2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,2,True)

        self.assertRaises(TypeError,Volume.ellipsoid,"radius1",2,2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,"radius2",2)
        self.assertRaises(TypeError,Volume.ellipsoid,2,2,"radius3")
    
    def test_irregularVolume(self):
        self.assertAlmostEqual(Volume.irregular(0,1),0)
        self.assertAlmostEqual(Volume.irregular(1,0),0)
        self.assertAlmostEqual(Volume.irregular(1,1),1)
        self.assertAlmostEqual(Volume.irregular(2.5,2),2.5*2)
    
    def test_irregularValue(self):
        self.assertRaises(ValueError,Volume.irregular,-2,2)
        self.assertRaises(ValueError,Volume.irregular,2,-2)
    
    def test_irregularType(self):
        self.assertRaises(TypeError,Volume.irregular,3+5j,2)
        self.assertRaises(TypeError,Volume.irregular,2,3+5j)

        self.assertRaises(TypeError,Volume.irregular,True,2)
        self.assertRaises(TypeError,Volume.irregular,2,True)

        self.assertRaises(TypeError,Volume.irregular,"area",2)
        self.assertRaises(TypeError,Volume.irregular,2,"height")









 

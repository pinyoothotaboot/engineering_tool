import unittest
import sys
import math
sys.path.append('..')

from engineering_tool.temperatures import Temperature

class TestTemperature(unittest.TestCase):

    def test_CelToFahTemp(self):
        self.assertAlmostEqual(Temperature.CelsiusToFahrenheit(0),32)
        self.assertAlmostEqual(Temperature.CelsiusToFahrenheit(1),32+(9/5))
        self.assertAlmostEqual(Temperature.CelsiusToFahrenheit(2.5),(9/5)*2.5+32)
        self.assertAlmostEqual(Temperature.CelsiusToFahrenheit(-200),(9/5)*-200+32)
    
    def test_CelToFahType(self):
        self.assertRaises(TypeError,Temperature.CelsiusToFahrenheit,2+2j)
        self.assertRaises(TypeError,Temperature.CelsiusToFahrenheit,True)
        self.assertRaises(TypeError,Temperature.CelsiusToFahrenheit,"Celsius")
    
    def test_KelToFahTemp(self):
        self.assertAlmostEqual(Temperature.KelvinToFahrenheit(0),(9/5)*(-273.15)+32)
        self.assertAlmostEqual(Temperature.KelvinToFahrenheit(2.5),(9/5)*(2.5-273.15)+32)
        self.assertAlmostEqual(Temperature.KelvinToFahrenheit(-200),(9/5)*(-200-273.15)+32)
    
    def test_KelToFahType(self):
        self.assertRaises(TypeError,Temperature.KelvinToFahrenheit,2+2j)
        self.assertRaises(TypeError,Temperature.KelvinToFahrenheit,True)
        self.assertRaises(TypeError,Temperature.KelvinToFahrenheit,"Kelvin")
    
    def test_FahToCelTemp(self):
        self.assertAlmostEqual(Temperature.FahrenheitToCelsius(0),(5/9)*-32)
        self.assertAlmostEqual(Temperature.FahrenheitToCelsius(2.5),(5/9)*(2.5-32))
        self.assertAlmostEqual(Temperature.FahrenheitToCelsius(-200),(5/9)*(-200-32))
    
    def test_FahToCelType(self):
        self.assertRaises(TypeError,Temperature.FahrenheitToCelsius,2+2j)
        self.assertRaises(TypeError,Temperature.FahrenheitToCelsius,True)
        self.assertRaises(TypeError,Temperature.FahrenheitToCelsius,"Fahrenheit")
    
    def test_CelToKelTemp(self):
        self.assertAlmostEqual(Temperature.CelsiusToKelvin(0),273.15)
        self.assertAlmostEqual(Temperature.CelsiusToKelvin(2.5),2.5+273.15)
        self.assertAlmostEqual(Temperature.CelsiusToKelvin(-200),-200+273.15)
    
    def test_CelToKelType(self):
        self.assertRaises(TypeError,Temperature.CelsiusToKelvin,2+2j)
        self.assertRaises(TypeError,Temperature.CelsiusToKelvin,True)
        self.assertRaises(TypeError,Temperature.CelsiusToKelvin,"Celsius")
    
    def test_KelToCelTemp(self):
        self.assertAlmostEqual(Temperature.KelvinToCelsius(0),-273.15)
        self.assertAlmostEqual(Temperature.KelvinToCelsius(2.5),2.5-273.15)
        self.assertAlmostEqual(Temperature.KelvinToCelsius(-200),-200-273.15)
    
    def test_KelToCelType(self):
        self.assertRaises(TypeError,Temperature.KelvinToCelsius,2+2j)
        self.assertRaises(TypeError,Temperature.KelvinToCelsius,True)
        self.assertRaises(TypeError,Temperature.KelvinToCelsius,"Celsius")
    
    def test_FahToKelTemp(self):
        self.assertAlmostEqual(Temperature.FahrenheitToKelvin(0),(5/9)*(-32)+273.15)
        self.assertAlmostEqual(Temperature.FahrenheitToKelvin(2.5),(5/9)*(2.5-32)+273.15)
        self.assertAlmostEqual(Temperature.FahrenheitToKelvin(-200),(5/9)*(-200-32)+273.15)
    
    def test_FahToKelType(self):
        self.assertRaises(TypeError,Temperature.FahrenheitToKelvin,2+2j)
        self.assertRaises(TypeError,Temperature.FahrenheitToKelvin,True)
        self.assertRaises(TypeError,Temperature.FahrenheitToKelvin,"Fahrenheit")
    
    def test_Gas(self):
        self.assertAlmostEqual(Temperature.Gas(0,1,1,1),0)
        self.assertAlmostEqual(Temperature.Gas(-200,2,2,2),(-200*2)/(2*2))
        self.assertAlmostEqual(Temperature.Gas(200,2,2,2),(200*2)/(2*2))
    
    def test_GasValue(self):
        self.assertRaises(ValueError,Temperature.Gas,2,-2,2,2)
        self.assertRaises(ValueError,Temperature.Gas,2,2,-2,2)
        self.assertRaises(ValueError,Temperature.Gas,2,2,2,-2)
    
    def test_GasType(self):
        self.assertRaises(TypeError,Temperature.Gas,2+2j,2,2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2+2j,2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,2+2j,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,2,2+2j)
        self.assertRaises(TypeError,Temperature.Gas,True,2,2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,True,2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,True,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,2,True)
        self.assertRaises(TypeError,Temperature.Gas,"P",2,2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,"V",2,2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,"n",2)
        self.assertRaises(TypeError,Temperature.Gas,2,2,2,"R")
        

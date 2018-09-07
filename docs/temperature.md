# Definition
**Temperature** is a physical quantity expressing hot and cold. It is measured with a thermometer calibrated in one or more temperature scales. The most commonly used scales are the Celsius scale (formerly called centigrade) (denoted °C), Fahrenheit scale (denoted °F), and Kelvin scale (denoted K). The kelvin (with a lower case is the unit of temperature in the International System of Units (abbreviated SI), in which temperature is one of the seven fundamental base quantities. The Kelvin scale is widely used in science and technology

![T = \frac{PV}{nR}](https://latex.codecogs.com/svg.latex?T%20=%20\frac{PV}{nR})

**T** = Temperature
**P** = Pressure
**V** = Volume
**R** = Gas constant
**n** = Gas mol

# Units of measurement
- Temperature (**Celsius**) , C
- Temperature (**Fahrenheit**) , F
- Temperature (**Kelvin**), K

# Conversion
- When known temp : **Celsius**

	![F = \frac{9}{5}{C}+32](https://latex.codecogs.com/svg.latex?F%20=%20\frac{9}{5}{C}+32)

	![K = {C}+273.15](https://latex.codecogs.com/svg.latex?K%20=%20{C}+273.15)

- When known temp : **Fahrenheit**

	![C = \frac{5}{9}(F-32)](https://latex.codecogs.com/svg.latex?C%20=%20\frac{5}{9}(F-32))

	![K = \frac{5}{9}(F-32)+{273.15}](https://latex.codecogs.com/svg.latex?K%20=%20\frac{5}{9}(F-32)+{273.15})

- When known temp : **Kelvin**

	![F = \frac{9}{5}(K-273.15)+32](https://latex.codecogs.com/svg.latex?F%20=%20\frac{9}{5}(K-273.15)+32)

	![C = K-273.15](https://latex.codecogs.com/svg.latex?C%20=%20K-273.15)

# Example

```python
from engineering_tool.temperatures import *

def ConvertToCelsius():
		F = 373 # Fahrenheit
		K = 400 # Kelvin
		
		C1 = Temperature.FahrenheitToCelsius(F)
		C2 = Temperature.KelvinToCelsius(K)
		
		print("Temperature C1 is %.2f C"%C1)
		print("Temperature C2 is %.2f C"%C2)

def ConvertToKelvin():
		F = 356 # Fahrenheit
		C = 150 # Celsius
		
		K1 = Temperature.FahrenheitToKelvin(F)
		K2 = Temperature.CelsiusToKelvin(C)
		
		print("Temperature K1 is %.2f K"%K1)
		print("Temperature K2 is %.2f K"%K2)

def ConvertToFahrenheit():
		C = 200 # Celsius
		K = 373 # Kelvin

		F1 = Temperature.CelsiusToFahrenheit(C)
		F2 = Temperature.KelvinToFahrenheit(K)

		print("Temperature F1 is %.2f F"%F1)
		print("Temperature F2 is %.2f F"%F2)

def GasTemperature():
		P = 150  # N/m2
		V = 40   # m3
		n = 0.607 # mol
		R = 0.08206 # (m3 x N/m2)/(mol x K)

		T = Temperature.Gas(P,V,n,R)

		print("Temperature is %.2f K"%T)
```
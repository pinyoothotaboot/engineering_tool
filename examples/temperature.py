import sys
sys.path.append("..")

from engineering_tool.temperatures import *

def Gas_Temperature():

    pressure = 0.22    # atm
    volume   = 10      # Litre or 1 Litre = 1000 cm^3
    n_Mole_H2O = 0.056 # mol  H2O 1 g / 18 g.mol^-1  
    R_H2O = 0.08206    # L.atm.mol^-1K^-1

    temp = Temperature.Gas(pressure,volume,n_Mole_H2O,R_H2O)

    print("Temperature : %f K"%temp)
    print("Temperature : %f C"%Temperature.KelvinToCelsius(temp))
    print("Temperature : %f F"%Temperature.KelvinToFahrenheit(temp))

Gas_Temperature()

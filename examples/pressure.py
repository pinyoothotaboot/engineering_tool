import sys
sys.path.append("..")
from engineering_tool.pressures import *

def ShowPressure(pressure):
    print("Pressure is %f Pascal"%pressure)
    print("Pressure is %f Bar"%Pressure.PascalToBar(pressure))
    print("Pressure is %f ATM"%Pressure.PascalToAtm(pressure))
    print("Pressure is %f mmHg"%Pressure.PascalTommHg(pressure))
    print("Pressure is %f PSI"%Pressure.PascalToPsi(pressure))
    print("Pressure is %f Torr"%Pressure.PascalToTorr(pressure))


# Formula : P = F/A
def SimplePressure():

    force = 100   # N
    area  = 0.1    # m^2

    pressure = Pressure.ForceAndArea(force,area)

    print("Simple Pressure")
    ShowPressure(pressure)

# Formula : P = 1/2mv^2 / V
def FluidKineticPressure():

    mass = 5.6 # Kg
    velocity = 15.5  # m/s
    volume = 4  # m^3

    pressure = Pressure.KineticMass(volume,velocity,mass)

    print("FLuid Kinetic Pressure")
    ShowPressure(pressure)

# Formula : P = mgh/V
def FluidPotentialPressure():

    mass   = 5.6  # Kg
    height = 1.75 # m
    volume = 4    # m^3 

    pressure = Pressure.PotentialMass(volume,mass,height)

    print("Fluid Potential Pressure")
    ShowPressure(pressure)


SimplePressure()
FluidKineticPressure()
FluidPotentialPressure()
import unittest
import sys
import math
sys.path.append('..')

from engineering_tool.electrics import *

class TestElectric(unittest.TestCase):

    def test_power(self):
        self.assertAlmostEqual(Power.VoltageAndCurrent(0,0),0)
        self.assertAlmostEqual(Power.VoltageAndCurrent(2,2),2*2)

        self.assertAlmostEqual(Power.VoltageAndResistance(0,1),0)
        self.assertAlmostEqual(Power.VoltageAndResistance(2,2),4/2)

        self.assertAlmostEqual(Power.ResistanceAndCurrent(0,0),0)
        self.assertAlmostEqual(Power.ResistanceAndCurrent(2,2),2*(2**2))

        self.assertAlmostEqual(Power.kWDC(0,0),0)
        self.assertAlmostEqual(Power.kWDC(2.5,5),2.5*5/1000)

        self.assertAlmostEqual(Power.kWOnePhaseAC(0,0,0),0)
        self.assertAlmostEqual(Power.kWOnePhaseAC(2,2.4,0.9),2*2.4*0.9/1000)

        self.assertAlmostEqual(Power.kWThreePhaseAC(0,0,0),0)
        self.assertAlmostEqual(Power.kWThreePhaseAC(2,2.5,0.8),1.73*2*2.5*0.8/1000)

        self.assertAlmostEqual(Power.kVAOnePhaseAC(0,0),0)
        self.assertAlmostEqual(Power.kVAOnePhaseAC(2,2),2*2/1000)

        self.assertAlmostEqual(Power.kVAThreePhaseAC(0,0),0)
        self.assertAlmostEqual(Power.kVAThreePhaseAC(2,3),2*3*1.73/1000)
    
    def test_powerValue(self):
        self.assertRaises(ValueError,Power.VoltageAndCurrent,-2,2)
        self.assertRaises(ValueError,Power.VoltageAndCurrent,2,-2)

        self.assertRaises(ValueError,Power.VoltageAndResistance,-2,2)
        self.assertRaises(ValueError,Power.VoltageAndResistance,2,-2)

        self.assertRaises(ValueError,Power.ResistanceAndCurrent,-2,2)
        self.assertRaises(ValueError,Power.ResistanceAndCurrent,2,-2)

        self.assertRaises(ValueError,Power.kWDC,-2,2)
        self.assertRaises(ValueError,Power.kWDC,2,-2)

        self.assertRaises(ValueError,Power.kWOnePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Power.kWOnePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Power.kWOnePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Power.kWThreePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Power.kWThreePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Power.kWThreePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Power.kVAOnePhaseAC,-2,2)
        self.assertRaises(ValueError,Power.kVAOnePhaseAC,2,-2)

        self.assertRaises(ValueError,Power.kVAThreePhaseAC,-2,2)
        self.assertRaises(ValueError,Power.kVAThreePhaseAC,2,-2)

    def test_powerType(self):
        self.assertRaises(TypeError,Power.VoltageAndCurrent,2+2j,2)
        self.assertRaises(TypeError,Power.VoltageAndCurrent,2,2+2j)
        self.assertRaises(TypeError,Power.VoltageAndCurrent,True,2)
        self.assertRaises(TypeError,Power.VoltageAndCurrent,2,True)
        self.assertRaises(TypeError,Power.VoltageAndCurrent,"voltage",2)
        self.assertRaises(TypeError,Power.VoltageAndCurrent,2,"current")

        self.assertRaises(TypeError,Power.VoltageAndResistance,2+2j,2)
        self.assertRaises(TypeError,Power.VoltageAndResistance,2,2+2j)
        self.assertRaises(TypeError,Power.VoltageAndResistance,True,2)
        self.assertRaises(TypeError,Power.VoltageAndResistance,2,True)
        self.assertRaises(TypeError,Power.VoltageAndResistance,"voltage",2)
        self.assertRaises(TypeError,Power.VoltageAndResistance,2,"resistance")

        self.assertRaises(TypeError,Power.ResistanceAndCurrent,2+2j,2)
        self.assertRaises(TypeError,Power.ResistanceAndCurrent,2,2+2j)
        self.assertRaises(TypeError,Power.ResistanceAndCurrent,True,2)
        self.assertRaises(TypeError,Power.ResistanceAndCurrent,2,True)
        self.assertRaises(TypeError,Power.ResistanceAndCurrent,2,"current")
        self.assertRaises(TypeError,Power.ResistanceAndCurrent,"resistance",2)

        self.assertRaises(TypeError,Power.kWDC,2+2j,2)
        self.assertRaises(TypeError,Power.kWDC,2,2+2j)
        self.assertRaises(TypeError,Power.kWDC,True,2)
        self.assertRaises(TypeError,Power.kWDC,2,True)
        self.assertRaises(TypeError,Power.kWDC,2,"current")
        self.assertRaises(TypeError,Power.kWDC,"voltage",2)

        self.assertRaises(TypeError,Power.kWOnePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,True,2,2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,True,2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,2,True)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,"voltage",2,2)
        self.assertRaises(TypeError,Power.kWOnePhaseAC,2,2,"powerfactor")

        self.assertRaises(TypeError,Power.kWThreePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,True,2,2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,True,2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,2,True)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,"voltage",2,2)
        self.assertRaises(TypeError,Power.kWThreePhaseAC,2,2,"powerfactor")

        self.assertRaises(TypeError,Power.kVAOnePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Power.kVAOnePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Power.kVAOnePhaseAC,True,2)
        self.assertRaises(TypeError,Power.kVAOnePhaseAC,2,True)
        self.assertRaises(TypeError,Power.kVAOnePhaseAC,2,"current")
        self.assertRaises(TypeError,Power.kVAOnePhaseAC,"voltage",2)

        self.assertRaises(TypeError,Power.kVAThreePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Power.kVAThreePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Power.kVAThreePhaseAC,True,2)
        self.assertRaises(TypeError,Power.kVAThreePhaseAC,2,True)
        self.assertRaises(TypeError,Power.kVAThreePhaseAC,2,"current")
        self.assertRaises(TypeError,Power.kVAThreePhaseAC,"voltage",2)

    
    def test_current(self):
        self.assertAlmostEqual(Current.PowerAndResistance(0,1),0)
        self.assertAlmostEqual(Current.PowerAndResistance(1,1),math.sqrt(1))
        self.assertAlmostEqual(Current.PowerAndResistance(2.5,5),math.sqrt(2.5/5))

        self.assertAlmostEqual(Current.PowerAndVoltage(0,1),0)
        self.assertAlmostEqual(Current.PowerAndVoltage(1,2),1/2)

        self.assertAlmostEqual(Current.VoltageAndResistance(0,1),0)
        self.assertAlmostEqual(Current.VoltageAndResistance(2,5),2/5)

        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyDC(0,1,1),0)
        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyDC(1,1,1),1*746/1*1)

        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyPFOnePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyPFOnePhaseAC(1,1,1,1),1*746/1*1*1)

        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyPFThreePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Current.HPAndVoltageAndEfficiencyPFThreePhaseAC(1,1,1,1),1*746/1.73*1*1*1)

        self.assertAlmostEqual(Current.kWAndVoltageAndPFOnePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Current.kWAndVoltageAndPFOnePhaseAC(1,1,1),1*1000/1*1)

        self.assertAlmostEqual(Current.kWAndVoltageAndPFThreePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Current.kWAndVoltageAndPFThreePhaseAC(1,1,1),1*1000/1.73*1*1)

        self.assertAlmostEqual(Current.kVAAndVoltageOnePhaseAC(0,1),0)
        self.assertAlmostEqual(Current.kVAAndVoltageOnePhaseAC(1,1),1*1000/1)

        self.assertAlmostEqual(Current.kVAAndVoltageThreePhaseAC(0,1),0)
        self.assertAlmostEqual(Current.kVAAndVoltageThreePhaseAC(1,1),1*1000/1.763)
    
    def test_currentValue(self):
        self.assertRaises(ValueError,Current.PowerAndResistance,-2,2)
        self.assertRaises(ValueError,Current.PowerAndResistance,2,-2)

        self.assertRaises(ValueError,Current.PowerAndVoltage,-2,2)
        self.assertRaises(ValueError,Current.PowerAndVoltage,2,-2)

        self.assertRaises(ValueError,Current.VoltageAndResistance,-2,2)
        self.assertRaises(ValueError,Current.VoltageAndResistance,2,-2)

        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyDC,-2,2,2)
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyDC,2,-2,2)
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyDC,2,2,-2)

        self.assertRaises(ValueError,Current.kWAndVoltageAndPFOnePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Current.kWAndVoltageAndPFOnePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Current.kWAndVoltageAndPFOnePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Current.kWAndVoltageAndPFThreePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Current.kWAndVoltageAndPFThreePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Current.kWAndVoltageAndPFThreePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,-2,2,2) 
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,-2,2) 
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,-2,2,2) 
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,-2,2) 
        self.assertRaises(ValueError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Current.kVAAndVoltageOnePhaseAC,-2,2)
        self.assertRaises(ValueError,Current.kVAAndVoltageOnePhaseAC,2,-2)

        self.assertRaises(ValueError,Current.kVAAndVoltageThreePhaseAC,-2,2)
        self.assertRaises(ValueError,Current.kVAAndVoltageThreePhaseAC,2,-2)           
    
    def test_currentType(self):
        self.assertRaises(TypeError,Current.PowerAndResistance,2+2j,2)
        self.assertRaises(TypeError,Current.PowerAndResistance,2,2+2j)
        self.assertRaises(TypeError,Current.PowerAndResistance,True,2)
        self.assertRaises(TypeError,Current.PowerAndResistance,2,True)
        self.assertRaises(TypeError,Current.PowerAndResistance,"power",2)
        self.assertRaises(TypeError,Current.PowerAndResistance,2,"resistance")

        self.assertRaises(TypeError,Current.PowerAndVoltage,2+2j,2)
        self.assertRaises(TypeError,Current.PowerAndVoltage,2,2+2j)
        self.assertRaises(TypeError,Current.PowerAndVoltage,True,2)
        self.assertRaises(TypeError,Current.PowerAndVoltage,2,True)
        self.assertRaises(TypeError,Current.PowerAndVoltage,"voltage",2)
        self.assertRaises(TypeError,Current.PowerAndVoltage,2,"power")

        self.assertRaises(TypeError,Current.VoltageAndResistance,2+2j,2)
        self.assertRaises(TypeError,Current.VoltageAndResistance,2,2+2j)
        self.assertRaises(TypeError,Current.VoltageAndResistance,True,2)
        self.assertRaises(TypeError,Current.VoltageAndResistance,2,True)
        self.assertRaises(TypeError,Current.VoltageAndResistance,2,"resistance")
        self.assertRaises(TypeError,Current.VoltageAndResistance,"voltage",2)

        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2+2j,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,2+2j,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,2,2+2j)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,True,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,True,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,2,True)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,"HP",2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,"E",2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyDC,2,2,"Eff")

        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,"E",2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFOnePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,"E",2,2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Current.HPAndVoltageAndEfficiencyPFThreePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,True,2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,True,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,2,True)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,"E",2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFOnePhaseAC,2,2,"PF")

        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,True,2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,True,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,2,True)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,"E",2)
        self.assertRaises(TypeError,Current.kWAndVoltageAndPFThreePhaseAC,2,2,"PF")

        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,True,2)
        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,2,True)
        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,2,"E")
        self.assertRaises(TypeError,Current.kVAAndVoltageOnePhaseAC,"kVA",2)

        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,True,2)
        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,2,True)
        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,2,"E")
        self.assertRaises(TypeError,Current.kVAAndVoltageThreePhaseAC,"kVA",2)
    
    def test_resistance(self):
        self.assertAlmostEqual(Resistance.VoltageAndPower(0,1),0)
        self.assertAlmostEqual(Resistance.VoltageAndPower(1,1),1)
        self.assertAlmostEqual(Resistance.VoltageAndPower(2.5,5),(2.5**2)/5)

        self.assertAlmostEqual(Resistance.PowerAndCurrent(0,1),0)
        self.assertAlmostEqual(Resistance.PowerAndCurrent(1,2),1/2**2)

        self.assertAlmostEqual(Resistance.VoltageAndCurrent(0,1),0)
        self.assertAlmostEqual(Resistance.VoltageAndCurrent(2,5),2/5)
    
    def test_resistanceValue(self):
        self.assertRaises(ValueError,Resistance.VoltageAndPower,-2,2)
        self.assertRaises(ValueError,Resistance.VoltageAndPower,2,-2)

        self.assertRaises(ValueError,Resistance.PowerAndCurrent,-2,2)
        self.assertRaises(ValueError,Resistance.PowerAndCurrent,2,-2)

        self.assertRaises(ValueError,Resistance.VoltageAndCurrent,-2,2)
        self.assertRaises(ValueError,Resistance.VoltageAndCurrent,2,-2)
    
    def test_resistanceType(self):
        self.assertRaises(TypeError,Resistance.VoltageAndPower,2+2j,2)
        self.assertRaises(TypeError,Resistance.VoltageAndPower,2,2+2j)
        self.assertRaises(TypeError,Resistance.VoltageAndPower,True,2)
        self.assertRaises(TypeError,Resistance.VoltageAndPower,2,True)
        self.assertRaises(TypeError,Resistance.VoltageAndPower,"power",2)
        self.assertRaises(TypeError,Resistance.VoltageAndPower,2,"voltage")

        self.assertRaises(TypeError,Resistance.PowerAndCurrent,2+2j,2)
        self.assertRaises(TypeError,Resistance.PowerAndCurrent,2,2+2j)
        self.assertRaises(TypeError,Resistance.PowerAndCurrent,True,2)
        self.assertRaises(TypeError,Resistance.PowerAndCurrent,2,True)
        self.assertRaises(TypeError,Resistance.PowerAndCurrent,"current",2)
        self.assertRaises(TypeError,Resistance.PowerAndCurrent,2,"power")

        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,2+2j,2)
        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,2,2+2j)
        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,True,2)
        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,2,True)
        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,2,"current")
        self.assertRaises(TypeError,Resistance.VoltageAndCurrent,"voltage",2)
    
    def test_voltage(self):
        self.assertAlmostEqual(Voltage.CurrentAndResistance(0,0),0)
        self.assertAlmostEqual(Voltage.CurrentAndResistance(2.5,3),2.5*3)

        self.assertAlmostEqual(Voltage.PowerAndCurrent(0,1),0)
        self.assertAlmostEqual(Voltage.PowerAndCurrent(2.5,3),2.5/3)

        self.assertAlmostEqual(Voltage.PowerAndResistance(0,0),0)
        self.assertAlmostEqual(Voltage.PowerAndResistance(2.5,3),math.sqrt(2.5*3))

        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentDC(0,1,1),0)
        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentDC(1,1,1),1*746/(1*1))

        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC(1,1,1,1),1*746/(1*1*1))

        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC(1,1,1,1),1*746/(1.73*1*1*1))

        self.assertAlmostEqual(Voltage.kWAndCurrentAndPFOnePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Voltage.kWAndCurrentAndPFOnePhaseAC(1,1,1),1*1000/(1*1))

        self.assertAlmostEqual(Voltage.kWAndCurrentAndPFThreePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Voltage.kWAndCurrentAndPFThreePhaseAC(1,1,1),1*1000/(1.73*1*1))

        self.assertAlmostEqual(Voltage.kVAAndCurrentOnePhaseAC(0,1),0)
        self.assertAlmostEqual(Voltage.kVAAndCurrentOnePhaseAC(1,1),1*1000/(1))

        self.assertAlmostEqual(Voltage.kVAAndCurrentThreePhaseAC(0,1),0)
        self.assertAlmostEqual(Voltage.kVAAndCurrentThreePhaseAC(1,1),1*1000/(1.763*1))
    
    def testvoltageValue(self):
        self.assertRaises(ValueError,Voltage.CurrentAndResistance,-2,2)
        self.assertRaises(ValueError,Voltage.CurrentAndResistance,2,-2)

        self.assertRaises(ValueError,Voltage.PowerAndCurrent,-2,2)
        self.assertRaises(ValueError,Voltage.PowerAndCurrent,2,-2)

        self.assertRaises(ValueError,Voltage.PowerAndResistance,-2,2)
        self.assertRaises(ValueError,Voltage.PowerAndResistance,2,-2)

        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentDC,-2,2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentDC,2,-2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentDC,2,2,-2)

        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFOnePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFThreePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Voltage.kVAAndCurrentOnePhaseAC,-2,2)
        self.assertRaises(ValueError,Voltage.kVAAndCurrentOnePhaseAC,2,-2)

        self.assertRaises(ValueError,Voltage.kVAAndCurrentThreePhaseAC,-2,2)
        self.assertRaises(ValueError,Voltage.kVAAndCurrentThreePhaseAC,2,-2)
    
    def test_voltageType(self):
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,2+2j,2)
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,2,2+2j)
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,True,2)
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,2,True)
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,"power",2)
        self.assertRaises(TypeError,Voltage.PowerAndCurrent,2,"current")

        self.assertRaises(TypeError,Voltage.PowerAndResistance,2+2j,2)
        self.assertRaises(TypeError,Voltage.PowerAndResistance,2,2+2j)
        self.assertRaises(TypeError,Voltage.PowerAndResistance,True,2)
        self.assertRaises(TypeError,Voltage.PowerAndResistance,2,True)
        self.assertRaises(TypeError,Voltage.PowerAndResistance,"power",2)
        self.assertRaises(TypeError,Voltage.PowerAndResistance,2,"resistance")

        self.assertRaises(TypeError,Voltage.CurrentAndResistance,2+2j,2)
        self.assertRaises(TypeError,Voltage.CurrentAndResistance,2,2+2j)
        self.assertRaises(TypeError,Voltage.CurrentAndResistance,True,2)
        self.assertRaises(TypeError,Voltage.CurrentAndResistance,2,True)
        self.assertRaises(TypeError,Voltage.CurrentAndResistance,"current",2)
        self.assertRaises(TypeError,Voltage.CurrentAndResistance,2,"resistance")

        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2+2j,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,2+2j,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,2,2+2j)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,True,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,True,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,2,True)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,"HP",2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,"current",2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentDC,2,2,"Eff")

        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,True,2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,True,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,2,True)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFOnePhaseAC,2,2,"PF")

        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,True,2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,True,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,2,True)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Voltage.kWAndCurrentAndPFThreePhaseAC,2,2,"PF")

        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,True,2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,2,True)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,"kVA",2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentOnePhaseAC,2,"current")

        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,2+2j,2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,2,2+2j)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,True,2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,2,True)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,"kVA",2)
        self.assertRaises(TypeError,Voltage.kVAAndCurrentThreePhaseAC,2,"current")
    
    def test_conductance(self):
        self.assertAlmostEqual(Conductance.Resistance(1),1)
        self.assertAlmostEqual(Conductance.Resistance(2.5),1/2.5)
    
    def test_conductanceValue(self):
        self.assertRaises(ValueError,Conductance.Resistance,0)
        self.assertRaises(ValueError,Conductance.Resistance,-2)
    
    def test_conductanceType(self):
        self.assertRaises(TypeError,Conductance.Resistance,2+2j)
        self.assertRaises(TypeError,Conductance.Resistance,True)
        self.assertRaises(TypeError,Conductance.Resistance,"resistance")
    
    def test_capacitance(self):
        self.assertAlmostEqual(Capacitance.Farad(0,1),0)
        self.assertAlmostEqual(Capacitance.Farad(2.5,36.7),2.5/36.7)

        self.assertAlmostEqual(Capacitance.Coulomb(0,0),0)
        self.assertAlmostEqual(Capacitance.Coulomb(2.5,36.7),2.5*36.7)
    
    def test_capacitanceValue(self):
        self.assertRaises(ValueError,Capacitance.Farad,-2,0)
        self.assertRaises(ValueError,Capacitance.Farad,0,-2)

        self.assertRaises(ValueError,Capacitance.Coulomb,-2,0)
        self.assertRaises(ValueError,Capacitance.Coulomb,0,-2)
    
    def test_capacitanceType(self):
        self.assertRaises(TypeError,Capacitance.Farad,2+2j,2)
        self.assertRaises(TypeError,Capacitance.Farad,2,2+2j)
        self.assertRaises(TypeError,Capacitance.Farad,True,2)
        self.assertRaises(TypeError,Capacitance.Farad,2,True)
        self.assertRaises(TypeError,Capacitance.Farad,"coulomb",2)
        self.assertRaises(TypeError,Capacitance.Farad,2,"voltage")

        self.assertRaises(TypeError,Capacitance.Coulomb,2+2j,2)
        self.assertRaises(TypeError,Capacitance.Coulomb,2,2+2j)
        self.assertRaises(TypeError,Capacitance.Coulomb,True,2)
        self.assertRaises(TypeError,Capacitance.Coulomb,2,True)
        self.assertRaises(TypeError,Capacitance.Coulomb,"farad",2)
        self.assertRaises(TypeError,Capacitance.Coulomb,2,"voltage")
    
    def test_frequency(self):
        self.assertAlmostEqual(Frequency.Hertz(1),1)
        self.assertAlmostEqual(Frequency.Hertz(100),1/100)

        self.assertAlmostEqual(Frequency.Sec(1),1)
        self.assertAlmostEqual(Frequency.Sec(100),1/100)
    
    def test_frequencyValue(self):
        self.assertRaises(ValueError,Frequency.Hertz,0)
        self.assertRaises(ValueError,Frequency.Hertz,-2)

        self.assertRaises(ValueError,Frequency.Sec,0)
        self.assertRaises(ValueError,Frequency.Sec,-2)
    
    def test_frequencyType(self):
        self.assertRaises(TypeError,Frequency.Hertz,2+2j)
        self.assertRaises(TypeError,Frequency.Hertz,True)
        self.assertRaises(TypeError,Frequency.Hertz,"time")

        self.assertRaises(TypeError,Frequency.Sec,2+2j)
        self.assertRaises(TypeError,Frequency.Sec,True)
        self.assertRaises(TypeError,Frequency.Sec,"hertz")
    
    def test_hosepower(self):
        self.assertAlmostEqual(Hosepower.DC(0,0,0),0)
        self.assertAlmostEqual(Hosepower.DC(1,746,1),1*746*1/746)

        self.assertAlmostEqual(Hosepower.OnePhaseAC(0,0,0,0),0)
        self.assertAlmostEqual(Hosepower.OnePhaseAC(1,746,1,1),1*746*1*1/746)

        self.assertAlmostEqual(Hosepower.ThreePhaseAC(0,0,0,0),0)
        self.assertAlmostEqual(Hosepower.ThreePhaseAC(1,746,1,1),1.73*1*746*1*1/746)
    
    def test_hosepowerValue(self):
        self.assertRaises(ValueError,Hosepower.DC,-2,2,2)
        self.assertRaises(ValueError,Hosepower.DC,2,-2,2)
        self.assertRaises(ValueError,Hosepower.DC,2,2,-2)

        self.assertRaises(ValueError,Hosepower.OnePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Hosepower.OnePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Hosepower.OnePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Hosepower.OnePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Hosepower.ThreePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Hosepower.ThreePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Hosepower.ThreePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Hosepower.ThreePhaseAC,2,2,2,-2)
    
    def test_hosepowerType(self):
        self.assertRaises(TypeError,Hosepower.DC,2+2j,2,2)
        self.assertRaises(TypeError,Hosepower.DC,2,2+2j,2)
        self.assertRaises(TypeError,Hosepower.DC,2,2,2+2j)
        self.assertRaises(TypeError,Hosepower.DC,True,2,2)
        self.assertRaises(TypeError,Hosepower.DC,2,True,2)
        self.assertRaises(TypeError,Hosepower.DC,2,2,True)
        self.assertRaises(TypeError,Hosepower.DC,"current",2,2)
        self.assertRaises(TypeError,Hosepower.DC,2,"E",2)
        self.assertRaises(TypeError,Hosepower.DC,2,2,"Eff")

        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,"current",2,2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,"E",2,2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Hosepower.OnePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,"current",2,2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,"E",2,2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,"Eff",2)
        self.assertRaises(TypeError,Hosepower.ThreePhaseAC,2,2,2,"PF")
    
    def test_powerfactor(self):
        self.assertAlmostEqual(Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC(1,1,1,1),746)

        self.assertAlmostEqual(Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC(1,1,1,1),746/1.73)

        self.assertAlmostEqual(Powerfactor.kWAndCurrentAndVoltageOnePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Powerfactor.kWAndCurrentAndVoltageOnePhaseAC(1,1,1),1000)

        self.assertAlmostEqual(Powerfactor.kWAndCurrentAndVoltageThreePhaseAC(0,1,1),0)
        self.assertAlmostEqual(Powerfactor.kWAndCurrentAndVoltageThreePhaseAC(1,1,1),1000/1.73)
    
    def test_powerfactorValue(self):
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,2,-2)

        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,-2,2,2)
        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,-2,2)
        self.assertRaises(ValueError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,2,-2)
    
    def test_powerfactorType(self):
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,"E",2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC,2,2,2,"Eff")

        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,"E",2)
        self.assertRaises(TypeError,Powerfactor.HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC,2,2,2,"Eff")

        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,True,2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,True,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,2,True)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageOnePhaseAC,2,2,"E")

        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2+2j,2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,2+2j,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,2,2+2j)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,True,2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,True,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,2,True)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,"kW",2,2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,"current",2)
        self.assertRaises(TypeError,Powerfactor.kWAndCurrentAndVoltageThreePhaseAC,2,2,"E")
    
    def test_efficiency(self):
        self.assertAlmostEqual(Efficiency.DC(0,1,1),0)
        self.assertAlmostEqual(Efficiency.DC(1,1,1),746)

        self.assertAlmostEqual(Efficiency.OnePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Efficiency.OnePhaseAC(1,1,1,1),746)

        self.assertAlmostEqual(Efficiency.ThreePhaseAC(0,1,1,1),0)
        self.assertAlmostEqual(Efficiency.ThreePhaseAC(1,1,1,1),746/1.73)
    
    def test_efficiencyValue(self):
        self.assertRaises(ValueError,Efficiency.DC,-2,2,2)
        self.assertRaises(ValueError,Efficiency.DC,2,-2,2)
        self.assertRaises(ValueError,Efficiency.DC,2,2,-2)

        self.assertRaises(ValueError,Efficiency.OnePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Efficiency.OnePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Efficiency.OnePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Efficiency.OnePhaseAC,2,2,2,-2)

        self.assertRaises(ValueError,Efficiency.ThreePhaseAC,-2,2,2,2)
        self.assertRaises(ValueError,Efficiency.ThreePhaseAC,2,-2,2,2)
        self.assertRaises(ValueError,Efficiency.ThreePhaseAC,2,2,-2,2)
        self.assertRaises(ValueError,Efficiency.ThreePhaseAC,2,2,2,-2)
    
    def test_efficiencyType(self):
        self.assertRaises(TypeError,Efficiency.DC,2+2j,2,2)
        self.assertRaises(TypeError,Efficiency.DC,2,2+2j,2)
        self.assertRaises(TypeError,Efficiency.DC,2,2,2+2j)
        self.assertRaises(TypeError,Efficiency.DC,True,2,2)
        self.assertRaises(TypeError,Efficiency.DC,2,True,2)
        self.assertRaises(TypeError,Efficiency.DC,2,2,True)
        self.assertRaises(TypeError,Efficiency.DC,"HP",2,2)
        self.assertRaises(TypeError,Efficiency.DC,2,"E",2)
        self.assertRaises(TypeError,Efficiency.DC,2,2,"current")

        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,"E",2)
        self.assertRaises(TypeError,Efficiency.OnePhaseAC,2,2,2,"PF")

        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2+2j,2,2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2+2j,2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,2+2j,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,2,2+2j)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,True,2,2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,True,2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,True,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,2,True)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,"HP",2,2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,"current",2,2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,"E",2)
        self.assertRaises(TypeError,Efficiency.ThreePhaseAC,2,2,2,"PF")

        


        

        





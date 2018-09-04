import sys
sys.path.append("..")
from engineering_tool.electrics import *

def Power_Electric():

    voltage_DC = 15      # Volt DC
    current_DC = 2.5     # Amp DC

    voltage_AC1P = 225.5 # Vrms 1 Phase
    current_AC1P = 5.5   # Amp  1 Phase
    PF_AC1P      = 0.8   # Power factor

    voltage_AC3P = 225.5 # Vrms 3 Phase
    current_AC3P = 5.5   # Amp  3 Phase
    PF_AC3P      = 0.8   # Power factor

    print("Power in DC..")
    print("Power is %.3f Watt"%Power.VoltageAndCurrent(voltage_DC,current_DC))
    print("Power is %.4f kW"%Power.kWDC(current_DC,voltage_DC))

    print("Power in AC 1 Phase..")
    print("Power is %.3f kW rms"%Power.kWOnePhaseAC(current_AC1P,voltage_AC1P,PF_AC1P))
    print("Power is %.3f kVA"%Power.kVAOnePhaseAC(current_AC1P,voltage_AC1P))

    print("Power in AC 3 Phase..")
    print("Power is %.3f kW rms"%Power.kWThreePhaseAC(current_AC3P,voltage_AC3P,PF_AC3P))
    print("Power is %.3f kVA"%Power.kVAThreePhaseAC(current_AC3P,voltage_AC3P))

def Current_Electric():

    voltage = 15   # Volt
    resistance = 1000 # Ohm

    #------- Motor 1 Phase
    HP_1Phase = 2.5 # Hosepower
    E_1Phase  = 230.5 # Volt peak
    PF_1Phase = 0.67  # power factor
    Eff_1Phase = 0.9  # Efficieny

    #------- Motor 3 Phase
    HP_3Phase = 2.5 # Hosepower
    E_3Phase  = 230.5 # Volt peak
    PF_3Phase = 0.67  # power factor
    Eff_3Phase = 0.9  # Efficieny


    print("Current in DC...")
    print("Current is %.3f Amp"%Current.VoltageAndResistance(voltage,resistance))

    print("Current motor in 1 Phase AC")
    print("Current is %.3f Amp peak"%Current.HPAndVoltageAndEfficiencyPFOnePhaseAC(HP_1Phase,E_1Phase,Eff_1Phase,PF_1Phase))

    print("Current motor in 3 Phase AC")
    print("Current is %.3f Amp peak"%Current.HPAndVoltageAndEfficiencyPFThreePhaseAC(HP_3Phase,E_3Phase,Eff_3Phase,PF_3Phase))

def Resistance_Electric():

    voltage = 30.5  # Volt DC
    current = 2.5   # Amp DC

    print("Resistance DC ...")
    print("Resistance is %.3f Ohm"%Resistance.VoltageAndCurrent(voltage,current))

def Voltage_Electric():

    current = 20.5 # Amp
    power   = 1000 # Watt

    # Motor  1 Phase AC
    HP_1Phase  = 0.5  # Hosepower
    current_1Phase = 10.3  # Amp rms
    Eff_1Phase  =  0.6  # Efficiency
    PF_1Phase   = 0.9   # Power factor

    # Motor  3 Phase AC
    HP_3Phase  = 0.5  # Hosepower
    current_3Phase = 10.3  # Amp rms
    Eff_3Phase  =  0.6  # Efficiency
    PF_3Phase   = 0.9   # Power factor

    print("Voltage DC...")
    print("Voltage is %.3f Volt"%Voltage.PowerAndCurrent(power,current)) 

    print("Voltage motor 1 Phase AC...")
    print("Voltage is %.3f Volt rms"%Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC(HP_1Phase,current_1Phase,Eff_1Phase,PF_1Phase))

    print("Voltage motor 3 Phase AC...")
    print("Voltage is %.3f Volt rms"%Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC(HP_3Phase,current_3Phase,Eff_3Phase,PF_3Phase))


def Conductance_Electric():

    voltage = 30  # Volt DC
    current = 3.5 # Amp DC
    resistance = 2000 # Ohm

    print("Conductance by R : %f"%Conductance.Resistance(resistance))
    print("Conductance by V and I : %f"%Conductance.VoltageAndCurrent(voltage,current))


def Capacitance_Electric():

    voltage = 200  # Volt DC
    capacitance = 0.00015  # Farad

    print("Coulomb...")
    print("Q : %f"%Capacitance.Coulomb(capacitance,voltage)) 


def Frequency_Electric():

    t = 1  #  Sec
    Hz = 60 #  Hertz

    print("Frequency is %f Hz"%Frequency.Hertz(t))
    print("Period is %f Sec"%Frequency.Sec(Hz))

def Hosepower_Electric():

    # Motor DC
    E_DC       = 45  # Volt
    Current_DC = 3.5 # Amp
    Eff_DC     = 0.7 # Efficiency

    # Motor 1 Phase AC
    E_1AC        = 220  # Volt rms
    Current_1AC  = 7.5  # Amp
    Eff_1AC      = 0.8  # Efficiency
    PF_1AC       = 0.75 # Power factor

    # Motor 3 Phase AC
    E_3AC        = 220  # Volt rms
    Current_3AC  = 7.5  # Amp
    Eff_3AC      = 0.8  # Efficiency
    PF_3AC       = 0.75 # Power factor

    print("Hose power ....")
    print("HP DC motor is %f HP"%Hosepower.DC(Current_DC,E_DC,Eff_DC))
    print("HP AC 1 Phase motor is %f HP"%Hosepower.OnePhaseAC(Current_1AC,E_1AC,Eff_1AC,PF_1AC))
    print("HP AC 3 Phase motor is %f HP"%Hosepower.ThreePhaseAC(Current_3AC,E_3AC,Eff_3AC,PF_3AC))




Voltage_Electric()
Resistance_Electric()
Current_Electric()
Power_Electric()
Conductance_Electric()
Capacitance_Electric()
Frequency_Electric()
Hosepower_Electric()

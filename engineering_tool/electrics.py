import math

class Power:
    
    """
        Function    : cirVoltageAndCurrentcle
        Description : This function to calculate power.
        Formula     : V x I
        Input       : 
                      - Voltage(V) number type integer or float
                      - Current(I) number type integer or float
        Return      : Power in type interger or float
        Example     : VoltageAndCurrent(2,2)
                    >> 4
    """
    def VoltageAndCurrent(voltage,current):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if current < 0:
            raise ValueError("The current cannot be negative.")

        return voltage * current
    
    """
        Function    : VoltageAndResistance
        Description : This function to calculate power.
        Formula     : V^2 / R
        Input       : 
                      - Voltage(V) number type integer or float
                      - Resistance(R) number type integer or float
        Return      : Power in type interger or float
        Example     : VoltageAndResistance(2,2)
                    >> 2
    """
    def VoltageAndResistance(voltage,resistance):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if resistance <= 0:
            raise ValueError("The resistance cannot be negative.")

        return (voltage**2) / resistance
    
    """
        Function    : ResistanceAndCurrent
        Description : This function to calculate power.
        Formula     : I^2 x R
        Input       : 
                      - Current(I) number type integer or float
                      - Resistance(R) number type integer or float
        Return      : Power in type interger or float
        Example     : ResistanceAndCurrent(2,2)
                    >> 8
    """
    def ResistanceAndCurrent(resistance,current):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if resistance < 0:
            raise ValueError("The resistance cannot be negative.")

        return resistance * current**2
    
    """
        Function    : kWDC
        Description : This function to calculate power in Kilowatt DC.
        Formula     : (I x V) / 1000
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage DC(V) number type integer or float
        Return      : Power kW in type interger or float
        Example     : kWDC(4,250)
                    >> 1
    """
    def kWDC(current,voltage):

        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")

        return (current * voltage) / 1000
    
    """
        Function    : kWOnePhaseAC
        Description : This function to calculate power in Kilowatt AC 1 Phase.
                      115 , 208 , 220 , 230 ,240 volt
        Formula     : (I x E x PF) / 1000
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Power factor(PF) number type integer or float
        Return      : Power kW in type interger or float
        Example     : kWOnePhaseAC(4,250,1)
                    >> 1
    """
    def kWOnePhaseAC(current,voltage,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The power factor must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if PF < 0:
            raise ValueError("The power factor cannot be negative.")

        return (current * voltage * PF) / 1000
    
    """
        Function    : kWThreePhaseAC
        Description : This function to calculate power in Kilowatt AC 3 Phase.
                      all volt
        Formula     : (I x E x PF x 1.73) / 1000
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Power factor(PF) number type integer or float
        Return      : Power kW in type interger or float
        Example     : kWThreePhaseAC(4,250,1)
                    >> 1.73
    """
    def kWThreePhaseAC(current,voltage,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The power factor must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if PF < 0:
            raise ValueError("The power factor cannot be negative.")

        return (current * voltage * PF * 1.73) / 1000
    
    """
        Function    : kVAOnePhaseAC
        Description : This function to calculate power in KiloVoltAmp AC 1 Phase.
                      115 , 208 , 220 , 230 ,240 volt
        Formula     : (I x E ) / 1000
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
        Return      : Power kVA in type interger or float
        Example     : kVAOnePhaseAC(4,250)
                    >> 1
    """
    def kVAOnePhaseAC(current,voltage):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
       
        if current < 0:
            raise ValueError("The current cannot be negative.")
        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")

        return (current * voltage) / 1000

    """
        Function    : kVAThreePhaseAC
        Description : This function to calculate power in KiloVoltAmp AC 3 Phase.
                      all volt
        Formula     : (I x E x 1.73) / 1000
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
        Return      : Power kVA in type interger or float
        Example     : kVAThreePhaseAC(4,250)
                    >> 1.73
    """
    def kVAThreePhaseAC(current,voltage):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
       
        if current < 0:
            raise ValueError("The current cannot be negative.")
        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")

        return (current * voltage * 1.73) / 1000

class Current:

    """
        Function    : PowerAndResistance
        Description : This function to calculate current.
        Formula     : I^2 x R
        Input       : 
                      - Power(W) number type integer or float
                      - Resistance(R) number type integer or float
        Return      : Current in type interger or float
        Example     : PowerAndResistance(8,2)
                    >> 2
    """
    def PowerAndResistance(power,resistance):
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")

        if power < 0:
            raise ValueError("The power cannot be negative.")
        if resistance <= 0:
            raise ValueError("The resistance cannot be negative.")

        return math.sqrt(power/resistance)
    
    """
        Function    : PowerAndVoltage
        Description : This function to calculate current.
        Formula     : P / V
        Input       : 
                      - Power(W) number type integer or float
                      - Voltage(R) number type integer or float
        Return      : Current in type interger or float
        Example     : PowerAndVoltage(8,2)
                    >> 4
    """
    def PowerAndVoltage(power,voltage):
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")

        if power < 0:
            raise ValueError("The power cannot be negative.")
        if voltage <= 0:
            raise ValueError("The voltage cannot be negative.")

        return power / voltage
    
    """
        Function    : VoltageAndResistance
        Description : This function to calculate current.
        Formula     : V / R
        Input       : 
                      - Voltage(V) number type integer or float
                      - Resistance(R) number type integer or float
        Return      : Current in type interger or float
        Example     : VoltageAndResistance(8,2)
                    >> 4
    """
    def VoltageAndResistance(voltage,resistance):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if resistance <= 0:
            raise ValueError("The resistance cannot be negative.")

        return voltage / resistance
    
    """
        Function    : HPAndVoltageAndEfficiencyDC
        Description : This function to calculate current DC.
        Formula     : ( HP x 746 ) / ( E x Eff )
        Input       : 
                      - Voltage(E) number type integer or float
                      - Hosepower(HP) number type integer or float
                      - Efficiency(Eff) number type integer or float
        Return      : Current in type interger or float
        Example     : HPAndVoltageAndEfficiencyDC(1,1,1)
                    >> 746
    """
    def HPAndVoltageAndEfficiencyDC(HP,E,Eff):

        if type(HP) not in [int,float]:
            raise TypeError("The HP must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")
        
        if HP < 0:
            raise ValueError("The HP cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")

        return (HP*746)/(E*Eff)
    
    """
        Function    : HPAndVoltageAndEfficiencyPFOnePhaseAC
        Description : This function to calculate current 1 Phase AC.
        Formula     : ( HP x 746 ) / ( E x Eff x PF )
        Input       : 
                      - Voltage(E) number type integer or float
                      - Hosepower(HP) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Current in type interger or float
        Example     : HPAndVoltageAndEfficiencyPFOnePhaseAC(1,1,1,1)
                    >> 746
    """
    def HPAndVoltageAndEfficiencyPFOnePhaseAC(HP,E,Eff,PF):
        if type(HP) not in [int,float]:
            raise TypeError("The HP must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")
        
        if HP < 0:
            raise ValueError("The HP cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (HP*746)/(E*Eff*PF)
    
    """
        Function    : HPAndVoltageAndEfficiencyPFThreePhaseAC
        Description : This function to calculate current 3 Phase AC.
        Formula     : ( HP x 746 ) / ( 1.73 x E x Eff x PF )
        Input       : 
                      - Voltage(E) number type integer or float
                      - Hosepower(HP) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Current in type interger or float
        Example     : HPAndVoltageAndEfficiencyPFThreePhaseAC(1,1,1,1)
                    >> 431.21
    """
    def HPAndVoltageAndEfficiencyPFThreePhaseAC(HP,E,Eff,PF):
        if type(HP) not in [int,float]:
            raise TypeError("The HP must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")
        
        if HP < 0:
            raise ValueError("The HP cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (HP*746)/(1.73*E*Eff*PF)
    
    """
        Function    : kWAndVoltageAndPFOnePhaseAC
        Description : This function to calculate current 1 Phase AC.
        Formula     : ( kW x 1000 ) / ( E x PF )
        Input       : 
                      - Power(kW) number type integer or float
                      - Voltage(E) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Current in type interger or float
        Example     : kWAndVoltageAndPFOnePhaseAC(1,1,1)
                    >> 1000
    """
    def kWAndVoltageAndPFOnePhaseAC(kW,E,PF):
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")
        
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kW < 0:
            raise ValueError("The power cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (kW * 1000)/(E*PF)
    
    """
        Function    : kWAndVoltageAndPFThreePhaseAC
        Description : This function to calculate current 3 Phase AC.
        Formula     : ( kW x 1000 ) / ( 1.73 x E x PF )
        Input       : 
                      - Power(kW) number type integer or float
                      - Voltage(E) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Current in type interger or float
        Example     : kWAndVoltageAndPFThreePhaseAC(1,1,1)
                    >> 578.03
    """
    def kWAndVoltageAndPFThreePhaseAC(kW,E,PF):
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")
        
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kW < 0:
            raise ValueError("The power cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (kW * 1000)/(1.73*E*PF)
    
    """
        Function    : kVAAndVoltageOnePhaseAC
        Description : This function to calculate current 1 Phase AC.
        Formula     : ( kVA x 1000 ) / E
        Input       : 
                      - Power(kVA) number type integer or float
                      - Voltage(E) number type integer or float
        Return      : Current in type interger or float
        Example     : kVAAndVoltageOnePhaseAC(1,1)
                    >> 1000
    """
    def kVAAndVoltageOnePhaseAC(kVA,E):
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kVA) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kVA < 0:
            raise ValueError("The power cannot be negative.")

        return (kVA*1000)/E
    
    """
        Function    : kVAAndVoltageThreePhaseAC
        Description : This function to calculate current 3 Phase AC.
        Formula     : ( kVA x 1000 ) / ( 1.763 x E )
        Input       : 
                      - Power(kVA) number type integer or float
                      - Voltage(E) number type integer or float
        Return      : Current in type interger or float
        Example     : kVAAndVoltageThreePhaseAC(1,1)
                    >> 567.21
    """
    def kVAAndVoltageThreePhaseAC(kVA,E):
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kVA) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kVA < 0:
            raise ValueError("The power cannot be negative.")

        return (kVA*1000)/(1.763*E)

class Resistance:

    """
        Function    : VoltageAndPower
        Description : This function to calculate resistance.
        Formula     : V^2 / P
        Input       : 
                      - Voltage(V) number type integer or float
                      - Power(P) number type integer or float
        Return      : Resistance in type interger or float
        Example     : VoltageAndPower(2,2)
                    >> 2
    """
    def VoltageAndPower(voltage,power):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if power <= 0:
            raise ValueError("The power cannot be negative.")

        return (voltage**2) / power
    
    """
        Function    : PowerAndCurrent
        Description : This function to calculate resistance.
        Formula     : P / I^2
        Input       : 
                      - Current(I) number type integer or float
                      - Power(P) number type integer or float
        Return      : Resistance in type interger or float
        Example     : PowerAndCurrent(4,2)
                    >> 1
    """
    def PowerAndCurrent(power,current):
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if power < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")

        return power / (current**2)
    
    """
        Function    : VoltageAndCurrent
        Description : This function to calculate resistance.
        Formula     : V / I
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage(V) number type integer or float
        Return      : Resistance in type interger or float
        Example     : VoltageAndCurrent(4,2)
                    >> 2
    """
    def VoltageAndCurrent(voltage,current):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")

        return voltage / current

class Voltage:

    """
        Function    : CurrentAndResistance
        Description : This function to calculate voltage.
        Formula     : I x R
        Input       : 
                      - Current(I) number type integer or float
                      - Resistance(R) number type integer or float
        Return      : Voltage in type interger or float
        Example     : CurrentAndResistance(4,2)
                    >> 8
    """
    def CurrentAndResistance(current,resistance):
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if resistance < 0:
            raise ValueError("The resistance cannot be negative.")
        if current < 0:
            raise ValueError("The current cannot be negative.")

        return current * resistance
    
    """
        Function    : PowerAndCurrent
        Description : This function to calculate voltage.
        Formula     : P / I
        Input       : 
                      - Current(I) number type integer or float
                      - Power(P) number type integer or float
        Return      : Voltage in type interger or float
        Example     : PowerAndCurrent(4,2)
                    >> 2
    """
    def PowerAndCurrent(power,current):
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if power < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")

        return power / current
    
    """
        Function    : PowerAndResistance
        Description : This function to calculate voltage.
        Formula     : Sqrt(PxR)
        Input       : 
                      - Resistance(R) number type integer or float
                      - Power(P) number type integer or float
        Return      : Voltage in type interger or float
        Example     : PowerAndResistance(2,2)
                    >> 2
    """
    def PowerAndResistance(power,resistance):
        if type(power) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")

        if power < 0:
            raise ValueError("The power cannot be negative.")
        if resistance < 0:
            raise ValueError("The resistance cannot be negative.")

        return math.sqrt(power * resistance)
    
    """
        Function    : HPAndEfficiencyAndCurrentDC
        Description : This function to calculate voltage DC.
        Formula     : ( HP x 746 ) / ( I x Eff ) 
        Input       : 
                      - Hosepower(HP) number type integer or float
                      - Current(I) number type integer or float
                      - Efficiency(Eff) number type integer or float
        Return      : Voltage DC in type interger or float
        Example     : HPAndEfficiencyAndCurrentDC(1,1,1)
                    >> 746
    """
    def HPAndEfficiencyAndCurrentDC(HP,current,Eff):
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")

        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")

        return (HP*746)/(current*Eff)
    
    """
        Function    : HPAndEfficiencyAndCurrentAndPFOnePhaseAC
        Description : This function to calculate voltage 1 phase AC.
        Formula     : ( HP x 746 ) / ( I x Eff x PF ) 
        Input       : 
                      - Hosepower(HP) number type integer or float
                      - Current(I) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power FActor(PF) number type integer or float
        Return      : Voltage AC 1 phase in type interger or float
        Example     : HPAndEfficiencyAndCurrentAndPFOnePhaseAC(1,1,1,1)
                    >> 746
    """
    def HPAndEfficiencyAndCurrentAndPFOnePhaseAC(HP,current,Eff,PF):
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")

        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (HP*746)/(current*Eff*PF)
    
    """
        Function    : HPAndEfficiencyAndCurrentAndPFThreePhaseAC
        Description : This function to calculate voltage 3 phase AC.
        Formula     : ( HP x 746 ) / ( 1.73 x I x Eff x PF ) 
        Input       : 
                      - Hosepower(HP) number type integer or float
                      - Current(I) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Voltage AC 3 phase in type interger or float
        Example     : HPAndEfficiencyAndCurrentAndPFThreePhaseAC(1,1,1,1)
                    >> 431.21
    """
    def HPAndEfficiencyAndCurrentAndPFThreePhaseAC(HP,current,Eff,PF):
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")

        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if Eff <= 0:
            raise ValueError("The efficiency cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (HP*746)/(1.73*current*Eff*PF)
    
    """
        Function    : kWAndCurrentAndPFOnePhaseAC
        Description : This function to calculate voltage 1 phase AC.
        Formula     : ( kW x 1000 ) / ( I x PF ) 
        Input       : 
                      - Power(kW) number type integer or float
                      - Current(I) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Voltage AC 1 phase in type interger or float
        Example     : kWAndCurrentAndPFOnePhaseAC(1,1,1)
                    >> 1000
    """
    def kWAndCurrentAndPFOnePhaseAC(kW,current,PF):
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")

        if kW < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (kW*1000)/(current*PF)
    
    """
        Function    : kWAndCurrentAndPFThreePhaseAC
        Description : This function to calculate voltage 3 phase AC.
        Formula     : ( kW x 1000 ) / ( 1.73 x I x PF ) 
        Input       : 
                      - Power(kW) number type integer or float
                      - Current(I) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Voltage AC 3 phase in type interger or float
        Example     : kWAndCurrentAndPFThreePhaseAC(1,1,1)
                    >> 578.03
    """
    def kWAndCurrentAndPFThreePhaseAC(kW,current,PF):
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The powerfactor must be a non-negative real number.")

        if kW < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if PF <= 0:
            raise ValueError("The powerfactor cannot be negative.")

        return (kW*1000)/(1.73*current*PF)
    
    """
        Function    : kVAAndCurrentOnePhaseAC
        Description : This function to calculate voltage 1 phase AC.
        Formula     : ( kVA x 1000 ) / I 
        Input       : 
                      - Power(kVA) number type integer or float
                      - Current(I) number type integer or float
        Return      : Voltage AC 1 phase in type interger or float
        Example     : kVAAndCurrentOnePhaseAC(1,1)
                    >> 1000
    """
    def kVAAndCurrentOnePhaseAC(kVA,current):
        if type(kVA) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if kVA < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")

        return (kVA*1000)/current
    
    """
        Function    : kVAAndCurrentThreePhaseAC
        Description : This function to calculate voltage 3 phase AC.
        Formula     : ( kVA x 1000 ) / ( 1.763 x I ) 
        Input       : 
                      - Power(kVA) number type integer or float
                      - Current(I) number type integer or float
        Return      : Voltage AC 3 phase in type interger or float
        Example     : kVAAndCurrentOnePhaseAC(1,1)
                    >> 567.21
    """
    def kVAAndCurrentThreePhaseAC(kVA,current):
        if type(kVA) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")

        if kVA < 0:
            raise ValueError("The power cannot be negative.")
        if current <= 0:
            raise ValueError("The current cannot be negative.")

        return (kVA*1000)/(1.763*current)
    
    """
        Function    : CoulombAndFarad
        Description : This function to calculate voltage.
        Formula     : Q/C
        Input       : 
                      - Coulomb(Q) number type integer or float
                      - Capacitance(C) number type integer or float
        Return      : Voltage in type interger or float
        Example     : CoulombAndFarad(1,1)
                    >> 1
    """
    def CoulombAndFarad(coulomb,farad):
        if type(coulomb) not in [int,float]:
            raise TypeError("The coulomb must be a non-negative real number.")
        if type(farad) not in [int,float]:
            raise TypeError("The farad must be a non-negative real number.")

        if coulomb <= 0:
            raise ValueError("The coulomb cannot be negative.")
        if farad <= 0:
            raise ValueError("The farad cannot be negative.")

        return coulomb / farad
    
class Conductance:

    """
        Function    : Resistance
        Description : This function to calculate conductance.
        Formula     : 1 / R
        Input       : 
                      - Resistance(R) number type integer or float
        Return      : Conductance in type interger or float
        Example     : Resistance(2)
                    >> 0.5
    """
    def Resistance(resistance):
        if type(resistance) not in [int,float]:
            raise TypeError("The resistance must be a non-negative real number.")
       
        if resistance <= 0:
            raise ValueError("The resistance cannot be negative.")
      
        return 1 / resistance
    
    """
        Function    : VoltageAndCurrent
        Description : This function to calculate conductance.
        Formula     : I/V
        Input       : 
                      - Voltage(V) number type integer or float
                      - Current(I) number type integer or float
        Return      : Conductance in type interger or float
        Example     : VoltageAndCurrent(2,2)
                    >> 1
    """
    def VoltageAndCurrent(voltage,currrent):

        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(currrent) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
       
        if voltage <= 0:
            raise ValueError("The voltage cannot be negative.")
        if currrent <= 0:
            raise ValueError("The current cannot be negative.")

        return currrent / voltage

class Capacitance:

    """
        Function    : Farad
        Description : This function to calculate capacitance.
        Formula     : Q / V
        Input       : 
                      - Coulomb(Q) number type integer or float
                      - Voltage(V) number type integer or float
        Return      : Capacitance in type interger or float
        Example     : Farad(2,2)
                    >> 1
    """
    def Farad(coulomb,voltage):
        if type(coulomb) not in [int,float]:
            raise TypeError("The coulomb must be a non-negative real number.")
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")

        if voltage <= 0:
            raise ValueError("The voltage cannot be negative.")
        if coulomb < 0:
            raise ValueError("The coulomb cannot be negative.")

        return coulomb / voltage
    
    """
        Function    : Coulomb
        Description : This function to calculate charge.
        Formula     : C x V
        Input       : 
                      - Capacitance(C) number type integer or float
                      - Voltage(V) number type integer or float
        Return      : Charge in type interger or float
        Example     : Coulomb(2,2)
                    >> 4
    """
    def Coulomb(farad,voltage):
        if type(voltage) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(farad) not in [int,float]:
            raise TypeError("The farad must be a non-negative real number.")

        if voltage < 0:
            raise ValueError("The voltage cannot be negative.")
        if farad < 0:
            raise ValueError("The farad cannot be negative.")

        return farad * voltage
    
class Frequency:

    """
        Function    : Hertz
        Description : This function to calculate frequency.
        Formula     : 1 / T
        Input       : 
                      - Period(T) number type integer or float
        Return      : Frequency in type interger or float
        Example     : Hertz(1)
                    >> 1
    """
    def Hertz(T):
        if type(T) not in [int,float]:
            raise TypeError("The T must be a non-negative real number.")
        
        if T <= 0:
            raise ValueError("The T cannot be negative.")

        return 1 / T
    
    """
        Function    : Sec
        Description : This function to calculate period.
        Formula     : 1 / f
        Input       : 
                      - Frequency(f) number type integer or float
        Return      : Period in type interger or float
        Example     : Sec(1)
                    >> 1
    """
    def Sec(f):
        if type(f) not in [int,float]:
            raise TypeError("The frequency must be a non-negative real number.")
    
        if f <= 0:
            raise ValueError("The frequency cannot be negative.")
        
        return 1 / f

class Hosepower:

    """
        Function    : DC
        Description : This function to calculate Hosepower in HP DC.
        Formula     : (I x E x Eff ) / 746
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Efficiency(Eff) number type integer or float
        Return      : HP in type interger or float
        Example     : DC(1,746,1)
                    >> 1
    """
    def DC(current,E,Eff):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The Efficiency must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if E < 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff < 0:
            raise ValueError("The Efficiency cannot be negative.")

        return (current * E * Eff) / 746
    
    """
        Function    : OnePhaseAC
        Description : This function to calculate Hosepower in HP 1 Phase AC.
                      115 , 208 , 220 , 230 ,240 volt
        Formula     : (I x E x Eff x PF  ) / 746
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power factor(PF) number type integer or float
        Return      : HP in type interger or float
        Example     : OnePhaseAC(1,746,1,1)
                    >> 1
    """
    def OnePhaseAC(current,E,Eff,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The Efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The Power factor must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if E < 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff < 0:
            raise ValueError("The Efficiency cannot be negative.")
        if PF < 0:
            raise ValueError("The Power factor cannot be negative.")

        return (current * E * Eff * PF) / 746
    
    """
        Function    : ThreePhaseAC
        Description : This function to calculate Hosepower in HP 3 Phase AC.
                      all volt
        Formula     : (1.73 x I x E x Eff x PF  ) / 746
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Power factor(PF) number type integer or float
        Return      : HP in type interger or float
        Example     : OnePhaseAC(1,746,1,1)
                    >> 1.73
    """
    def ThreePhaseAC(current,E,Eff,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The Efficiency must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The Power factor must be a non-negative real number.")

        if current < 0:
            raise ValueError("The current cannot be negative.")
        if E < 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff < 0:
            raise ValueError("The Efficiency cannot be negative.")
        if PF < 0:
            raise ValueError("The Power factor cannot be negative.")

        return (1.73 * current * E * Eff * PF) / 746

class Powerfactor:

    """
        Function    : HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC
        Description : This function to calculate Powerfactor in 1 Phase AC.
        Formula     : ( HP x 746 ) / ( E x Eff x I )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Hosepower(HP) number type integer or float
        Return      : Power Factor in type interger or float
        Example     : HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC(1,1,1,1)
                    >> 746
    """
    def HPAndVoltageAndEfficiencyAndCurrentOnePhaseAC(HP,current,E,Eff):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The Efficiency must be a non-negative real number.")
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff <= 0:
            raise ValueError("The Efficiency cannot be negative.")
        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")

        return (HP*746)/(E*Eff*current)
    
    """
        Function    : HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC
        Description : This function to calculate Powerfactor in 3 Phase AC.
        Formula     : ( HP x 746 ) / ( 1.73 x E x Eff x I )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Efficiency(Eff) number type integer or float
                      - Hosepower(HP) number type integer or float
        Return      : Power Factor in type interger or float
        Example     : HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC(1,1,1,1)
                    >> 431.21
    """
    def HPAndVoltageAndEfficiencyAndCurrentThreePhaseAC(HP,current,E,Eff):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(Eff) not in [int,float]:
            raise TypeError("The Efficiency must be a non-negative real number.")
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if Eff <= 0:
            raise ValueError("The Efficiency cannot be negative.")
        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")

        return (HP*746)/(1.73*E*Eff*current)
    
    """
        Function    : kWAndCurrentAndVoltageOnePhaseAC
        Description : This function to calculate Powerfactor in 1 Phase AC.
        Formula     : ( kW x 1000 ) / ( I x E )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Power(kW) number type integer or float
        Return      : Power Factor in type interger or float
        Example     : kWAndCurrentAndVoltageOnePhaseAC(1,1,1)
                    >> 1000
    """
    def kWAndCurrentAndVoltageOnePhaseAC(kW,current,E):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kW < 0:
            raise ValueError("The power cannot be negative.")

        return (kW*1000)/(current*E)
    
    """
        Function    : kWAndCurrentAndVoltageThreePhaseAC
        Description : This function to calculate Powerfactor in 3 Phase AC.
        Formula     : ( kW x 1000 ) / ( 1.73 x I x E )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Power(kW) number type integer or float
        Return      : Power Factor in type interger or float
        Example     : kWAndCurrentAndVoltageThreePhaseAC(1,1,1)
                    >> 578.03
    """
    def kWAndCurrentAndVoltageThreePhaseAC(kW,current,E):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(kW) not in [int,float]:
            raise TypeError("The power must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if kW < 0:
            raise ValueError("The power cannot be negative.")

        return (kW*1000)/(1.73*current*E)

class Efficiency:

    """
        Function    : DC
        Description : This function to calculate Efficiency DC.
        Formula     : ( HP x 746 X / ( E x I )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Hosepower(HP) number type integer or float
        Return      : Efficiency in type interger or float
        Example     : DC(1,1,1)
                    >> 746
    """
    def DC(HP,E,current):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")

        return (HP*746)/(E*current)
    
    """
        Function    : OnePhaseAC
        Description : This function to calculate Efficiency 1 phase AC.
        Formula     : ( HP x 746 X / ( E x I x PF )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Hosepower(HP) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Efficiency in type interger or float
        Example     : OnePhaseAC(1,1,1,1)
                    >> 746
    """
    def OnePhaseAC(HP,E,current,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The power factor must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")
        if PF <= 0:
            raise ValueError("The power factor cannot be negative.")

        return (HP*746)/(E*PF*current)
    
    """
        Function    : ThreePhaseAC
        Description : This function to calculate Efficiency 3 phase AC.
        Formula     : ( HP x 746 X / ( 1.73 x E x I x PF )
        Input       : 
                      - Current(I) number type integer or float
                      - Voltage AC(E) number type integer or float
                      - Hosepower(HP) number type integer or float
                      - Power Factor(PF) number type integer or float
        Return      : Efficiency in type interger or float
        Example     : ThreePhaseAC(1,1,1,1)
                    >> 431.21
    """
    def ThreePhaseAC(HP,E,current,PF):
        if type(current) not in [int,float]:
            raise TypeError("The current must be a non-negative real number.")
        if type(E) not in [int,float]:
            raise TypeError("The voltage must be a non-negative real number.")
        if type(HP) not in [int,float]:
            raise TypeError("The hosepower must be a non-negative real number.")
        if type(PF) not in [int,float]:
            raise TypeError("The power factor must be a non-negative real number.")

        if current <= 0:
            raise ValueError("The current cannot be negative.")
        if E <= 0:
            raise ValueError("The voltage cannot be negative.")
        if HP < 0:
            raise ValueError("The hosepower cannot be negative.")
        if PF <= 0:
            raise ValueError("The power factor cannot be negative.")

        return (HP*746)/(1.73*E*PF*current)
    

    
    
    
    

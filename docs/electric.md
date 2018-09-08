# Definition
**Electricity** is the set of physical phenomena associated with the presence and motion of electric charge. Although initially considered a phenomenon separate from magnetism, since the development of Maxwell's equations, both are recognized as part of a single phenomenon: electromagnetism. Various common phenomena are related to electricity, including lightning, static electricity, electric heating, electric discharges and many others.

# Units of measurement

- Electric power :  **Watt**
- Hose power : **HP**
- Electric volt : **Volt**
- Electric current : **Amp**
- Electric resistant : **Ohm**
- Electric conductance : **Mho**
- Electric capacitance : **Farad**
- Frequency : **Hertz**
- Power Factor : **PF**
- Efficiency : **Eff**

# 1. Find power

![P = VI = \frac{V^2}{R} = {I^2}{R} ](https://latex.codecogs.com/svg.latex?P%20=%20VI%20=%20\frac{V^2}{R}%20=%20{I^2}{R})

**V** = Voltage
**I**  = Electric current 
**R** = Resistance

**Example**

```python
from engineering_tool.electrics import Power

V = 30.5 # Volt
I = 2.5  # Amp
R = 1500 # Ohm

P1 = Power.VoltageAndCurrent(V,I)
P2 = Power.VoltageAndResistance(V,R)
P3 = Power.ResistanceAndCurrent(R,I)
P4 = Power.KwDC(I,R)

print("Power is %.2f W"%P1)
print("Power is %.2f W"%P2)
print("Power is %.2f W"%P3)
print("Power is %.2f Kw"%P4)
```

1 phase AC

![P = \frac{I\cdot E \cdot PF}{1000}](https://latex.codecogs.com/svg.latex?P%20=%20\frac{I\cdot%20E%20\cdot%20PF}{1000})

**I**  = AC current
**E** = AC voltage
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Power

I  = 15.7  # Amp rms
E  = 230.5 # Volt rms
PF = 0.78  # PF 

Power_1P = Power.kWOnePhaseAC(I,E,PF)
print("Power is %.2f kW"%Power_1P)
```

3 phase AC 

![P = \frac{1.73 \cdot I \cdot E \cdot PF}{1000}](https://latex.codecogs.com/svg.latex?P%20=%20\frac{1.73%20\cdot%20I%20\cdot%20E%20\cdot%20PF}{1000})

**I**  = AC current
**E** = AC voltage
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Power

I  = 15.7  # Amp rms
E  = 230.5 # Volt rms
PF = 0.78  # PF 
Power_3P = Power.kWThreePhaseAC(I,E,PF)
print("Power is %.2f kW"%Power_3P)
```

1 phase AC , Known **kVA**

![P = kVA \cdot PF](https://latex.codecogs.com/svg.latex?P%20=%20kVA%20\cdot%20PF)

**P**  = Power : KiloWatt
**kVA** = KiloVoltAmp
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Power

kVA  = 150.7  # kVA
PF = 0.78  # PF 
Power_1P = Power.kVAOnePhaseAC(kVA,PF)
print("Power is %.2f kW"%Power_1P)
```

3 phase AC , Known **kVA**

![](https://latex.codecogs.com/svg.latex?P%20=%20kVA%20\cdot%20PF\cdot{1.73})

**P**  = Power : KiloWatt
**kVA** = KiloVoltAmp
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Power

kVA  = 150.7  # kVA
PF = 0.78  # PF 
Power_3P = Power.kVAThreePhaseAC(kVA,PF)
print("Power is %.2f kW"%Power_3P)
```

# 2.Find current

![I = \sqrt{\frac{P}{R}}=\frac{P}{V}=\frac{V}{R}](https://latex.codecogs.com/svg.latex?I%20=%20\sqrt{\frac{P}{R}}=\frac{P}{V}=\frac{V}{R})

**I** = Current
**P** = Power
**R** = Resistance
**V** = Voltage

**Example**

```python
from engineering_tool.electrics import Current

V = 30.5  # Volt
P = 1000  # Watt
R = 1500  # Ohm

I1 = Current.PowerAndResistance(P,R)
I2 = Current.PowerAndVoltage(P,V)
I3 = Current.VoltageAndResistance(V,R)

print("Current is %.2f A"%I1)
print("Current is %.2f A"%I2)
print("Current is %.2f A"%I3)
```

**Current DC** , Known , HP

![I = \frac{HP\cdot{746}}{E\cdot Eff}](https://latex.codecogs.com/svg.latex?I%20=%20\frac{HP\cdot{746}}{E\cdot%20Eff})

**HP** = Hose power
**E**    = Voltage
**Eff** = Efficiency

**Example**

```python
from engineering_tool.electrics import Current

E = 30.5  # Volt
HP = 1.5  # Hp
Eff = 0.7  

I = Current.HPAndVoltageAndEfficiencyDC(HP,E,Eff)
print("Current is %.2f A"%I)
```

**Current 1 phase AC** , Known , HP

![I = \frac{HP\cdot 746}{E\cdot Eff \cdot PF}](https://latex.codecogs.com/svg.latex?I%20=%20\frac{HP\cdot%20746}{E\cdot%20Eff%20\cdot%20PF})

**I** = Current
**HP** = Hose power
**E** = Voltage AC
**Eff** = Efficiency
**PF** = Power factor

**Example**

```python
from engineering_tool.electrics import Current

E = 30.5  # Volt
HP = 1.5  # Hp
Eff = 0.7
PF = 0.8  
I = Current.HPAndVoltageAndEfficiencyPFOnePhaseAC(HP,E,Eff,PF)
print("Current is %.2f A"%I)
```
**Current 3 phase AC** , Known , HP

![](https://latex.codecogs.com/svg.latex?I%20=%20\frac{HP\cdot%20746}{1.73\cdot%20E\cdot%20Eff%20\cdot%20PF})

**I** = Current
**HP** = Hose power
**E** = Voltage AC
**Eff** = Efficiency
**PF** = Power factor

**Example**

```python
from engineering_tool.electrics import Current

E = 30.5  # Volt
HP = 1.5  # Hp
Eff = 0.7
PF = 0.8  
I = Current.HPAndVoltageAndEfficiencyPFThreePhaseAC(HP,E,Eff,PF)
print("Current is %.2f A"%I)
```

**Current 1 phase AC** , Known , kW

![I =  \frac{kW\cdot 1000}{E\cdot PF}](https://latex.codecogs.com/svg.latex?I%20=%20\frac{kW\cdot%201000}{E\cdot%20PF})

**kW** = Power in KiloWatt
**E** = Voltage AC 1 phase
**PF** = Power factor

**Example**

```python
from engineering_tool.electrics import Current

kW = 3.5  # Kilowatt
E = 220  # Volt rms
PF = 0.8  
I = Current.kWAndVoltageAndPFOnePhaseAC(kW,E,PF)
print("Current is %.2f A"%I)
```

**Current 3 phase AC** , Known , kW

![I = \frac{kW\cdot 1000}{1.73\cdot E\cdot PF}](https://latex.codecogs.com/svg.latex?I%20=%20\frac{kW\cdot%201000}{1.73\cdot%20E\cdot%20PF})

**kW** = Power in KiloWatt
**E** = Voltage AC 3 phase
**PF** = Power factor

**Example**

```python
from engineering_tool.electrics import Current

kW = 3.5  # Kilowatt
E = 115  # Volt rms
PF = 0.8  
I = Current.kWAndVoltageAndPFThreePhaseAC(kW,E,PF)
print("Current is %.2f A"%I)
```

**Current 1 phase AC** , Known , kVA

![](https://latex.codecogs.com/svg.latex?I=%20\frac{kVA\cdot%201000}{E})

**kVA** = KiloVoltAmp
**E** = Voltage 1 phase AC

**Example**

```python
from engineering_tool.electrics import Current

kVA = 3.5  # KiloVoltAmp
E = 235  # Volt rms  
I = Current.kVAAndVoltageOnePhaseAC(kVA,E)
print("Current is %.2f A"%I)
```

# 3. Find resistance

![R = \frac{V^2}{P}=\frac{V}{I}=\frac{P}{I^2}](https://latex.codecogs.com/svg.latex?R%20=%20\frac{V^2}{P}=\frac{V}{I}=\frac{P}{I^2})

**V** = Voltage
**P** = Power
**I** = Current

**Example**

```python
from engineering_tool.electrics import Resistance

V = 12  # Volt
P = 500 # Watt
I = 2.5 # A
R1 = Resistance.VoltageAndPower(V,P)
R2 = Resistance.PowerAndCurrent(P,I)
R3 = Resistance.VoltageAndCurrent(V,I)

print("Resistance is %.2f Ohm"%R1)
print("Resistance is %.2f Ohm"%R2)
print("Resistance is %.2f Ohm"%R3)
```

# 3. Find resistance

![R = \frac{V^2}{P}=\frac{V}{I}=\frac{P}{I^2}](https://latex.codecogs.com/svg.latex?R%20=%20\frac{V^2}{P}=\frac{V}{I}=\frac{P}{I^2})

**V** = Voltage
**P** = Power
**I** = Current

**Example**

```python
from engineering_tool.electrics import Resistance

V = 12  # Volt
P = 500 # Watt
I = 2.5 # A
R1 = Resistance.VoltageAndPower(V,P)
R2 = Resistance.PowerAndCurrent(P,I)
R3 = Resistance.VoltageAndCurrent(V,I)

print("Resistance is %.2f Ohm"%R1)
print("Resistance is %.2f Ohm"%R2)
print("Resistance is %.2f Ohm"%R3)
```

# 4. Find voltage

![V = IR=\frac{P}{I}=\sqrt(PR)](https://latex.codecogs.com/svg.latex?V%20=%20IR=\frac{P}{I}=\sqrt(PR))

**I** = Current
**R** = Resistance
**P** = Power

**Example**

```python
from engineering_tool.electrics import Voltage

R = 1200  # Ohm
P = 500 # Watt
I = 2.5 # A

V1 = Voltage.CurrentAndResistance(I,R)
V2 = Voltage.PowerAndCurrent(P,I)
V3 = Voltage.PowerAndResistance(P,R)

print("Voltage is %.2f Volt"%V1)
print("Voltage is %.2f Volt"%V2)
print("Voltage is %.2f Volt"%V3)
```

**Voltage DC** , Known , HP

![V = \frac{HP\cdot 746}{I\cdot Eff}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{HP\cdot%20746}{I\cdot%20Eff})

**HP** = Hose power
**I** = Current DC
**Eff** = Efficiency

**Example**
```python
from engineering_tool.electrics import Voltage

HP = 1.5 # HP
Eff = 0.5 # Eff
I = 2.5 # A

V = Voltage.HPAndEfficiencyAndCurrentDC(HP,I,Eff)
print("Voltage is %.2f Volt"%V)
```

**Voltage 1 phase AC** , Known , HP

![V = \frac{HP\cdot 746}{I\cdot Eff\cdot PF}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{HP\cdot%20746}{I\cdot%20Eff\cdot%20PF})

**HP** = Hose power
**I** = Current
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Voltage

HP = 1.5 # HP
Eff = 0.5 # Eff
I = 2.5 # A
PF = 0.7
V = Voltage.HPAndEfficiencyAndCurrentAndPFOnePhaseAC(HP,I,Eff,PF)
print("Voltage is %.2f Volt"%V)
```

**Voltage 3 phase AC** , Known , HP

![V = \frac{HP\cdot 746}{1.73 \cdot I \cdot Eff \cdot PF}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{HP\cdot%20746}{1.73%20\cdot%20I%20\cdot%20Eff%20\cdot%20PF})

**HP**  = Hose power
**I** = Current
**Eff** = Efficiency
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Voltage

HP = 1.5 # HP
Eff = 0.5 # Eff
I = 2.5 # A
PF = 0.7
V = Voltage.HPAndEfficiencyAndCurrentAndPFThreePhaseAC(HP,I,Eff,PF)
print("Voltage is %.2f Volt"%V)
```

**Voltage 1 phase AC** , Known , kW

![V = \frac{kW\cdot1000}{I\cdot PF}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{kW\cdot1000}{I\cdot%20PF})

**kW** = Power in kilowatt
**I** = Current
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Voltage

kW = 1.5 # kW
I = 2.5 # A
PF = 0.7
V = Voltage.kWAndCurrentAndPFOnePhaseAC(kW,I,PF)
print("Voltage is %.2f Volt"%V)
```

**Voltage 3 phase AC** , Known , kW

![V = \frac{kW\cdot 1000}{1.73\cdot I \cdot PF}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{kW\cdot%201000}{1.73\cdot%20I%20\cdot%20PF})

**kW** = Power in kilowatt
**I** = Current
**PF** = Power factor

**Example**
```python
from engineering_tool.electrics import Voltage

kW = 1.5 # kW
I = 2.5 # A
PF = 0.7
V = Voltage.kWAndCurrentAndPFThreePhaseAC(kW,I,PF)
print("Voltage is %.2f Volt"%V)
```

**Voltage 1 phase AC** , Known , kVA

![V = \frac{kVA\cdot 1000}{I}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{kVA\cdot%201000}{I})

**kVA** = KiloVoltAmp
**I** = Current

**Example**
```python
from engineering_tool.electrics import Voltage

kVA = 1.5 # kVA
I = 2.5 # A
V = Voltage.kVAAndCurrentOnePhaseAC(kVA,I)
print("Voltage is %.2f Volt"%V)
```

**Voltage 3 phase AC** , Known , kVA

![V = \frac{kVA\cdot 1000}{1.763\cdot I }](https://latex.codecogs.com/svg.latex?V%20=%20\frac{kVA\cdot%201000}{1.763\cdot%20I%20})

**kVA** = KiloVoltAmp
**I** = Current

**Example**
```python
from engineering_tool.electrics import Voltage

kVA = 1.5 # kVA
I = 2.5 # A
V = Voltage.kVAAndCurrentThreePhaseAC(kVA,I)
print("Voltage is %.2f Volt"%V)
```

**Voltage ** , Known **Q,C**

![V = \frac{Q}{C}](https://latex.codecogs.com/svg.latex?V%20=%20\frac{Q}{C})

**Q** = Coulomb
**C** = Capacitance

**Example**
```python
from engineering_tool.electrics import Voltage

Q = 1.5 # Coulomb
C = 2.5 # Farad
V = Voltage.CoulombAndFarad(Q,C)
print("Voltage is %.2f Volt"%V)
```






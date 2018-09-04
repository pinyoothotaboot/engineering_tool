from engineering_tool.electrics import Power


V = 15
I =2

P = Power.VoltageAndCurrent(V,I)

print("Power is %f"%P)
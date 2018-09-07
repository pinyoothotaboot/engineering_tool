# Engineering Tool

The tool is a physic formula for Engineering or Science : **Python 3.6+**.


# Features
- Area Formula
- Volume Formula
- Electric Formula
- Pressure Formula
- Temperature Formula 

# Setup
- First : Check python version and PIP version
![](docs/images/check_version.png?raw=true)
- Second : Install lib engineering-tool
![](docs/images/install.png?raw=true)
- Third : Test lib in python shell
![](docs/images/example.png?raw=true)

# Example

```python
from engineering_tool.electrics import Power
voltage = 15 # Volt
current = 2.5 # Amp
power = Power.VoltageAndCurrent(voltage,current)
print("Power is %.2f Watt"%power)
```

# Documentation
The Engineering tool [documentation](https://github.com/pinyoothotaboot/engineering_tool/tree/master/docs) is the best place to start.after that try opening an issue.
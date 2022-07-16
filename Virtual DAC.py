voltage_max = 12
binary_max = 1023

def dac(binary_value):
    conversion = voltage_max/binary_max
    voltage = float(binary_value)*conversion
    return voltage

print(dac(binary_value=input("Please enter binary value!\n")))
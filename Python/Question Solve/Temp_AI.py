def Conversion(Celsius):
    Fahrenheit = (Celsius * 1.8) + 32 
    print("\n%.2f Celsius is equivalent to: %.2f Fahrenheit" %(Celsius,Fahrenheit))
    return Fahrenheit
def Check(Fahren_temp,Celsius_Temp):
    if (Fahren_temp < 32 and Celsius_Temp < 0 ):
        print("Temperature is below Freezing Point.\n")

    elif (Fahren_temp == 32 and Celsius_Temp == 0):
        print("Temperature is at Freezing Point.\n")

    else:
        print("Temperature is above Freezing Point.\n")

Celsius = float(input("Enter temperature in celsius: "))
Fahren = Conversion(Celsius)
Check(Fahren,Celsius)


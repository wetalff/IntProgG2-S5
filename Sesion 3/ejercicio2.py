#Bono
Sueldo = float(input("Ingrese el sueldo del empleado: "))

bono_10= Sueldo * 0.10
bono_5= Sueldo * 0.05
bono_sueldo_10 = Sueldo + bono_10
bono_sueldo_5 = Sueldo + bono_5

if Sueldo > 3000:
    print("Como el sueldo es mayor a 3000, especificamente: ", Sueldo," entonces el bono sera de: ",bono_10,"Y Sueldo con el bono sera de: ", bono_sueldo_10)
if Sueldo > 1500 and Sueldo <= 3000:
    print("Como el sueldo es mayor a 1500 pero menor a o igual a 3000, especificamente: ", Sueldo,"entonces el bono sera de: ",bono_5,"Y Sueldo con el bono sera de: ", bono_sueldo_5)
if Sueldo <= 1500:
    print("No tendra bono")
    
    

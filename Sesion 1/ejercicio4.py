#Cálculo del consumo de combustible
Distancia_Km = float(input("Ingrese la distancia recorrida en kilometros: "))
Ltrs_Consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
Rendimiento = Distancia_Km / Ltrs_Consumidos
Precio_Litro_en_Cordobas = 48.97
Gasto_Total_Combust = Ltrs_Consumidos * Precio_Litro_en_Cordobas
print(f"""
     Distancia recorrida en km: {Distancia_Km:>14} 
     Litros consumidos: {Ltrs_Consumidos:>21}
     Precio por litro en cordobas: {Precio_Litro_en_Cordobas:>11} cordobas
     El rendimiento del vehiculo es del: {Rendimiento} Km/L
     Gasto total de combustible: {Gasto_Total_Combust:>13} cordobas """)


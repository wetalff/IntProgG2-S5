#Cálculo del consumo de agua por persona
ltrs_Consum_mes_Vivienda = float(input("Ingrese la cantidad de litros consumidos en un mes en una vivienda: "))
Cant_Personas = int(input("Ingrese la cantidad de personas que viven en esa vivienda: "))
Consumo_Mensual_persona = ltrs_Consum_mes_Vivienda / Cant_Personas
Consumo_Diario_persona = Consumo_Mensual_persona / 30
print(f""" 
    Consumo total de agua en el mes: {ltrs_Consum_mes_Vivienda:>14}
    Cantidad total de personas en la vivienda: {Cant_Personas}
    Consumo mensual de agua por persona: {Consumo_Mensual_persona:>10}
    Consumo diario de agua por persona: {Consumo_Diario_persona:>11.2f}""")

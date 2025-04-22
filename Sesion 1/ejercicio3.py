#Cálculo de interés compuesto
Capital_inicial = float(input("Ingrese la cantidad inicial de capital: "))
Tasa_de_interes_anual = int(input("Ingrese la tasa de interes anual en porcentaje: "))
Años = int(input("Ingrese la cantidad de años: "))
interes_decimal = Tasa_de_interes_anual / 100
Monto_Final = ((1 + interes_decimal)**Años) * Capital_inicial
interes_Ganado = Monto_Final - Capital_inicial
print(f"""
      Capital inicial: {Capital_inicial:>10.0f}
      Tasa de interes anual: {Tasa_de_interes_anual}
      Años activo: {Años:>11}
      Monto final: {Monto_Final:>14.0f}
      Interes ganado: {interes_Ganado:>11.0f}""")


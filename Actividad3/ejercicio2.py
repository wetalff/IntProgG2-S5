# Control de inventario de un producto
Cantidad_inicial = int(input("Ingrese la cantidad inicial del producto en el inventario: "))
Produc_Recibido = int(input("Ingrese la cantidad de producto recibido: "))
Produc_Vendido = int(input("Ingrese la cantidad de producto vendido: "))
Suma = Produc_Recibido + Cantidad_inicial
Inventario_Actual = Suma - Produc_Vendido
print(f"""
      Inventario Inicial: {Cantidad_inicial}
      Producto Recibido: {Produc_Recibido:>3}
      Producto Vendido: {Produc_Vendido:>4}
      Inventario Actual: {Inventario_Actual:>3}""")


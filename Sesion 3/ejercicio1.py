#Calificaciones

calificacion = float(input("Dime tu calificación de la clase: "))

if calificacion >= 9 and calificacion <=10:
    print("Tu calificacion es A")
elif calificacion >= 7 and calificacion <=8:
    print("Tu calificacion es B")
elif calificacion >=5 and calificacion <=6:
    print("Tu calificacion es C")
elif calificacion >= 3 and calificacion <=4:
    print("Tu calificacion es D")
elif calificacion >= 0 and calificacion <=2:
    print("Tu calificacion es F")
else:
    print("Calificacion no valida")
    
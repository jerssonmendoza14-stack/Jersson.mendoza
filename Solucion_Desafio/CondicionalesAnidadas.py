print("Este programa mezcla dos colores.")
print("Colores disponibles: R: rojo A: azul")
primera = input("Elija un color (R o A): ")
if primera == "R":
    print("A.azul  V.verde")
    segunda = input("Elija otro color (A o V): ")
    if segunda == "A":
        print("La mezcla de rojo y azul es: Morado.")
    else:
        print("La mezcla de rojo y verde es: Amarillo.")
else:
    print("R.rojo  V.verde")
    segunda = input("Elija otro color (R o V): ")
    if segunda == "R":
        print("La mezcla de azul y rojo es: Morado.")
    else:
        print("La mezcla de azul y verde es: Cian.")
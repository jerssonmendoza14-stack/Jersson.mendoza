# Estructuras de control del prorama

velocidad = float(input("Ingrese su velovidad promedio: "))

while velocidad < 0:
    print("La velocidad no puede ser negativa, por favor ingrese un valor valido")
    velocidad = float(input("Ingrese su velovidad promedio: ")) 
if velocidad > 50:
    print("Usted esta excediendo el limite de velocidad")
elif velocidad < 20:
    print("Usted esta conduciendo muy lento")
else:    print("Usted esta conduciendo a una velocidad adecuada")   
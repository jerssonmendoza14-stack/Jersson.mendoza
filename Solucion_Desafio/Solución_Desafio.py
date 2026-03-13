# Programa para evaluar el promedio de un estudiante según sus calificaciones

# Solicitar las 5 calificaciones
Primera_nota = int(input("Estimado estudiante ingrese la primera nota: "))
while Primera_nota < 0 or Primera_nota > 100:
    print("La nota no puede ser menor a 0 ni mayor a 100, por favor ingrese un valor valido")
    Primera_nota = int(input("Estimado estudiante ingrese la primera nota: "))
Segunda_nota = int(input("Estimado estudiante ingrese la segunda nota: "))
while Segunda_nota < 0 or Segunda_nota > 100:
    print("La nota no puede ser menor a 0 ni mayor a 100, por favor ingrese un valor valido")
    Segunda_nota = int(input("Estimado estudiante ingrese la segunda nota: "))
Tercera_nota = int(input("Estimado estudiante ingrese la tercera nota: "))
while Tercera_nota < 0 or Tercera_nota > 100:
    print("La nota no puede ser menor a 0 ni mayor a 100, por favor ingrese un valor valido")
    Tercera_nota = int(input("Estimado estudiante ingrese la tercera nota: "))
Cuarta_nota = int(input("Estimado estudiante ingrese la cuarta nota: "))
while Cuarta_nota < 0 or Cuarta_nota > 100:
    print("La nota no puede ser menor a 0 ni mayor a 100, por favor ingrese un valor valido")
    Cuarta_nota = int(input("Estimado estudiante ingrese la cuarta nota: "))
Quinta_nota = int(input("Estimado estudiante ingrese la quinta nota: "))
while Quinta_nota < 0 or Quinta_nota > 100:
    print("La nota no puede ser menor a 0 ni mayor a 100, por favor ingrese un valor valido")
    Quinta_nota = int(input("Estimado estudiante ingrese la quinta nota: "))

# Calcular el promedio
Promedio = (Primera_nota + Segunda_nota + Tercera_nota + Cuarta_nota + Quinta_nota) / 5

# Mostrar el promedio
print("El promedio de sus notas es: ", Promedio)

# Determinar el resultado
if  Promedio < 39:    
    print("Con ese promedio, reprobo el curso")
    print("Debes repetirlo")
elif Promedio >= 40 and Promedio < 59:
    print("Con ese promedio, queda en recuperación")
    print("Debes esforzarte más para aprobar el curso")
else:
    print("Con ese promedio, Aprobo el curso")
    print("Felicidades")
print("Hasta la próxima")
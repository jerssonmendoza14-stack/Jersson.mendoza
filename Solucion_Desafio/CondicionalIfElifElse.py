#temperatura = int(input("Ingrese la temperatura: "))
#if temperatura >= 30:
#    print("Sistema de refrigeración encendido")
#else:
 #   print("Sistema de refrigeración apagado")
#*****************************************************
#calificación = int(input("Ingrese la calificación: "))   

#if calificación <60:
#    print("Reprobado")
#elif calificación >=70 and calificación <80:
#    print("Aprobado")
#else:
#    print("Excelente")  
#*****************************************************
Edad = int(input("Cuantos años tienes?: "))
if Edad < 0:
    print("Ingrese un valor valido")
elif Edad < 18:
    print("Eres menor de edad")
    print("Puedes jugar videojuegos")
elif Edad >= 18 and Edad < 60:
    print("Eres mayor de edad, puedes conducir")
else:
    print("Ya esta viejo, no puedes conducir ni jugar") 
print("Hasta la próxima")
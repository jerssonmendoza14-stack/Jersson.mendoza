numero = int(input("Ingrese un número: "))
if numero < 0:  
    print("El número es Negativo")
elif numero % 2 != 0:
    print("El número es Impar")
else:
    print("El número es Par")
""""Programa No. 10:
De un numero tomar su ultima cifra y decir si es par o no"""

print("-----------------------------------------------------------")
print("-----------------Ultimo digito par o impar-----------------")
print("-----------------------------------------------------------")

#Input
x = int(input("Ingrese un numero entero: "))

#processing
ultimo_digito = x%10
r = ultimo_digito%2
if r==0:
    msj = "Este es par"
else:
    msj = "Este es impar"

#Output
print("El numero " + str(x), "tiene como ultimo digito " + str(ultimo_digito), msj)
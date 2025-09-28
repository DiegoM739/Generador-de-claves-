# Creacion de constraseña de 16 bits

from random import randint

# Definimos los conjuntos de caracteres para la clave
UPPER= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER= "abcdefghijklmnopqrstuvwxyz"
NUMBERS= "0123456789"
SYMBOLS= "@#?"
ALLOWED= UPPER + LOWER + NUMBERS + SYMBOLS

# Input de longitud al usuario 
length_pass= int(input("Ingrese la cantidad de caracteres que desea: "))

# Validar minimo 16 caracteres
if length_pass < 16:
    length_pass= 16

# Generador de constraseñas donde usamos for_in range para repetir 
# tantas veces como la longitud que se ingrese en el input 
clave= ""
for _ in range(length_pass):
    posicion= randint(0, len(ALLOWED)- 1)
    caracter= ALLOWED[posicion]
    clave= clave + caracter 

# Mostrar la clave 
print("La contraseña generada es:", clave)
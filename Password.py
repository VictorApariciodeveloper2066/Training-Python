import string
import random

def generar_contrasena(longitud):
    """Genera una contraseña aleatoria de la longitud especificada."""
    caracteres = string.hexdigits + string.digits
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    return print("La contraseña generada es: " + contrasena)

longitud = int(input("Ingrese la longitud de la contraseña: "))
generar_contrasena(longitud)
# Alumno: Nikolas Barroso
# PD: este trabajo fue realizado con jupyter y luego exportado a Python.
#-------------------------------------------------------------------------#

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad:"))

if edad > 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_usuario = int(input("Ingrese su nota:"))

if nota_usuario >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num_usuario = int(input("Ingrese un numero:"))

if (num_usuario % 2 == 0):
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad:"))

if edad <= 12:
  print("Es niño/a")
elif edad >= 12 and edad < 18:
  print("Es adolescente")
elif edad >= 18 and edad < 30:
  print("Es adulto/a joven")
else:
  print("Es adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese una contraseña:")

if 8 <= len(contraseña) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
# 
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# 
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#   ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
#   ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
#   ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# 
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(20)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
  print("Sesgo positivo")
elif media < mediana and mediana < moda:
  print("Sesgo negativo")
else:
  print("Sin sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

string_usuario = input("Ingrese una frase o palabra:")
ultima_letra = string_usuario[-1].lower()
vocales = "aeiou"

if ultima_letra in vocales:
  print(string_usuario + "!")
else:
  print(string_usuario)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre:")

print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

numero_usuario = int(input(f"Seleccione una de las siguientes opciones:"))

if numero_usuario == 1:
  print(nombre.upper())
elif numero_usuario == 2:
  print(nombre.lower())
else:
  print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# 1. Menor que 3: "Muy leve" (imperceptible).
# 2. Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# 3. Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# 4. Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# 5. Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# 6. Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

print(f"Un terremoto de magnitud {magnitud} en la escala de Richter se considera: {categoria}")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio correspondiente, Norte o Sur:")
mes = int(input("Ingrese el mes (1-12):"))
dia = int(input("Ingrese el dia:"))

if hemisferio == "Norte":
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6):
        estacion = "primavera"
    elif (mes == 6 and dia >= 21) or (mes > 5 and mes < 9):
        estacion = "verano"
    elif (mes == 9 and dia >= 21) or (mes > 8 and mes < 12):
        estacion = "otoño"
    else:
        estacion = "invierno"

elif hemisferio == "Sur":
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6):
        estacion = "otoño"
    elif (mes == 6 and dia >= 21) or (mes > 5 and mes < 9):
        estacion = "invierno"
    elif (mes == 9 and dia >= 21) or (mes > 8 and mes < 12):
        estacion = "primavera"
    else:
        estacion = "verano"

else:
  print("Valor ingresado no valido.")

print(f"En el hemisferio {hemisferio}, se encuentra en la estacion {estacion}.")



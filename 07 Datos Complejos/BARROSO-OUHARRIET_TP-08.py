# PRÁCTICO 6: ESTRUCTURAS DE DATOS COMPLEJAS
#-------------------------------------------------------------------------#
# Alumno: Nikolas Barroso
# PD: este trabajo fue realizado con jupyter y luego exportado a Python.
#-------------------------------------------------------------------------#
# --- Actividades ---

# EJERCICIO 1: Añadir frutas al diccionario
print("\n1) AÑADIR FRUTAS AL DICCIONARIO")
print("-" * 40)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print("Diccionario inicial:", precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir frutas:", precios_frutas)

# EJERCICIO 2: Actualizar precios
print("\n2) ACTUALIZAR PRECIOS DE FRUTAS")
print("-" * 40)

print("Precios antes de actualizar:", precios_frutas)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Precios después de actualizar:", precios_frutas)

# EJERCICIO 3: Lista de frutas sin precios
print("\n3) LISTA DE FRUTAS SIN PRECIOS")
print("-" * 40)

frutas_sin_precios = list(precios_frutas.keys())
print("Lista de frutas:", frutas_sin_precios)

# EJERCICIO 4: Agenda telefónica
print("\n4) AGENDA TELEFÓNICA")
print("-" * 40)

contactos = {}

print("Ingrese 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    telefono = input(f"Teléfono de {nombre}: ")
    contactos[nombre] = telefono

print("\nContactos guardados:", contactos)

nombre_buscar = input("\nIngrese el nombre a buscar: ")
if nombre_buscar in contactos:
    print(f"El teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print("Contacto no encontrado.")

# EJERCICIO 5: Análisis de palabras en una frase
print("\n5) ANÁLISIS DE PALABRAS EN UNA FRASE")
print("-" * 40)

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] = contador_palabras[palabra] + 1
    else:
        contador_palabras[palabra] = 1

print("Recuento de palabras:", contador_palabras)

# EJERCICIO 6: Promedio de notas de alumnos
print("\n6) PROMEDIO DE NOTAS DE ALUMNOS")
print("-" * 40)

alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    print(f"Ingrese las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas

print("\nPromedios de cada alumno:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

# EJERCICIO 7: Análisis de parciales con sets
print("\n7) ANÁLISIS DE PARCIALES CON SETS")
print("-" * 40)

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 105, 106, 107}

print("Estudiantes que aprobaron Parcial 1:", parcial1)
print("Estudiantes que aprobaron Parcial 2:", parcial2)

ambos_parciales = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos_parciales)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

# EJERCICIO 8: Sistema de inventario
print("\n8) SISTEMA DE INVENTARIO")
print("-" * 40)

inventario = {}

while True:
    print("\nOpciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            print(f"Stock de {producto}: {inventario[producto]} unidades")
        else:
            print("Producto no encontrado.")
    
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            cantidad = int(input("Cantidad a agregar: "))
            inventario[producto] = inventario[producto] + cantidad
            print(f"Nuevo stock de {producto}: {inventario[producto]} unidades")
        else:
            print("Producto no existe. Use la opción 3 para agregarlo.")
    
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in inventario:
            print("El producto ya existe.")
        else:
            cantidad = int(input("Ingrese el stock inicial: "))
            inventario[producto] = cantidad
            print(f"Producto {producto} agregado con {cantidad} unidades")
    
    elif opcion == "4":
        print("Saliendo del sistema de inventario...")
        break
    
    else:
        print("Opción no válida.")

# EJERCICIO 9: Agenda con tuplas como claves
print("\n9) AGENDA CON TUPLAS COMO CLAVES")
print("-" * 40)

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

print("Agenda actual:", agenda)

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)
if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad programada para ese día y hora.")

# EJERCICIO 10: Invertir diccionario países-capitales
print("\n10) INVERTIR DICCIONARIO PAÍSES-CAPITALES")
print("-" * 40)

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

print("Diccionario original:", paises_capitales)

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario invertido:", capitales_paises)

print("\n" + "=" * 60)
print("FIN DEL PRÁCTICO")
print("=" * 60)
#Versionde propuesta por GGG EJERCICIO 003 PROGRA100
#DANI, me gusta mas el uso de arrays xq asi puedes generar una funcion que tanque toods los escenarios posibles 
#Codename: Lumbrera Py-Rebeca
print("Bienvenido al sistema de cálculo de promedio ponderado. V.GGG")
print(" ")
print("Lumbrera Py-Rebeca, Daniel Sandoval Parra")
print(" ")
print("El sistema soporta mas de 4 notas distintas. Deben tener punto decimal (Ej: seis siete => 6.7)")
#asi no importa el numero de notas que le tires , ya que te hace una suma 
notas = []
numnotas = int(input("Indica el número de notas que tiene la asignatura: "))
for i in range(numnotas):
    nota = float(input(f"Ingresa la nota {i + 1}: "))
    notas.append(nota)

print("Notas ingresadas:", notas)
usar_promedio_simple = input(
    "¿Calcular promedio simple? (s/n): "
).strip().lower() == "s"

if usar_promedio_simple:
    promedio = sum(notas) / len(notas)
else:
    ponderaciones = []

    for i in range(len(notas)):
        porcentaje = float(input(f"Ponderación de la nota {i + 1} (%): "))
        ponderaciones.append(porcentaje)

    if sum(ponderaciones) == 100:
        promedio = sum(
            nota * porcentaje
            for nota, porcentaje in zip(notas, ponderaciones)
        ) / 100
    else:
        print("Las ponderaciones deben sumar 100.")

print("El promedio es:", promedio)
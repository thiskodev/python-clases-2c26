"""
Registrar los ingresos mensuales de un cliente durante 3 meses usando un bucle while 
para solicitar el ingreso de cada mes. Validar que los ingresos sean números positivos. 
Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido 
y volvé a pedir el dato.

Calcular el total acumulado durante los 3 meses y el promedio mensual. 
Mostrá este resultado al final del programa.

"""

iteracion = 1
max_iteracion = 3
ingreso_total = 0
meses = ""

while iteracion <= max_iteracion:

  mes = input("Ingrese el mes: ")
  ingreso = int(input("Ingreso del cliente: "))
  
  iteracion += 1
  ingreso_total += ingreso 
  meses += f"Mes de {mes}, ${ingreso}.\n"
  
ingreso_prom = ingreso_total / max_iteracion
print("\n------Ingresos ------\n")
print(meses)
print(f"Ingreso Promedio: ${ingreso_prom}, Igreso Total: ${ingreso_total}")
print("\n----------")






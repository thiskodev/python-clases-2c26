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

while iteracion <= max_iteracion:

  ingreso = int(input("Ingreso del cliente: "))

  if ingreso < 0:
    print("El número es negativo, se ignora. Intentá de nuevo.")
    continue  
  
  iteracion += 1
  ingreso_total += ingreso 
 
ingreso_prom = ingreso_total / max_iteracion
print("\n------Ingresos ------\n")
print(f"Ingreso Promedio: ${ingreso_prom}, Igreso Total: ${ingreso_total}")
print("\n----------")






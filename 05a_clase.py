# Bucle while 
"""
numero = 1
while numero <= 20:
  print(f"Esta es la iteracion: {numero}") 
  numero += 3
"""

nombre = ""
intento = 1
intentos_max = 3

while nombre == "" and intento <= intentos_max:
  
  nombre = input("Ingresá tu nombre: ").strip()
  if nombre == "":
    print(f"El nombre no puede estar vacío. intento {intento}/{intentos_max}.")
  else:
    print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")
  intento += 1

print("Has superado el maximo de intento, intente mas tarde")


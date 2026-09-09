# Ejercicio con elif 
"""
edad = int(input("Cual es tu edad: "))

if edad < 11:
  print("Tu edad es " + str(edad) + ", Sos un niño")
elif edad < 18:
  print ("Sos adoslecente")
elif edad < 60:
  print("Sos adulto")
elif edad >= 60:
  print("Sos de la tercera edad") 
else:
  print("Ingrese de vuelta una edad validad")
"""

# Ejercicio con match
"""
print("1) Actualizar\n 2) Crear\n 3) Mostrar\n 4) Borrar")
crud = int(input("Que desea hacer: "))

match crud:
  case 1:
    print("Aca vamos Actualizar algo") 
  case 2:
    print("Aca vamos Crear algo")
  case 3:
    print("Aca vamos Mostrar algo")
  case 4:
    print("Aca vamos Eliminar algo")
  case _:
    print("Ingese un numero valido")
"""

nombre = "Ana"
print(len(nombre))
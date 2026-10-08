mi_diccionario = {
  "nombre": "Ana",
  "edad": 25,
  "ciudad": "Buenos Aires"
}

otros_datos = {
  "genero": "no binario",
  "codigo_postal": 1358
}

mi_diccionario["profesion"] = "Programadora" 

print(f"Emi vive {mi_diccionario['ciudad']}")
mi_diccionario["ciudad"] = "Las Flores"
print(f"Emi se mudo a {mi_diccionario['ciudad']}")
print(mi_diccionario["profesion"])

print(mi_diccionario.get("nombre"))
print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())

eliminar = mi_diccionario.pop("edad")
print(mi_diccionario.items())
print(mi_diccionario.keys())
print(f"el valor eliminado es: {eliminar}")
eliminar_profesion = mi_diccionario.popitem() 
print("le sacamos el titulo: ", eliminar_profesion)


mi_diccionario.update(otros_datos)
mi_diccionario.update(genero="femenino", nombre="Maria", ciudad="Cordoba")
print(mi_diccionario)
print("----------------------\n")
for clave, valor in mi_diccionario.items():
  print(f"{clave}: {valor}")

estudiantes = {
  "Ana": {"edad": 22, "carrera": "Informática"},
  "Juan": {"edad": 24, "carrera": "Diseño", "nota":8}
}

print(estudiantes["Juan"]["nota"])

inventario = [
  {"nombre": "manzanas", "cantidad": 50},
  {"nombre": "peras", "cantidad": 30},
  {"nombre": "naranjas", "cantidad": 40}
]

for producto in inventario:
  print(f"{producto['nombre']} : {producto['cantidad']}")

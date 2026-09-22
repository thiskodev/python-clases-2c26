"""
ingresos = [40000, 55000, 60000, 45000, 70000, 50000]
count = 0

for ingreso in ingresos:
    if ingreso > 50000:
        count += 1

print(f"Cantidad de ingresos superiores a $50000: {count}")
"""

"""
usuarios = ["Ana", "Luis", "andrés", "María", "Alejandro", "Lucía"]
letra_buscada = "A"

for nombre in usuarios:
  if nombre.startswith(letra_buscada):
    print(f"Nombre que empieza con '{letra_buscada}': {nombre}")
"""

productos = [
  ["Nombre: Peras", "Precio: 5000", "Categoria: Verduleria"], 
  ["Nombre: Manzanas", "Precio: 4000", "Categoria: Verduleria"],
  ["Nombre: Papas", "Precio: 2000", "Categoria: Verduleria"],
]

print(productos[1][1])
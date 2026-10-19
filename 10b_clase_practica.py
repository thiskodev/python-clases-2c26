# 1) Agregar Producto
# 2) Mostrar Producto
# 3) Actualizar 
# 4) Eliminar 

productos = []

def agregar_producto(nombre, precio, categoria):
  producto = [nombre, precio, categoria]
  productos.append(producto)

agregar_producto("Papas", 2500, "Verduras")
agregar_producto("Peras", 3500, "Verduras")
agregar_producto("Detergente", 3200, "Limpieza")

print(productos)

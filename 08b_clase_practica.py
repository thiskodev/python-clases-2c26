"""  # Creamos una lista vacía para almacenar los diccionarios
clientes = [] 
  # Bucle para ingresar los datos de varios clientes
while True:
  print("\nIngresá los datos del cliente.[vacío para finalizar]:")
  codigo = input("Código del cliente: ")
  # Condición para salir del bucle si el código está vacío
  if codigo == "":
    break
  nombre = input("Nombre del cliente: ")
  ciudad = input("Ciudad del cliente: ")
  # Creamos un diccionario con los datos ingresados
  cliente = {
    "código": codigo,
    "nombre": nombre,
    "ciudad": ciudad
  }
  
# Agregamos el diccionario a la lista de clientes
  clientes.append(cliente)
# Mostramos los datos de todos los clientes registrados
  print("\n--- Clientes Registrados ---")
  for cliente in clientes:
    print(f"Código: {cliente['código']}, Nombre: {cliente['nombre']}, Ciudad: {cliente['ciudad']}")
"""

productos = {
  "lápiz": 50,
  "cuaderno": 200,
  "goma": 30,
  "marcador": 100
}

# Mostramos los productos disponibles al inicio
print("Productos disponibles:")
for nombre, precio in productos.items():
  print(f"{nombre.capitalize()}: ${precio}")
# Bucle para permitir al usuario eliminar productos
while True:
  print("\nIngresá el nombre del producto que querés eliminar (o presioná Enter para terminar):")
  eliminar = input("Producto a eliminar: ").lower()
  # Si el usuario presiona Enter sin escribir nada, se sale del bucle
  if eliminar == "":
    break
  # Verificamos si el producto está en el diccionario y lo eliminamos
  if eliminar in productos:
    productos.pop(eliminar)
    print(f"El producto '{eliminar}' fue eliminado del inventario.")
  else:
    print(f"El producto '{eliminar}' no existe en el inventario.")
  # Mostramos el estado actual del diccionario
  print("\nProductos restantes:")
  for nombre, precio in productos.items():
    print(f"{nombre.capitalize()}: ${precio}")
    # Estado final del diccionario
    print("\n--- Estado final del inventario ---")

for nombre, precio in productos.items():
  print(f"{nombre.capitalize()}: ${precio}")
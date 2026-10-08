productos = []

while True:
  print("\n----- SISTEMA GESTOR DE PRODUCTOS ----\n")
  print("1. Agregar producto")
  print("2. Mostrar productos")
  print("3. Actualizar producto")
  print("4. Eliminar producto")
  print("5. Salir")
  print("\n--------------------------------------\n")
  
  opcion = input("Elija una opción (1-5): ").strip()

  match opcion:
    # Agregar Productos
    case "1":
      print("\n--- AGREGAR PRODUCTO ---")
      nombre = input("Nombre: ").strip()
      while nombre == "":
        nombre = input("El nombre no puede estar vacío: ").strip()

      categoria = input("Categoría: ").strip()
      while categoria == "":
        categoria = input("La categoría no puede estar vacía: ").strip()

      precio_input = input("Precio: ").strip()
      while not precio_input.isdigit():
        precio_input = input("Ingrese solo números para el precio: ").strip()

      precio = int(precio_input)

      nuevo_producto = [nombre, categoria, precio]
      productos.append(nuevo_producto)
      print("¡Producto agregado!")

    # Mostrar Productos
    case "2":
      print("\n--- LISTA DE PRODUCTOS ---")
      if len(productos) == 0:
        print("No hay productos registrados.")
      else:
        for i in range(len(productos)):
        # prod = [Jabon,Limpieza,2000] 
          prod = productos[i]
          print(f"ID: {i + 1} | Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")

    # Editar Productos
    case "3":
      print("\n--- ACTUALIZAR PRODUCTO ---")
      if len(productos) == 0:
        print("No hay productos para actualizar.")
      else:
        # Mostramos los productos primero
        print("Productos disponibles:")
        for i in range(len(productos)):
          prod = productos[i]
          print(f"ID: {i + 1} - {prod[0]}")

        id_input = input("\nSeleccione el ID a actualizar: ").strip()
        
        if id_input.isdigit():
          # Se le resta 1 porque la lista empieza en 0 
          posicion = int(id_input) - 1
          
          if posicion >= 0 and posicion < len(productos):
            print("\nIngrese los nuevos datos:")
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_categoria = input("Nueva categoría: ").strip()
            nuevo_precio = int(input("Nuevo precio: "))

            productos[posicion] = [nuevo_nombre, nueva_categoria, nuevo_precio]
            print("¡Producto actualizado!")
          else:
            print("No existe un producto con ese ID.")
        else:
          print("Debe ingresar un número de ID válido.")

    # Eliminar Productos
    case "4":
      print("\n--- ELIMINAR PRODUCTO ---")
      if len(productos) == 0:
        print("No hay productos para eliminar.")
      else:
        # Mostramos los productos primero
        print("Productos disponibles:")
        for i in range(len(productos)):
          prod = productos[i]
          print(f"ID: {i + 1} - {prod[0]}")

        id_input = input("\nSeleccione el ID a eliminar: ").strip()
        
        if id_input.isdigit():
          posicion = int(id_input) - 1
          
          if posicion >= 0 and posicion < len(productos):
            producto_eliminado = productos.pop(posicion)
            print(f"¡Producto '{producto_eliminado[0]}' eliminado con éxito!")
          else:
            print("No existe un producto con ese ID.")
        else:
          print("Debe ingresar un número de ID válido.")
    
    # Salida por default si el usuario algo que no sea 1 a 5
    case _:
      print("Saliendo del programa... ¡Hasta luego!")
      break
# Ingreso de datos
nombre = input("Nombre: ").strip().title()
apellido = input("Apellido: ").strip().title()
correo = input("Correo electrónico: ").strip()
edad_texto = input("Edad: ").strip()

# Validaciones
correo_valido = "@" in correo and correo.count("@") == 1 and " " not in correo
edad_valida = edad_texto.isdigit()
mostrar_datos = correo_valido and edad_valida

if mostrar_datos:
    edad = int(edad_texto)

    # Clasificación por edad
    if edad < 15:
        categoria = "Niño/a"
    elif edad <= 18:
        categoria = "Adolescente"
    else:
        categoria = "Adulto/a"

    # Mostrar datos
    print("\n--- Ficha del cliente ---")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Correo: {correo}")
    print(f"Categoría: {categoria}")
else:
    print("ERROR: Los datos ingresados no son válidos.")
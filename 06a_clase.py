""""
numeros = [10,20,30]
indice = 0

while indice < len(numeros):
  print(f"Indice {indice}, Valor: {numeros[indice]}") 
  indice += 1
"""

"""
numeros = [10,20,30]
for i in numeros:
  print("El numero de la lista ", i)
"""
"""
palabra = "Hola"
for letra in palabra:
  print("Letra:", letra)
"""

"""
           #[ 0 , 1 , 2 , 3]
productos = ["P1","P2","P3","P4"]
producto_buscado = "P3"

for i in productos:
  if i == producto_buscado:
    print(f"producto {i} encontrado")
    break
  else:
    print(f"Producto {i}, no es igual a {producto_buscado}")
"""

for i in range(10, 0, -2):
  print(i)

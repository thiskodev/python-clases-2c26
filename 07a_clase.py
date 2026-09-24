""""
ventas = []
contador = 0

while contador < 3:
  montos = int(input("Ingrese el monto: "))
  ventas.append(montos)
  contador += 1

ventas.remove(2000)
print(ventas)
"""

"""
ventas1 = [1000,2000,1000]
ventas2 = [6000, 8000]
ventas1.extend(ventas2)
print(ventas1)

ventas = tuple(ventas1)
print(ventas)
"""

letras = ('a', 'b', 'c', 'd', 'e')
print(letras[1:4])  
print(letras[::-2])  
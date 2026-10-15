
def sumar(a,b): 
  """ Esta funcion hace es sumar......."""
  return a + b
"""
print(sumar(3,6))
variable_oculta_aguinaldo = sumar(2,4)

suma_completa = sumar(4,6) + 10 + sumar(3,7)

print(f"Suma: {suma_completa}")
"""

"""
# Funcion que eleva al cuadraro lo que ingresa el user
def calcular_cuadrado(numero):
  return numero ** 2
    

numero_ingresado = int(input("Ingresá un número: "))
cuadrado = calcular_cuadrado(numero_ingresado)
print(f"El cuadrado de {numero_ingresado} es {cuadrado}")
"""

# funcion con dos return
def calcular_area_y_perimetro(base, altura):
  """Esta funcion calcula un monton de cositas"""
  area = base * altura
  perimetro = 2 * (base + altura)
  volumen = base * base * altura 
  return area, perimetro, volumen

area, perimetro, volumen = calcular_area_y_perimetro(2,4)
"""
print(f"Perimetro: {perimetro} cm")
print(f"Area: {area} cm2")
print(f"Volumen: {volumen} cm3")
"""

help(sumar)
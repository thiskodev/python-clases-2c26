import random
import math
import calculadora
from datetime import datetime
from colorama import Fore, Back, init


# Modulo random
"""
def tirar_dados ():
  dado = random.randint(1,6)
  print(f"la tirada salio {dado}")

tirar_dados()

lista = ["oro","espada","basto","copa"]
random.choice(lista)
print(lista)
"""

# Modulo math
"""
potencia = math.pow(3,2)
print(math.pi)
print(potencia)

radio = float(input("Ingresá el radio del círculo: "))
area = math.pi * math.pow(radio, 2)
print(f"El área del círculo con radio {radio} es: {area:.2f}")
"""

# Modulo datetime
fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)
print("Solo la fecha:", fecha_hora_actual.strftime("%Y-%m-%d"))
print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))
print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))


init()
print(Fore.GREEN + "Texto en verde")
print(Back.RED + "Fondo rojo" + Back.RESET)
print(Fore.BLUE + Back.YELLOW + "Texto azul en fondo amarillo")

print(calculadora.sumar(2,4))

resta = calculadora.restar(4,1)
print(resta)

raiz_cuadrada = int(calculadora.raiz(16)) 
print(raiz_cuadrada)
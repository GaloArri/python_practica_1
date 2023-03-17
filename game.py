from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+","-","*","/"]

# Cantidad de cuentas a resolver.
times = 5

# Contadores de victorias y derrotas.
cantP = 0
cantG = 0

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
# Se eligen números y operador al azar.
  number_1 = randrange(10)
  operator=choice(operators)
  number_2 = randrange(10)

# Realizo las cuentas dependiendo el operador que haya tocado.
  if operator == "+": 
    resultado = number_1 + number_2
  elif operator == "-":
    resultado = number_1 - number_2
  elif operator == "/":
    while number_2 == 0:
      number_2 = randrange(10)
    resultado = number_1 / number_2
  elif operator == "*":
    resultado = number_1 * number_2

# Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

# Le pedimos al usuario el resultado.
  result = float(input("resultado: "))

# Mostramos el resultado en pantalla.
  print (f"El resultado es: {resultado} ")

# Sumamos el contador de ganadas y perdidas.
  if(resultado == result):
    cantG+=1
  else:
    cantP+=1

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora actual.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
print(f"\nTardaste {total_time.seconds} segundos.")

# Mostramos el resultado.
print(f"Las veces que gano fueron: {cantG} y las veces que perdio fue : {cantP}")
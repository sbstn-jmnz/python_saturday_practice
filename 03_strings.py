# Los stings son cadenas de letras
# Se pueden hacer con "" o ''

import re


str_one = "Micro"
str_two = 'System'

# Juntar uno o más strings se denomina concatenar. En python se puede concatenar utilizando el operador '+'
print(str_one + str_two)

# Ojo: con la ',' la función print NO
# concatena
print(str_one, str_two)

# Podemos también multiplicar un string con un int

print('Hello'*3) 

str_three = 'Bye'

result = str_three * 5

print(result)

# Existe la función len() que nos entrega el largo de un string
# Número de caracteres
print(len(result))
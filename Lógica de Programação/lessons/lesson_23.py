""" FATIAMENTO DE STRINGS """

""" 
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
H | e | l | l | o |   | W | o | r | l | d |
-11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres de str 
"""

variable = 'Hello World'

print(variable[0:5]) # Hello
print(variable[0:11]) # Hello World
print(variable[0:11:4]) # Hor (pula de 4 em 4)
print(len(variable)) # Conta os caracteres presentes na variavel: variable = Hello Wordl = 11
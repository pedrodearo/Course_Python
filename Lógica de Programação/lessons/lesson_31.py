""" WHILE - WHILE (LAÇOS INTERNOS) """

""" 
Repetições
while (enquanto)
Executa uma ação enquanto uma confição for verdadeira
"""

lines = 5
columns = 5

line = 1
while line <= lines:
  column = 1

  while column <=  columns:
    print(f'{line=}, {column=}')
    column+= 1

  line += 1

print('Finish')
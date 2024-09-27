""" WHILE - CONTINUE (PULANDO ALGUMA REPETIÇÃO) """

""" 
Repetições
while (enquanto)
Executa uma ação enquanto uma confição for verdadeira
"""

counter = 0

while counter <= 100:
  counter += 1

  if counter >= 10 and counter <=40:
    print('Secret')
    continue

  print(counter)
  
  if counter == 50:
    break

print('finish')
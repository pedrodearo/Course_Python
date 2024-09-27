""" WHILE - ELSE """

string = 'Any value'

i = 0
while i < len(string):
  letter = string[i]

  if letter == ' ':
      break

  print(letter)
  i += 1

else:
  print('The else was executed')

""" TODA VEZ QUE O WHILE TIVER UM 'break' O ELSE NÃO FUNCIONA """
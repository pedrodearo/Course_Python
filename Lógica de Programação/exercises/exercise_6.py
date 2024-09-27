"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

number = int(input("Type an int number to find out the correct greeting: "))

if number >= 0 and number <= 11:
  print('GOOD MORNING')

if number >= 12 and number <= 17:
  print('GOOD EVENING')

elif number >= 18 and number <= 23:
  print('GOOD NIGHT')


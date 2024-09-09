""" INTRODUÇÃO AO TRY/EXCEPT """

"""
TRY -> Tentar execultar o código
EXCEPT -> Ocorreu algum erro ao tentar executar
"""

number_str = input("I'll double you number:")

try:
  number_int = int(number_str)
  print(f'\nDouble {number_str} is {number_int * 2}')

except:
  print("\nThis isn't a number")
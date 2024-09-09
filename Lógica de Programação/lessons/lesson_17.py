""" OPERADOR LÓGICO - AND (E) """

""" 
AND - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão falsy (que você já viu) 
0 | 0.0 | '' | False
Também existe o tipo None que é usado para representar um não valor
"""

options = input('Type [E] to enter ot [Q] to quit \n\n')
password_entered = input('Password: ')
password_allowed = '123456'

if options == 'E' and password_entered == password_allowed:
  print('You entered')

elif password_entered != password_allowed:
  print('Password not allowed')

elif options == 'Q':
  print('You left')

else:
  print('Invalid option!')

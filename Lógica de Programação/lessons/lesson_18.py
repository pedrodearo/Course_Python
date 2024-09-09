""" OPERADOR LÓGICO - OR (OU) """

""" 
OR - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressão inteira
será avaliada naquele valor. São considerados falsy (que você já viu)
0 | 0.0 | '' | False
Também existe o tipo None que é usado para representar um 'não valor'
"""

options = input('Type [E] to enter ot [Q] to quit \n\n')
password_entered = input('Password: ')
password_allowed = '123456'

if (options == 'E' or options == 'e') and password_entered == password_allowed:
  print('You entered')

elif password_entered != password_allowed:
  print('Password not allowed')

elif (options == 'Q' or options =='q'):
  print('You left')

else:
  print('Invalid option!')
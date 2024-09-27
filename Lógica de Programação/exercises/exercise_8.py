""" EXERCICIO GUIADO - CALCULADORA UTILIZANDO 'WHILE' """

# COLHENDO OS INPUTS
while True:
  number_1 = input('Type a number: ')
  number_2 = input('Type a second number: ')
  operators = input('Type an operator (+-/*): ')

  valid_numbers = None

# CONVERTENDO OS VALORES DIGITADOS PARA 'FLOAT'

  try:
    number_1_float = float(number_1)
    number_2_float = float(number_2)
    valid_numbers = True

# CASO O USUÁRIO DIGITE UM NÚMERO INVÁLIDO

  except:
    valid_numbers = None

  if valid_numbers is None:
    print('One of the number is invalid!')
    continue

#LISTA DE OPERADORES PERMITIDOS

  valid_operators = '+-/*'

# CASO O USUÁRIO DIGITE UM OPERADOR QUE NÃO ESTIVER
# PRESENTE NA VARIAVEL ACIMA

  if operators not in valid_operators:
    print('Invalid Operator!')
    continue 

# CASO O USUÁRIO DIGITE MAIS DE UM OPERADOR

  if len(operators) > 1:
    print('Type only one operator')
    continue 

# CASO O USUÁRIO TENHA DIGITADO '+' IRÁ REALIZAR UMA CONTA DE ADIÇÃO

  if operators == '+':
    addition = number_1_float + number_2_float
    print(f'{number_1_float} + {number_2_float} is {addition}')

# CASO O USUÁRIO TENHA DIGITADO '-' IRÁ REALIZAR UMA CONTA DE SUBTRAÇÃO

  elif operators == '-':
    subtraction = number_1_float - number_2_float
    print(f'{number_1_float} - {number_2_float} is {subtraction}')

# CASO O USUÁRIO TENHA DIGITADO '/' IRÁ REALIZAR UMA CONTA DE DIVISÃO

  elif operators == '/':
    division = number_1_float / number_2_float
    print(f'{number_1_float} / {number_2_float} is {division}')

# CASO O USUÁRIO TENHA DIGITADO '*' IRÁ REALIZAR UMA CONTA DE MULTIPLICAÇÃO

  elif operators == '*':
    multiplication = number_1_float * number_2_float
    print(f'{number_1_float} * {number_2_float} is {multiplication}')

  else:
    print('It should never have gotten to this print')

# OPÇÃO PARA SAIR DA CALCULADORA.
# CASO SEJA DIGITADO QUALQUER OUTRA LETRA 'Y' O PROGRAMA IRÁ 
# EXECULTAR NOVAMENTE, CASO CONTRARIO, O PROGRAMA SERÁ ENCERRADO

  leave = input('Do you want to leave? [y]es:\n').lower().startswith('y')

  if leave is True:
    break
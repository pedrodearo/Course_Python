""" ITERANDO STRINGS COM WHILE """

""" Adicione algum caracter entre as letras do nome digitado """

name = input('Type your name:\n')


indice = 0
new_name = ''
while  indice < len(name):
  
  letter = name[indice]
  new_name += f'|{letter}'
  indice += 1

new_name += '|'
print(new_name)
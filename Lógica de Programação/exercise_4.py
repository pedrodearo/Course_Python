name = input('Type your name: ')
age = input('Type your age: ')

if name and age:
  print(f'\nYour name is: {name} \n')
  print(f'Your inverted name is: ', name[::-1], '\n' )

  if '' in name:
    print('Your name contains espace \n')
  else:
    print("Your name doesn't contains espace \n")

  print(f'The first letter in your name is: {name[0]} \n')
  print(f'The last letter in you name is: {name[-1]} \n')
  print(f'Your name have "{len(name)}"  characters \n')

else:
  print('\nSorry, you left some field empty')
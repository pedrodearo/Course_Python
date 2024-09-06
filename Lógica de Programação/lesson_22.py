""" FORMATAÇÃO COM F-STRINGS """

""" 
s - string
d - int 
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal: + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variable = 'ABC'
print(f'{variable}')
print(f'{variable:.>11}')
print(f'{variable:.<11}')
print(f'{variable:.^11}')
print(f'{1000.63284168321:0=+10,.1f}')
print(f'O hexadecimal de 1500 é: {1500:08X}')

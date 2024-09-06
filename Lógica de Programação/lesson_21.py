""" INTERPOLAÇÃO BÁSICA DE STRING """

""" 
s - string
'd' e 'i' - int
f - float
'x' e 'X' - Hexadecimal (ABCDEF0123456789)
"""
name = 'Pedro'
price = 1000.5095483
variable = '%s, the price is R$%.2f' % (name, price)

print(variable)
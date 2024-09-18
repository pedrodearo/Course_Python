""" ID """

"""
Flags (Bandeiras) - Marcam um local
None = Não valor
is | is not = (tipo, valor, identidade)
id = identidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
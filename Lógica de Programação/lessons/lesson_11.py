""" INTRODUÇÃO ÀS F-STRINGS """

name = 'Pedro Dearo'
heigth = 1.8
weigth = 73
bmi = weigth / heigth ** 2

line_1 = f'{name} is {heigth} tall, and weigth {weigth}Kg. Your BMI is {bmi:.2f}' # :.2f, para limitar a quantidade de casas decimais

print(line_1)
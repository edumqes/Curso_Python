#Formatação de strings

"""
s - string
d ou i - int
f - float
.<num_digitos>f
x ou X - hexadecimal
> - Caracaters a esquerda (LPAD)
< - Caracteres a direita (RPAD)
^ - Caracteres ao centro
Sinal (+ ou -)
"""

variavel = 'ABCD'
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{123.4567891011:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:04x}')
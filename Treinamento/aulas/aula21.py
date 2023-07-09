#While
'''
Executa enquanto a condição for verdadeira
break - sai do "laço"
continue - ignora iteração e volta para início do laço
'''

numero = int(input('Digite um número: '))

while numero > 0:
    numero -= 1
    if numero % 4 == 0:
        continue
    print(numero)
else:
    print('Terminou!')




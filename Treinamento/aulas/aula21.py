#While
'''
Executa enquanto a condição for verdadeira
break - sai do "laço"
continue - ignora iteração e volta para início do laço
'''

i = input('Digite um número inteiro: ')

if i.isdigit():
    numero = int(i)
    while numero > 0:
        numero -= 1
        if numero % 4 == 0:
            continue
        print(numero)
        #if numero == 0:
            #break
else:
    print('Valor digitado não é número inteiro!')




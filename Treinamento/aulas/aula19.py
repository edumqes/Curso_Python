#Tratamento de Erros (try/except)

'''
try -> tenta executar
except -> caso ocorra erro captura exceção
'''

dividendo = input('Digite um número: ')
divisor = input('Digite outro número: ')

try:
    resultado = int(dividendo) // int(divisor)
    print(f'Resultado da divisão é {resultado}')
except:
    print('Impossível dividir por zero')

string = 'Pedro Marques'
print(string.replace('o','a'))
print(string.upper())
print(string.endswith('s'))



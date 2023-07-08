#Operadores Condicionais

'''
if condição1:
    instrução 1
elif condição2:
    instrução 2
else:
    instrução 3
'''

acao = input('Você quer entrar ou sair? ')

if acao == 'entrar':
    print('Você entrou no sistema')
elif acao == 'sair':
    print('Você saiu do sistema')
else:
    print('Digite somente "entrar" ou "sair"')

print("Fim")

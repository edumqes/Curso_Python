#Operadores lógicos

"""
and - Todas as condições devem ser verdadeiras
or - Basta uma condiçaõ ser verdadeira
not - Inverte a condição
0 0.0 '' interpretado como False
"""

acao = input('[E]ntrada ou [S]air: ')
senha = input('Senha: ') or 'Sem senha'

if (acao == 'E' or acao == 'e') and not senha == 'Sem senha':
    print('Entrar')
else:
    print('Sair')

print(True or False)
print(bool(0))

print(not True)

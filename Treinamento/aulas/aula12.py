#Input - coletar dados digitados na tela (somente str)

nome = input('Qual o seu nome? ')
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#converte para int antes da soma
soma = int(num1) + int(num2)

print(f'Meu nome é {nome}')
print(f'A soma dos números é {soma}')
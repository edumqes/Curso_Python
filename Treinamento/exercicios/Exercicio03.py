#Comparar 2 números

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if int(num1) == int(num2):
    print("Os dois números são iguais")
elif int(num1) > int(num2):
    print(f'Primeiro número é o maior {num1}')
else:
    print(f'Segundo número é o maior {num2}')

print("Fim")
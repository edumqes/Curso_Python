#Operadores IN e NOT IN
#Strings são iteráveis

nome = input('Digite seu nome: ')
letra = input('Digite uma letra de a a z: ')

if letra in nome:
    print(f'Seu nome {nome} contem a letra {letra}')
else:
    print(f'Seu nome {nome} não contem a letra {letra}')

print("Fim")

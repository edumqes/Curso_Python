nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
        print("Digite corretamente nome e idade!")

#Palindromo
texto = input('Digite um texto: ')
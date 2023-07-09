
nome = input('Digite nome completo: ')

i = 0

texto = ''
while i < len(nome):
    
    if (nome[i] == ' '):
        break
    
    print(nome[i])
    i += 1
else:
    print("Nome nã contem espaços")
#Match Case
'''
case 1: condicao1
case 2: condicao2
case 3: condicao3
case _: condicao inválida
'''
#rodízio
placa = input('Digite placa: ')
try:
    match int(placa[-1]):
        case 1 | 2:
            print('Segunda-Feira')
        case 3 | 4:
            print('Terça-Feira')
        case 5 | 6:
            print('Quarta-Feira')
        case 7 | 8:
            print('Quinta-Feira')
        case 9 | 0:
            print('Sexta-Feira')
except:
    print('Placa inválida!')
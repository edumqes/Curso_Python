#Formataçaõ de string - Exercício anterior

#Calculo IMC
nome = 'Eduardo'
altura = 1.71
peso = 75

imc = peso / (altura ** 2)

#f-string
linha = f'{nome} tem {altura:.2f} de altura e pesa {peso} kg'
print(linha)

#Função format
formatado = '{} tem {:.2f} de altura e pesa {} kg'.format(nome,altura,peso)     #Precisam estar na ordem
print(formatado)
print('IMC = {:.2f}'.format(imc))

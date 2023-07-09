#Constante -> "variável" que nunca muda o valor
#None -> não tem valor atribuído
#is/is not

NOTA_CORTE = 7.0

nota = input('Digite nota da prova: ')
aprovado = float(nota) >= NOTA_CORTE
reprovado = None

if aprovado:
    print('Aprovado!')
else:
    reprovado = True
    print('Reprovado!')

print(reprovado is not None)





        

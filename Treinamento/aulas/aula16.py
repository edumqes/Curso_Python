#Interpolaçao de strings

'''
%s - string
%f - float
%d ou %i - int
%x ou %X - heaxadecimal
'''

nome = 'Eduardo'
preco = 123.4567
unidade = 10
texto = '%s, o preço de %i unidades do produto é R$%.2f' % (nome,unidade,preco * unidade)
print(texto)


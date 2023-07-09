#Qual letra mais aparece numa frase?

frase = 'O Python é uma linguagem de programação multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'


quantidade = 0
letra = ' '

for i in frase:
    contador = frase.count(i)
    if i != ' ' and quantidade < contador:
        quantidade = contador
        letra = i
    #print(frase[i],contador)

print(f"A letra '{letra}' apareceu {quantidade} vezes")

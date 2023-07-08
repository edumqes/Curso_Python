#Conversão de tipos

'''
int(str) -> converte para inteiro
float(str) -> converte para float
str(int) -> converte para string
bool(value) -> converte para boolean
'''

print(1 + 1)            #Soma
print('a' + 'b')        #Concatena

#print('1' + 1)         #Type error str + int

#After cast
print(int('1') + 1)         #Soma OK  (int ou float)
print('1' + str(1))         #Concatena OK

print(type(float('1') + 1))

print(bool())   #String vazio False
print(bool(1))  #Qualquer valor não vazio True

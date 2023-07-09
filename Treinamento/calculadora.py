while True:

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')   

    try:
        #Somente números
        float1 = float(num1)
        float2 = float(num2)
    except:
        print('Número(s) Inválido(s)!')
        continue
   
    operador = input('Digite um operador ( + - * / ): ')

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    match operador:
            case '+':
                print(f'Resultado = {float(num1) + float(num2)}')
            case '-':
                print(f'Resultado = {float(num1) - float(num2)}')
            case '*':
                print(f'Resultado = {float(num1) * float(num2)}')
            case '/':
                try:
                    print(f'Resultado = {float(num1) / float(num2)}')
                except Exception as error:
                    print(error)
                    continue
            case _:
                print('Operador Inválido!')
                continue
        
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair:
        break
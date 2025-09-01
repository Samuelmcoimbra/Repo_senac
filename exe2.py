while True:
    try:
        numero = float(input('Digite um número: '))
        break
    except:
        print('Digite apenas números')

match numero:
    case n if n >= 0:
        print('O numero é positivo!')
    case n if n < 0:
        print('O número é negativo!')


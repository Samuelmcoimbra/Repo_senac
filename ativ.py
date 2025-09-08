velocidade = int(input('Digite a velocidade do veículo: '))
limite = int(input('Digite o limite de velocidade da via: '))

def multa(velocidade, limite):
    if velocidade <= limite:
        return 0
    elif velocidade <= limite * 1.1:
        return 180.00
    elif velocidade <= limite * 1.3:
        return 340.56
    else:
        return 480.98
print(f'Você foi multado em R$ {multa(velocidade, limite):.2f}')
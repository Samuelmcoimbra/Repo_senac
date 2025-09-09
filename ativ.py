'''velocidade = int(input('Digite a velocidade do veículo: '))
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
print(f'Você foi multado em R$ {multa(velocidade, limite):.2f}')'''
# Outra atividade




sexo = input('Qual o seu sexo: M (masculino)/ F (feminino)')
peso = float(input('Qual o seu peso: '))
alt = int(input('Qual sua altura em centímetros: '))
idade = int(input('Qual a sua idade: '))

def TMB(sexo, peso, alt, idade):
    if sexo.upper() == 'M':
        return 66.5 + (13.75 * peso) + (5.003 * alt) - (6.755 * idade)
    elif sexo.upper() == 'F':
        return 655.1 + (9.563 * peso) + (1.850 * alt) - (4.676 * idade)
print(f'Seu metabolismo basal é de {TMB(sexo, peso, alt, idade)} calorias')




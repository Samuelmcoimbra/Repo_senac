comprimento = float(input('Digite o comprimento da cozinha (em metros): '))
largura = float(input('Digite a largura da cozinha (em metros): '))
altura = float(input('Digite a altura da cozinha (em metros) '))

area_total = (comprimento * altura * largura)


quoc = int(area_total / 1.5)
resto = area_total % 1.5

match resto:
    case 0:
        caixas = quoc
    case _:
        caixas = quoc + 1

print(f'Área total das paredes: {area_total:.2f} m')    
print(f'Quantidade de caixas necessárias: {caixas}')
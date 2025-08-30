largura = float(input('Digita a largura do cômodo (em metros)'))
comprimento = float(input('Digita a altura do cômodo (em metros)'))
potencia_lampada = float(input('Digite a potência da lâmpada (em watts): '))


area = largura * comprimento
potencia_necessaria = area * 3

qtd_lampada = potencia_necessaria / potencia_lampada

print(f'Área do cômodo {area:.2f}')
print(f'Potência necessária {potencia_necessaria:.2f}')
print(f'Quantidade de lâmpadas {qtd_lampada}')
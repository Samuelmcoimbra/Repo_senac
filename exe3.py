while True:
        try:
            inicio = float(input("Digite a marcação do odômetro no início do dia (km): "))
            break
        except:
            print("Entrada inválida! Digite apenas números.")

    # --- Entrada segura do odômetro final ---
while True:
        try:
            fim = float(input("Digite a marcação do odômetro no fim do dia (km): "))
            if fim < inicio:
                print("O odômetro final não pode ser menor que o inicial.")
                continue
            break
        except:
            print("Entrada inválida! Digite apenas números.")

    # --- Entrada segura do consumo ---
while True:
        try:
            litros = float(input("Digite a quantidade de litros consumidos: "))
            if litros <= 0:
                print(" A quantidade de litros deve ser maior que zero.")
                continue
            break
        except:
            print(" Entrada inválida! Digite apenas números.")

    # --- Entrada segura do valor recebido ---
while True:
        try:
            valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))
            break
        except:
            print(" Entrada inválida! Digite apenas números.")

    # Processamento
km_rodados = fim - inicio
media_consumo = km_rodados / litros
gasto_combustivel = litros * 4.87
lucro_liquido = valor_recebido - gasto_combustivel

# Menu
while True:
        print("\nO que deseja calcular?")
        print("1 - Média de consumo (km/l)")
        print("2 - Gasto com combustível")
        print("3 - Lucro líquido")
        print("4 - Mostrar tudo")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            break
        except:
            print(" Digite apenas números inteiros!")
        

if opcao == 1:
        print(f"Média de consumo: {media_consumo:.2f} km/l")
elif opcao == 2:
        print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
elif opcao == 3:
        print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")
elif opcao == 4:
        print(f"Média de consumo: {media_consumo:.2f} km/l")
        print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
        print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")
elif opcao == 5:
        print("Saindo do programa... Até logo!")
else:
        print(" Opção inválida! Tente novamente.")


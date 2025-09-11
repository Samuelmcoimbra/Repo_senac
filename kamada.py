

# Cardápio do restaurante (prato: preço)
cardapio = {
    "Sushi Combo": 45.0,
    "Yakissoba": 38.0,
    "Tempurá": 30.0,
    "Lamen": 42.0,
    "Sashimi de Salmão": 50.0,
    "Guioza": 25.0
}

# Lista para armazenar pedidos
pedidos = []
contador_pedidos = 1


# 1. Função para exibir o cardápio
def exibir_cardapio():
    print("CARDÁPIO DIGITAL")
    for prato, preco in cardapio.items():
        print(f"{prato} - R$ {preco:.2f}")


# 2. Função para registrar um pedido
def registrar_pedido():
    global contador_pedidos

    numero_mesa = input("Digite o número da mesa: ")
    nome_garcom = input("Digite o nome do garçom: ")

    itens_escolhidos = []
    while True:
        exibir_cardapio()
        item = input("Digite o nome do prato (ou 'fim' para encerrar): ")
        if item.lower() == "fim":
            break
        if item in cardapio:
            itens_escolhidos.append(item)
        else:
            print("Esse item não está no cardápio.")

    total = 0
    itens_detalhados = []
    for item in itens_escolhidos:
        preco = cardapio[item]
        total += preco
        itens_detalhados.append((item, preco))

    pedido = {
        "id": contador_pedidos,
        "mesa": numero_mesa,
        "garcom": nome_garcom,
        "itens": itens_detalhados,
        "total": total
    }

    pedidos.append(pedido)
    contador_pedidos += 1

    print(f"Pedido {pedido['id']} registrado com sucesso!")


# 3. Função para fechar a conta
def fechar_conta():
    if not pedidos:
        print("⚠️ Não há pedidos registrados.")
        return

    id_pedido = int(input("Digite o número do pedido para fechar a conta: "))

    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            print("FECHAMENTO DE CONTA")
            print(f"Pedido: {pedido['id']}")
            print(f"Mesa: {pedido['mesa']}")
            print(f"Garçom: {pedido['garcom']}")
            print("Itens pedidos:")
            for item, preco in pedido["itens"]:
                print(f" - {item}: R$ {preco:.2f}")
            print(f"Total a pagar: R$ {pedido['total']:.2f}")
            return
    print("Pedido não encontrado.")


# -------------------------------
# Menu interativo
# -------------------------------
def menu():
    while True:
        print("SISTEMA DE PEDIDOS")
        print("1. Exibir cardápio")
        print("2. Registrar pedido")
        print("3. Fechar conta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cardapio()
        elif opcao == "2":
            registrar_pedido()
        elif opcao == "3":
            fechar_conta()
        elif opcao == "4":
            print("Encerrando o sistema")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")


# Executa o sistema
menu()

'''nome = ('João', 22, 4800,50, 'Rua jota, N°80')
# tuplas são imutáveis 
print(type(nome))'''

# Listas são são mutáveis

'''cliente = ['João', 22, 4800,50, 'Rua jota, N°80'] 

# Listas PRECISAM  ser declaradas entre conchetes ###
 .append adiciona um item na lista

#telefone = 21993249085

cliente.append(telefone)'''

# como usar lista no for

'''cliente = [ ]

while True:
    try:
        num = int(input('Digite um N°: '))
        cliente.append(num)
        sair = input('Deseja inserir mais um N°? (S/N)').upper().strip()
        if sair == 'N':
            break
    except:
        print('Digite um N° inválido')
for i in cliente:
    print(i)'''

'''print('Opções 1\n2\n3\n4')

while True:
    try:
        opcao = int(input('Opcao: '))
        if opcao in [1, 2, 3, 4]:
            print('Opção ok')
            break
        else:
            print('Opção inválida')
    except: 
        print('Digite um N° válido')'''

# Sistema simples de cadastro de produtos


nomes = []
valores = []

qtd = int(input("Quantos produtos deseja cadastrar? "))

i = 0
while i < qtd:
    try:
        nome = input(f"Digite o nome do produto {i+1}: ")
        valor = float(input(f"Digite o valor do produto {i+1}: "))


    except:
        print("Entrada inválida. Tente novamente.")
        continue

    nomes.append(nome)
    valores.append(valor)

    i += 1  # contador do while

# Exibe relatório final
print("RELATÓRIO DE PRODUTOS")
for i in range(qtd):
    print(f"Produto {i+1}: {nomes[i]} - R$ {valores[i]:.2f}")



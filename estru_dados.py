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

nome_prod = [ ]
valor_prod = [ ]

while True:
    try:
        valor = float(input('Digite o valor do produto'))
        valor_prod.append(valor)
    sair = input('Deseja cadastrar mais valores? S/N').upper().strip

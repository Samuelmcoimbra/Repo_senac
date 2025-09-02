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

num_prod = int(input('Quantos produtos deseja cadastrar?:'))
valor_prod = [ ]
nome_prod = [ ]


while True:
    try:
        valor = float(input('Digite o valor do produto:\n'))
        valor_prod.append(valor)
        break
    except:
        print('Digite valores válidos')
while True:
     try:
        nome = input('Coloque o nome do produto:\n')
        nome_prod.append(nome)
        sair = input('Deseja cadastrar mais produtos? S/N\n').upper().strip
        if sair == 'N':
            break
     except:
         print('Digite nomes válidos')



print('O produto',nome_prod[1],'custa', valor_prod[1] )



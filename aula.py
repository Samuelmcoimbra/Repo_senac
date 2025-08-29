# .title() faz a primeira letra do input ficar maiuscula 
# upper() coloca todas as letras em maiusculo
# lower() coloca todas as letras minusculas

'''aluno = input('Digite seu nome: ')
# Repetição 1
while True:
    try:
        nota1 = float(input('Digite sua nota: '))
        break
    except:
        print('Digite números válidos')
# Repetição 2
while True:
    try:
        nota2 = float(input('Digite sua nota: '))
        break
    except:
        print('Digite números válidos')

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Aprovado!!') '''

# Atividade 3
nome = input('Digite seu nome: ')
dias = int(input('Digite quantos dias deseja ficar hospedado: '))

print('Tipos de quartos disponiveis')
print('1 - Quarto Genin: 120,00 R$ por noite')
print('2 - Quarto Jounin: 180,00 R$ por noite')
print('3 - Suite Hokage 250,00 R$ por noite')

tipo_de_quarto = input('Digite o quarto que deseja alugar: ')

if tipo_de_quarto == 1:
    nome_quarto = 'Quarto Genin'
    valor_quarto = 180
elif tipo_de_quarto == 2:
    nome_quarto = 'Quarto Jounin'
    valor_quarto = 180
elif tipo_de_quarto == 3:
    nome_quarto = 'Suite Hokage'
    valor_quarto = 250

valor_total = ...


'''contador = 1
while contador <= 5:
    print(f'Contador = {contador}')
    contador += 1 '''

'''senha = ''

while senha != '1234':
    senha = input('Digite a senha ').strip() # .strip tira o espaço (space) que o usuário digitar (string)
    if senha != '1234':
        print('Senha incorreta. Digite novamente')


print("Acesso liberado")'''


# Laço for com range()
# o for vai rodar quantas vezes eu determinar no range()

#for i in range(0 , 31 , 10): # A variável em for (no caso i) só será usada dentro do for
#    print(i)



'''while True:
    numero = float(input('Digite um número maior que 10: '))

    if numero > 10:
        print('Número aceito!!')
        break
    else:
        print('O número deve ser maior que 10')'''

for i in range(1, 11):
    print(f'7 x {i} = {7*i}')
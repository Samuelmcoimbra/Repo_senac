tarefas = []

while True:
    tarefa = input('Digite uma tarefa para adicionar tarefas, remover para remover tarefas ou sair para finalizar: ')
    
    if tarefa == 'remover':
        tarefa_remover = input('Digite a tarefa que deseja remover: ')
        if tarefa_remover in tarefas:
            tarefas.remove(tarefa_remover)
            print(f'Tarefa "{tarefa_remover}" removida com sucesso.')
        else:
            print(f'Tarefa "{tarefa_remover}" não encontrada na lista.')
    elif tarefa == 'sair':
        print('Finalizando o programa.')
        break  
    tarefas.append(tarefa)
    print(tarefas)
print(f'Suas tarefas são: {tarefas}')
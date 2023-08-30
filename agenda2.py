import os
agenda_nome=[]
agenda_telefone=[]
opcao=5
opcao1=0
os.system('cls')

while opcao<0 or opcao>4: #verfica se o usuário informou uma entrada válida (0 a 4)
    print('***************************')  
    print('Informe a opção desejada: ')
    print('(1) Inserir um novo contato')
    print('(2) Exibir a lista de contatos')
    print('(3) Editar um contato')
    print('(4) Remover um contato')
    print('(0) SAIR')
    print('***************************')  
    opcao = int(input("\nInforme a opção desejada: "))
    os.system('cls')

while opcao>0 and opcao<=4: #entra no loop caso o usuário informe uma das opções (1 a 4)
        if (opcao==1): #cadastrar novo contato
            os.system('cls')
            print('*****INSERIR UM NOVO CONTATO*****')   
            nome = input("Informe o nome do contato: ")
            print("Informe o telefone para o contato ", nome, ":")
            telefone = input()
            agenda_nome.append(nome)
            agenda_telefone.append(telefone)
            os.system('cls')
            print('Contato adicionado com sucesso!')
            print('***************************')  
            print('') 
            
        if (opcao==2): #listar os contatos cadastrados
            os.system('cls')
            print('*****CONTATOS CADASTRADOS*****')
            cont=0
            for p in agenda_nome: #imprime cada elemento da lista (para cada elemento, faça)
                print (p)
                print('Tel.: ', agenda_telefone[cont])
                print('')
                cont=cont+1  
            print('***************************')  
            print('')
             
        if (opcao==3): #editar um contato
            os.system('cls')
            print('*****EDITAR UM CONTATO*****')
            print('Informe o contato que deseja editar: \n')
            cont=1
            cont1=0
            for p in agenda_nome: #imprime cada elemento da lista (para cada elemento, faça)
                print(cont,": ")
                print (p)
                print('Tel.: ', agenda_telefone[cont1])
                print('')
                cont1=cont1+1
                cont=cont+1
            print('')

            opcao = int(input("\nContato nº: ")) #o usuario informa qual deseja editar dentre os usuarios listados
            opcao1 = int(input("\nVocê deseja alterar o (1)Nome ou (2)Telefone ? ")) #o usuario informa qual deseja editar dentre os usuarios listados
            
            if (opcao1 == 1):
                cont=cont-2
                nome = input("Informe o novo nome do contato: ")
                agenda_nome[cont]=nome
                os.system('cls')
                print('Nome do contato editado com sucesso')  
                print('***************************')
                            
            if (opcao == 2):
                cont=cont-2
                telefone = input("Informe o novo número de telefone: ")
                agenda_telefone[cont]=telefone
                os.system('cls')
                print('Telefone do contato editado com sucesso')  
                print('***************************')
                

        if (opcao==4): #remover contatos
            os.system('cls')
            print('*****REMOVER UM CONTATO***** ')
            print('Informe o contato que deseja remover: \n')
            cont=1
            cont1=0
            for p in agenda_nome: #imprime cada elemento da lista (para cada elemento, faça)
                print(cont,": ")
                print (p)
                print('Tel.: ', agenda_telefone[cont1])
                print('')
                cont1=cont1+1
                cont=cont+1
            print('')
            opcao = int(input("\nContato nº: ")) #o usuario informa qual deseja excluir dentre os usuarios listados
            opcao=opcao-1
            agenda_nome.pop(opcao) 
            agenda_telefone.pop(opcao) 
            os.system('cls')
            print("Contato removido com sucesso!")
            print('***************************')
            
        print('***************************')  #ao final do loop, o programa retorna o meu principal e, caso selecionando o menu 1 2 3 ou 4, reiniciará
        print('Informe a opção desejada: ')
        print('(1) Inserir um novo contato')
        print('(2) Exibir a lista de contatos')
        print('(3) Editar um contato')
        print('(4) Remover um contato')
        print('(0) SAIR')
        print('***************************')  
        opcao = int(input("\nInforme a opção desejada: "))
        os.system('cls')
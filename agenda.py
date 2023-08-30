import os
agenda=[]
nome=""
telefone=""
opcao=5
os.system('cls')

while opcao<0 or opcao>4:
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


while opcao>0 and opcao<=4:
        if (opcao==1):
            os.system('cls')
            print('*****INSERIR UM NOVO CONTATO*****')   
            nome = input("Informe o nome do contato: ")
            print("Informe o telefone para o contato ", nome, ":")
            telefone = input()
            agenda.append(nome+" "+telefone)
            os.system('cls')
            print('Contato adicionado com sucesso!')
            print('***************************')  
            print('') 
            

        if (opcao==2):
            os.system('cls')
            print('*****CONTATOS CADASTRADOS*****')
            for p in agenda: #imprime cada elemento da lista (para cada elemento, faça)
                print (p)
            print('***************************')  
            print('')
             
        
        if (opcao==3):
            os.system('cls')
            print('*****EDITAR UM CONTATO*****')
            print('Informe o contato que deseja editar: \n')
            cont=1
            for p in agenda: #imprime cada elemento da lista (para cada elemento, faça)
                print(cont,": ")
                print (p)
                print("")
                cont=cont+1
            print('')
            opcao = int(input("\nContato nº: "))
            nome = input("Informe o nome do contato: ")
            print("Informe o telefone para o contato ", nome, ":")
            telefone = input()
            cont=cont-2
            agenda[cont]=nome+" "+telefone
            print('Contato editado com sucesso')  
            print('***************************')  

        if (opcao==4):
            os.system('cls')
            print('*****REMOVER UM CONTATO***** ')
            print('Informe o contato que deseja remover: \n')
            cont=1
            for p in agenda: #imprime cada elemento da lista (para cada elemento, faça)
                print(cont,": ")
                print (p)
                print("")
                cont=cont+1
            
            opcao = int(input("\nContato nº: "))
            opcao=opcao-1
            agenda.pop(opcao) 
            print("Contato removido com sucesso!")
            print('***************************')  
            print("")

       
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
#----------Início das Variáveis Globais---------
lista_peca = []
codigo_peca = 0


#-----------Fim das Variáveis Globais------------


#----------Início de cadastrar peça()--------
def cadastrar_peca(codigo):
    print('Bem-vindo ao menu de Cadastrar peca.')
    print('Código da peça: {}'.format(codigo))
    nome = input('Entre com o NOME da peça: ')
    nome = nome.upper()    
    fabricante = input('Entre com o FABRICANTE da peça: ')
    fabricante = fabricante.upper() 
    preco = float(input('Entre com o PREÇO (R$) da peça: '))
    dicionario_peca ={'codigo'     : codigo,
                         'nome'       : nome,
                         'fabricante' : fabricante,
                         'preco'      : preco}
    lista_peca.append(dicionario_peca.copy())



#------------Fim de cadastrar peça()---------


#----------Início de consultar peça()--------
def consultar_peca():
    print('Bem-vindo ao menu de Consultar peças.')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada: \n' +
                            '1-Consultar TODAS as Peças\n' +
                            '2-Consultar Peças por CÓDIGO\n' +
                            '3-Consultar Peça(s) por FABRICANTE \n' +
                            '4-Retornar\n' +
                            '>> ')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar TODAS as Peças')
            for peca in lista_peca: # peca vai varrer toda a lista de peças
                print('----------------------')
                for key ,value in peca.items():  # varrer todos os conjuntos chaves e valor do dicionário peça
                    print('{}: {}' .format(key,value))
                print('----------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar Peça por CÓDIGO')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for peca in lista_peca:
                if peca['codigo'] ==valor_desejado: #o valor do campo codigo desse dicionário é igual o valor desejado
                    print('----------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos chaves e valor do dicionário peça
                        print('{}: {}'.format(key, value))
                    print('----------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Peça(s) por FABRICANTE')
            valor_desejado = input('Entre com o FABRICANTE desejado: ')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado:  # o valor do campo fabricante desse dicionário é igual o valor desejado
                    print('----------------------')
                    for key, value in peca.items():  # varrer todos os conjuntos chaves e valor do dicionário peça
                        print('{}: {}'.format(key, value))
                    print('----------------------')


        elif opcao_consultar == '4':
            return  #sai da função consultar _peca e volta para o main
        else:
            print('Opção inválida, tente novamente!')
            continue  # volta para o início do laço da função consultar_peca


#----------Fim de consultar peça()-----------


#----------Início de remover peça()----------
def remover_peca():
    print('Bem-vindo ao menu de Remover peça.')
    valor_desejado = int(input('Entre com o CÓDIGO da peça que deseja remover: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado:
            lista_peca.remove(peca)
            print('Peça removida com sucesso!')


#-----------Fim de remover peça()------------


#------------- Início do Main -------------------


print('Bem vindo ao controle de estoque da Loja de bikes do Ronny Wallace!')
while True:
    opcao_principal = input('\nEscolha a opção desejada: \n'+
                            '1-Cadastrar Peça\n'+
                            '2-Consultar Peça(s)\n'+
                            '3-Remover Peça\n'+
                            '4-Sair\n'+
                            '>> ')
    if opcao_principal == '1':
        codigo_peca += 1
        cadastrar_peca(codigo_peca)
    elif opcao_principal =='2':
        consultar_peca()
    elif opcao_principal =='3':
        remover_peca()
    elif opcao_principal =='4':
        break #encerra o laço principal e termina o programa
    else:
        print('Opção inválida, tente novamente!')
        continue  #volta para o início do laço do programa



#-------------- Fim do Main ---------------------

#Função volumeObjeto()
def volumeObjeto():
    print('-------------------- VOLUME --------------------')
    while True:
      try:
          altura = float(input('Digite a altura em centímetros(cm): '))
          comprimento = float(input('Digite o comprimento em centímetros(cm): '))
          largura = float(input('Digite a largura em centímetros(cm): '))
          volume = float(altura * comprimento * largura)
          print('A dimensão do objeto é de {} cm³ '.format(volume))


          if (volume <= 1000):  
            return 10.00

          elif (volume > 1000) and (volume < 10000): 
            return 20.00

          elif (volume >= 10000) and (volume < 30000): 
            return 30.00 

          elif (volume > 30000) and (volume < 100000): 
            return 50.00

          else:
            print('Volume inválido! Não trabalhamos com objetos com dimensões tão grandes. ')
            print('Por favor entre com o volume do objeto novamente.')
          continue # retorna para a pergunta

      except ValueError: #Caso o usuário digite letra ou caractere especial.
            print('Valor inválido! Você digitou algum valor não numérico.')
            print('Por favor entre com o volume do objeto novamente.')





#Fim da função volumeObjeto


# Função PesoObjeto()
def pesoObjeto():
    print('--------------------- PESO ---------------------')
    while True:
        try:
          peso = float(input('Qual o peso do objeto(KG)? '))
          print('O peso do objeto é {} .'.format(peso))
                       
      
          if peso <= 0.1: 
            return 1.0

          elif 0.1 <= peso < 1:
            return 1.5

          elif 1 <= peso < 10:
            return 2.0

          elif 10 <= peso < 30:
            return 3.0    

          else:
            print('Peso excede limites de Quilos permitidos!')
            print('Por digite o peso do objeto novamente.')
            continue # voltar para o início do laço (# retorna para pergunta)

        except ValueError or SyntaxError:
          print('Você digitou um caractere não numérico!')  
          print('Por digite o peso do objeto novamente.')

          continue  
#Fim da função pesoObjeto()


#Função Rota()
def valorRota():
    print('--------------------- ROTA ---------------------')
    
    while True:
        rota = input('Selecione a rota: \n'+
                                'CS - De Campinas até São Paulo  \n'+
                                'SC - De São Paulo até Campinas  \n'+
                                'BS - De Betim até São paulo \n'+
                                'SB - De São Paulo até Betim \n'+
                                'BC - De Betim até Campinas \n'+
                                'CB - De Campinas até Betim \n'+
                                '>> ')
        rota = rota.upper()
        if rota == 'CS' or rota == 'SC':
          return 1.0
       
        elif rota == 'BS' or rota == 'SB':
          return 1.2
          
        elif rota == 'BC' or rota == 'CB':
          return 1.5
            
        else:
            print('Opção inválida!')
            print('Entre com a rota novamente.')



#Fim da função Rota()


#Início do main
print('Seja bem vindo à Transportadora do Ronny Wallace.')


volume = volumeObjeto() # aonde as variáveis globais recebem as locais das funções


peso = pesoObjeto()


rota = valorRota()


total = (volume * peso * rota) # ocorre a multiplicação dos valores para se obter o valor total


print('O valor total da entrega ficou; R$ {:.2f} ( Volume: R$ {:.2f}, peso: R$ {:.2f}, rota: R$ {:.2f} )' .format(total, volume, peso, rota))


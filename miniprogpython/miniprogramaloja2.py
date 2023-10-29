print('Bem-vindo à lanchonete do Chefe Ronny Wallace ') # identificador pessoal


print('Olá, o que você deseja? ')


print('\033[33m_\033[m' * 52) # algumas formatações para deixar o programa mais visualmente agradável


print(f'\033[36m{" CARDÁPIO ":^48}\033[m') 


print('\033[33m_\033[m' * 52)



print('| Código |         Descrição         |   Valor(R$) |')
print('|  100   |      Cachorro-Quente      |     9,00    |')
print('|  101   |    Cachorro-Quente Duplo  |    11,00    |')
print('|  102   |           X-Egg           |    12,00    |')
print('|  103   |          X-Salada         |    13,00    |')
print('|  104   |          X-Bacon          |    14,00    |')
print('|  105   |           X-Tudo          |    17,00    |')
print('|  200   |      Refrigerante Lata    |     5,00    |')
print('|  201   |         Chá Gelado        |     4,00    |')


print('\033[32m_\033[m' * 52)


acumulador = 0 # variável que recebe o(s) valore(s) do(s) item(s) pedido pelo cliente
while True: # loop que será quebrado caso o cliente não queira mais nada
 
    codigo = input('Digite o código do produto desejado: ')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Opção inválida! Digite um código existente.')
        continue


    if codigo == '100':
        print('Você escolheu Cachorro-Quente no valor de R$ 9,00')
        acumulador = acumulador + 9.00 # pegue o valor que tinha no acumulador e some com 9

    elif codigo == '101':
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00')
        acumulador = acumulador + 11.00 

    elif codigo == '102':
        print('Você escolheu X-Egg no valor de R$ 12,00')
        acumulador = acumulador + 12.00 
 
    elif codigo == '103':
        print('Você escolheu X-Salada no valor de R$ 13,00')
        acumulador = acumulador + 13.00 

    elif codigo == '104':
        print('Você escolheu X-Bacon no valor de R$ 14,00')
        acumulador = acumulador + 14.00 
 
    elif codigo == '105':
        print('Você escolheu X-Tudo no valor de R$ 17,00')
        acumulador = acumulador + 17.00 
    
    elif codigo == '200':
        print('Você escolheu Refrigerante Lata no valor de R$ 5,00')
        acumulador = acumulador + 5.00 

    elif codigo == '201':
        print('Você escolheu Chá Gelado no valor de R$ 4,00')
        acumulador = acumulador + 4.00 
    
    print('Valor parcial do pedido R${:.2f}'.format(acumulador)) # informe na tela do quanto o pedido está custando 


    acrescimo = input('Deseja pedir mais um produto? \n' +
                     '1 - SIM \n' +
                     '0 - NÃO\n' + 
                     '>>') # acredito que para o usuário esta impressão é bem clean e intuitiva
    
    if acrescimo == '1':
        continue # continua a acrescentar itens ao pedido
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        print('Obrigado e volte sempre!!!') 
        break  # quebra do laço While True invocando o print com o valor final do pedido


    print('R$ ', acumulador)
   

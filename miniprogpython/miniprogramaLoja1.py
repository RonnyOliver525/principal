print('Bem-vindo à loja do Ronny Wallace!') # Identificador pessoal


valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade desejada: '))
desconto_produto = 0
# teste em cima da variável quantidade
if qtd_produto <= 9: # outra maneira seria: if qtd-produto < 10:
    desconto_produto = 0.00


elif qtd_produto >= 10 and qtd_produto <= 99:
    desconto_produto = 0.05


elif qtd_produto > 99 and qtd_produto <= 999: # poderia fazer >= 100 and < 1000
    desconto_produto = 0.10


else: # como não terá mais opções posso finalizar com else
    desconto_produto = 0.15


total_sem_desconto = valor_produto * qtd_produto # variável do preço do produto sem desconto
print('O valor sem desconto do produto foi: R$ {:.2f}'.format(total_sem_desconto)) # Printa na tela o valor sem desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto # Cria-se uma variável para calcular o preço já com desconto


print('O valor com desconto do produto foi: R$ {:.2f}'.format(total_com_desconto)) # imprime o valor na tela com o desconto.


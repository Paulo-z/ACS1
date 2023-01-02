divida = int(input())
valor_mensal = int(input())
pagamento = 0

while divida > 0:
    pagamento += 1
    print(f'pagamento: {pagamento}')
    print(f'antes = {divida}')
    if valor_mensal < divida:
        divida -= valor_mensal
    else:
        divida = 0 
    print(f'depois = {divida}')   
    print('-' * 5)   
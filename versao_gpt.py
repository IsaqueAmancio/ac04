valor_divida = int(input())
pagamento_mes = int(input())
n_pagamento = 0
while valor_divida > 0:
    copy_divida = valor_divida 
    n_pagamento += 1
    valor_divida = valor_divida - pagamento_mes
    if (valor_divida < 0):
        valor_divida = 0

    print(f"pagamento: {n_pagamento}\nantes = {copy_divida}\ndepois = {valor_divida}\n-----")
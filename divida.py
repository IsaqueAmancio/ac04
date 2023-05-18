
pagamento_total = 0
numero_pagamentos = 0
valor_div = int(input())
copy_div = valor_div
valor_original = valor_div 
while valor_div > 0:
    pagamento_m = int(input())
    pagamento_total += pagamento_m
    valor_div = valor_original - pagamento_total
    numero_pagamentos += 1
    print(f"pagamento: {numero_pagamentos}\nantes = {copy_div}\ndepois = {valor_div}\n-----")
    copy_div = valor_original - pagamento_total 
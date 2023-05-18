def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

inicio = int(input())
fim = int(input())

quantidade_primos = 0
primos = []

for num in range(inicio, fim+1):
    if eh_primo(num):
        quantidade_primos += 1
        primos.append(num)

for primo in primos:
    print(primo)

print("primos:", quantidade_primos)
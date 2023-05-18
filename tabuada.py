a = int(input())
b = int(input())
if(a<=b):
    for j in range(a,b+1):
        for i in range (1,11):
            print(f"{j} x {i} = {j*i}")
            if(i == 10):
                print("----------")
if(a>b):
    print("Nenhuma tabuada no intervalo!")

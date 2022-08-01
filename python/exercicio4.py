import os
print("================================")
print("======Programa de tabuada=======")
print("================================")

quantidade_tabuada = int(input("Digite o mumero de até quantos você quer a tabuada: "))
interator = int(input("Digite o numero para o interator: "))

os.system("clear")

print("================================")
print("======Programa de tabuada=======")
print("================================")

for i in range(1, quantidade_tabuada+1):
    print("===========================")
    print(f"======[Tabuada - {i}]=======")
    print("===========================")
    for j in range(1, interator+1):
        print(f"{j} * {i} = {j*i}")

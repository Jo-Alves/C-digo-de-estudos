import os
print("================================")
print("======Programa de tabuada=======")
print("================================")

quantidade_tabuada = int(input("Informe até quantos você quer que a tabuada seja calculada: "))
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

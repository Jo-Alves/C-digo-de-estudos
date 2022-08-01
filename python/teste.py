aluno = {}

aluno["nome"] = "Joelmir"
aluno["sobrenome"] = "carvalho"
# print(((10+10+9)/3))
# print("{:.2f}".format((10+10+9)/3))

nome, sobrenome = aluno.values()
print(nome)
print(sobrenome)

alunos = [
    {
        "nome": "Joelmir Rogério",
        "sobrenome": "Carvalho"
    },
    {
        "nome": "Valdirene Aparecida",
        "sobrenome": "Ferreira"
    }
]

for aluno in alunos:
    nome, sobrenome = aluno.values()
    print(f"{nome} {sobrenome}")


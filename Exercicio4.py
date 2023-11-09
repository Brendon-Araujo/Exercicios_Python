#  Faça um programa que pede duas notas de um aluno.
#  Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

b1 = float(input("Digite a nota de seu primeiro bimestre: "))
b2 = float(input("Digite a nota de seu segundo bimestre: "))
b3 = float(input("Digite a nota de seu terceiro bimestre: "))
b4 = float(input("Digite a nota de seu quarto bimestre: "))
bf = (b1 + b2 + b3 + b4) / 4

if bf == 10:
    print(f"Aprovado com Distinção!")
elif bf >= 7 and bf <= 9:
    print(f"Aprovado!")
else:
    print(f"Reprovado!")
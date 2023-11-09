# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o *
# seguinte critério, baseado no salário atual:
#
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5%
#     Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

salario: float; salariof: float; aumento: float
percentual: int
colaborador: str


colaborador = input(f"Qual o seu nome?")
print(f"Olá, {colaborador}, soube que você terá um aumento no seu salário!")
salario = float(input("Me informe quanto você recebe atualmente:"))

if salario <= 280:
    percentual = 20
    aumento = (salario * percentual) // 100
    salariof = aumento + salario

elif salario > 280 and salario <=700:
    percentual = 15
    aumento = (salario * percentual) // 100
    salariof = aumento + salario

elif salario > 700 and salario <=1500:
    percentual = 10
    aumento = (salario * percentual) // 100
    salariof = aumento + salario

else:
    percentual = 5
    aumento = (salario * percentual) // 100
    salariof = aumento + salario

print(f"Esse é o seu antigo salário: {salario:.2f}")
print(f"Essse é o percentual de aumento aplicado: {percentual}%")
print(f"Esse é o valor do aumento: {aumento:.2f}")
print(f"Esse é o novo salário, após o aumento: {salariof:.2f}")

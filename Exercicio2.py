nome1: str; nome2: str
salario1: float; salario2: float
idade1: int; idade2: int
sexo1: str; sexo2: str

nome1 = input("Nome da primeira pessoa: ")
idade1 = int(input("Qual a idade da primeira pessoa: "))
sexo1 = input("Digite o genero da primeira pessoa (M/F):")
salario1 = float(input("Salário da primeira pessoa: "))
nome2 = input("Nome da segunda pessoa: ")
idade2 = int(input("Qual a idade da segunda pessoa: "))
sexo2 = input("Digite o genero da segunda pessoa (M/F)")
salario2 = float(input("Salário da segunda pessoa: "))

print(f"A primeira pessoa se chama {nome1}, tem {idade1} anos, se identifica do genero {sexo1} "
      f"e recebe {salario1:.2f} reais de salário")
print("")
print(f"A segunda pessoa se chama {nome2}, tem {idade2} anos, se identifica do genero {sexo2} "
      f"e recebe {salario2:.2f} reais de salário")
print("")
print(f"Obrigado por chegar ate aqui! =)")
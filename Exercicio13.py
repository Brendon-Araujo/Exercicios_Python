#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input("Escreva seu nome: ")
idade = int(input("Escreva sua idade: "))
salario = float(input("Escreva seu salário: "))
sexo = input("Escreva seu genero(F/M): ")
estado_civil = input("Escreva o seu estado civil(S/C/V/D): ")

while len(nome) <= 3:
    nome = input("Insira um nome válido: ")

while idade < 0 or idade > 150:
    idade = int(input("Insira uma idade válida: "))

while salario <= 0:
    salario = float(input("Insira um salário válido: "))

while (sexo!= "F") or (sexo!= "M"):
    sexo = input("Insira o genero corretamente(F/M): ")
if sexo == "F":
    sexo = "Feminino(a)"
else:
    sexo = "Masculino(a)"

while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input("Insira um estado civil válido('S'/'C'/'V'/'D'):")

if estado_civil == 'S':
    estado_civil = "Solteiro(a)"
elif estado_civil == 'C':
    estado_civil = "Casado(a)"
elif estado_civil == 'V':
    estado_civil = "Viuvo(a)"
else:
    estado_civil = "Divorciado(a)"

print("Dados coletados com sucesso!")
print(f"Nome: {nome};")
print(f"Idade: {idade} anos;")
print(f"Salário: {salario:.2f} reais;")
print(f"Sexo: {sexo};")
print(f"Estado Civil: {estado_civil}.")
#Faça um programa que leia 5 números e informe o maior número.
maior = 0

for i in range(0, 5):
    x = int(input("Insira 1 número: "))
    if x > maior:
      maior = x

print(maior)
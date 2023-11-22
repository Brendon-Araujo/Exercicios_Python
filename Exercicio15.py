#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
media: int

for i in range(0,5):
    x = int(input("Escreva um numero: "))
    soma = soma + x

media = soma / 5

print(soma)
print(media)
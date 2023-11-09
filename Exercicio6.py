# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

a: int; b: int; c: int; maior: int; menor: int

print(f"Escreva 3 numeros e te direi qual é o maior e menor")
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print(f"O numero {maior} é o maior numero e {menor} é o menor numero dos 3 citados.")

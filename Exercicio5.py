# Faça um Programa que leia três números inteiros e mostre o maior deles.

a: int; b: int; c: int;

print(f"Escreva 3 numeros e te direi qual o maior")
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b and a > c:
    print(f"O numero {a} é o maior numero entre {b} e {c}")
elif b > a and b > c:
    print(f"O numero {b} é o maior numero entre {a} e {c}")
else:
    print(f"O numero {c} é o maior numero entre {a} e {b}")
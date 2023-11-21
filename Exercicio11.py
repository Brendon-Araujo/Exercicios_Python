#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#Mostre uma mensagem de erro e voltando a pedir as informações.

nome = input("USER: ")
senha = input("PASSWORD: ")

while nome == senha:
    print("ERROR, TRY AGAIN")
    nome = input("USER: ")
    senha = input("PASSWORD: ")

print("SESSION STARTED")
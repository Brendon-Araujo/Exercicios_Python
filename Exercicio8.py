nome = input("Insira o seu nome:")
admissao = input("Insira sua data de admissão(dd/mm/aaaa):")
salario = float(input("Insira o valor do seu salário atual:"))
emprestimo = float(input("Insira o valor desejado para emprestimo:"))
from datetime import datetime
hoje = datetime.now().date()
admissao = datetime.strptime(admissao, "%d/%m/%Y").date()
tempo_casa = (hoje - admissao).days // 365
if emprestimo % 2 != 0 or emprestimo > salario * 2:
    print("Insira um valor válido!")
elif tempo_casa < 5:
    print("Infelizmente você não atende os requisitos mínimos do programa.")
else:
    print(f"Escolha a melhor opção de pagamento em dinheiro vivo: ")
    print(f"Digite 1, para notas de maior valor")
    print(f"Digite 2, para notas de menor valor")
    print(f"Digite 3, para notas meio a meio")
metodo = int(input(""))

if metodo == 1:
    print(f"Valor empréstimo: {emprestimo} reais")
    print(f"Notas de maior valor:")
    cem = int(emprestimo / 100)
    cedula_cem = cem
    emprestimo = emprestimo - (cem*100)
    cem = 100 * 1

    cinquenta = int(emprestimo / 50)
    cedula_cinquenta = cinquenta
    emprestimo = emprestimo - (cinquenta * 50)
    cinquenta = 50 * 1

    vinte = int(emprestimo / 20)
    cedula_vinte = vinte
    emprestimo = emprestimo - (vinte*20)
    vinte = 20 * 1

    dez = int(emprestimo / 10)
    cedula_dez = dez
    emprestimo = emprestimo - (dez * 10)
    dez = 10 * 1

    dois = int(emprestimo / 2)
    cedula_dois = dois
    emprestimo = emprestimo - (dois * 2)
    dois = 2 * 1

    cinco = int(emprestimo / 5)
    cedula_cinco = cinco
    emprestimo = emprestimo - (cinco * 5)
    cinco = 5 * 1

    print(f"{cedula_cem}x{cem} reais;")
    print(f"{cedula_cinquenta}x{cinquenta} reais;")
    print(f"{cedula_vinte}x{vinte} reais;")
    print(f"{cedula_dez}x{dez} reais;")
    print(f"{cedula_cinco}x{cinco} reais;")
    print(f"{cedula_dois}x{dois} reais.")

elif metodo == 2:
    print(f"Valor empréstimo: {emprestimo} reais")
    print(f"Notas de menor valor:")

    vinte = int(emprestimo / 20)
    cedula_vinte = vinte
    emprestimo = emprestimo - (vinte * 20)
    vinte = 20 * 1

    dez = int(emprestimo / 10)
    cedula_dez = dez
    emprestimo = emprestimo - (dez * 10)
    dez = 10 * 1

    dois = int(emprestimo / 2)
    cedula_dois = dois
    emprestimo = emprestimo - (dois * 2)
    dois = 2 * 1

    cinco = int(emprestimo / 5)
    cedula_cinco = cinco
    emprestimo = emprestimo - (cinco * 5)
    cinco = 5 * 1

    cinquenta = int(emprestimo / 50)
    cedula_cinquenta = cinquenta
    emprestimo = emprestimo - (cinquenta * 50)
    cinquenta = 50 * 1

    cem = int(emprestimo / 100)
    cedula_cem = cem
    emprestimo = emprestimo - (cem * 100)
    cem = 100 * 1

    print(f"{cedula_vinte}x{vinte} reais;")
    print(f"{cedula_dez}x{dez} reais;")
    print(f"{cedula_cinco}x{cinco} reais;")
    print(f"{cedula_dois}x{dois} reais.")
    print(f"{cedula_cinquenta}x{cinquenta} reais;")
    print(f"{cedula_cem}x{cem} reais;")

elif metodo == 3:
    print(f"Valor empréstimo: {emprestimo} reais")
    print(f"Notas meio a meio:")
    meio_maior = emprestimo / 2
    meior_menor = emprestimo / 2
    print(f"{meio_maior} reais em notas de maior valor:")

    cem = int(meio_maior / 100)
    cedula_cem = cem
    meio_maior = meio_maior - (cem * 100)
    cem = 100 * 1

    cinquenta = int(meio_maior / 50)
    cedula_cinquenta = cinquenta
    meio_maior = meio_maior - (cinquenta * 50)
    cinquenta = 50 * 1

    vinte = int(meio_maior / 20)
    cedula_vinte = vinte
    meio_maior = meio_maior - (vinte * 20)
    vinte = 20 * 1

    dez = int(meio_maior / 10)
    cedula_dez = dez
    meio_maior = meio_maior - (dez * 10)
    dez = 10 * 1

    dois = int(meio_maior / 2)
    cedula_dois = dois
    meio_maior = meio_maior - (dois * 2)
    dois = 2 * 1

    cinco = int(meio_maior / 5)
    cedula_cinco = cinco
    meio_maior = meio_maior - (cinco * 5)
    cinco = 5 * 1

    print(f"{cedula_cem}x{cem} reais;")
    print(f"{cedula_cinquenta}x{cinquenta} reais;")
    print(f"{cedula_vinte}x{vinte} reais;")
    print(f"{cedula_dez}x{dez} reais;")
    print(f"{cedula_cinco}x{cinco} reais;")
    print(f"{cedula_dois}x{dois} reais.")
    print("")
    print(f"{meior_menor} reais em notas de  menor valor:")
    vinte = int(meior_menor / 20)
    cedula_vinte = vinte
    meior_menor = meior_menor - (vinte * 20)
    vinte = 20 * 1

    dez = int(meior_menor / 10)
    cedula_dez = dez
    meior_menor = meior_menor - (dez * 10)
    dez = 10 * 1

    dois = int(meior_menor / 2)
    cedula_dois = dois
    meior_menor = meior_menor - (dois * 2)
    dois = 2 * 1

    cinco = int(meior_menor / 5)
    cedula_cinco = cinco
    meior_menor = meior_menor - (cinco * 5)
    cinco = 5 * 1

    cinquenta = int(meior_menor / 50)
    cedula_cinquenta = cinquenta
    meior_menor = meior_menor - (cinquenta * 50)
    cinquenta = 50 * 1

    cem = int(meior_menor / 100)
    cedula_cem = cem
    meior_menor = meior_menor - (cem * 100)
    cem = 100 * 1

    print(f"{cedula_vinte}x{vinte} reais;")
    print(f"{cedula_dez}x{dez} reais;")
    print(f"{cedula_cinco}x{cinco} reais;")
    print(f"{cedula_dois}x{dois} reais.")
    print(f"{cedula_cinquenta}x{cinquenta} reais;")
    print(f"{cedula_cem}x{cem} reais;")
else:
    print(f"Insira um método valido!")
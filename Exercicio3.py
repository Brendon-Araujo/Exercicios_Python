# Hora do dia

hora = int(input(f"Digite uma hora do dia: "))

if hora < 12:
    print(f"Bom dia!")
elif hora < 18:
    print(f"Boa tarde!")
else:
    print(f"Boa noite!")
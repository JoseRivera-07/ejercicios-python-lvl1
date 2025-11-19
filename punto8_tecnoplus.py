
# Empresa TecnoPlus
tecnica = float(input("Nota técnica (0-5): "))
logica = float(input("Nota lógica (0-5): "))

if 0 <= tecnica <= 5 and 0 <= logica <= 5:
    nota_final = tecnica * 0.7 + logica * 0.3
    print("Nota final:", nota_final)

    if nota_final >= 3:
        print("Aprobado")
    elif nota_final >= 2:
        print("Revisión")
    else:
        print("Reprobado")
else:
    print("Notas fuera de rango")

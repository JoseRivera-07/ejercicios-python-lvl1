
# Parqueadero RapidCar
horas = int(input("Ingresa horas de uso: "))

if horas < 0:
    print("Horas inválidas")
else:
    if horas <= 5:
        total = horas * 2000
    else:
        total = horas * 2000 + 5000  # multa
    print("Total a pagar:", total)

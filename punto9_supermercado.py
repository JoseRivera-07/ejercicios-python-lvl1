
# Supermercado AhorroMax
cantidad = int(input("Ingresa cantidad de productos: "))

if cantidad < 0:
    print("Cantidad inválida")
else:
    total = cantidad * 2000

    if cantidad >= 30:
        total *= 0.85
    elif cantidad >= 10:
        total *= 0.95

    if total < 50000:
        total += 5000  # envío

    print("Total final:", int(total))

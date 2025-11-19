
# Librería El Saber
precio = 25000
est = input("¿Eres estudiante? (si/no): ").lower()
cupon = input("Ingresa cupón (si tienes): ")

total = precio

if est == "si":
    total *= 0.85  # 15% descuento
    if cupon == "LIBRO10":
        total *= 0.90  # 10% adicional
elif cupon == "LIBRO10":
    print("Cupón no válido para no estudiantes.")

print("Total final:", int(total))

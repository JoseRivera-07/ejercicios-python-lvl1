
# Restaurante El Sabor Colombiano
menu = 12000
bebida = input("¿Desea bebida? (si/no): ").lower()

total = menu
if bebida == "si":
    total += 3000

total *= 1.08  # IVA 8%

print("Total con IVA:", int(total))

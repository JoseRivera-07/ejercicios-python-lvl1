
# Heladería Frosty
sabor = input("Ingresa el sabor (chocolate/vainilla): ").lower()

precios = {
    "chocolate": 4000,
    "vainilla": 3500
}

if sabor not in precios:
    print("Sabor no disponible")
else:
    topping = input("¿Desea topping? (si/no): ").lower()
    total = precios[sabor]
    if topping == "si":
        total += 1000
    print("Total a pagar:", total)


# Club Noche Estelar
edad = int(input("Ingresa tu edad: "))
documento = input("¿Tienes documento? (si/no): ").lower()

if edad < 18:
    print("Entrada denegada")
else:
    if documento == "si":
        print("Bienvenido al club")
    else:
        print("Debe presentar documento")

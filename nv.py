def encontrar_s(numero):
    def encontrar(inicio, camino):
        if inicio == numero:
            return camino
        
        if inicio > numero:
            return None
        
        # Intenta sumando 5
        suma = encontrar(inicio + 5, f"({camino} + 5)")
        if suma is not None:
            return suma
        
        # Intenta multiplicando por 3
        multiplicacion = encontrar(inicio * 3, f"({camino} * 3)")
        if multiplicacion is not None:
            return multiplicacion

    return encontrar(1, "1")

numero_objetivo = int(input("Ingrese el número objetivo: "))

resultado = encontrar_s(numero_objetivo)

if resultado is not None:
    print(f"Se encontró una solución: {resultado}")
else:
    print(f"No hay manera de llegar a {numero_objetivo} desde 1 usando solo (+5) y (*3).")
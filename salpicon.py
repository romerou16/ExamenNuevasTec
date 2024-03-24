class Fruta:
    def __init__(self, id, nombre, precioUnitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precioUnitario = precioUnitario
        self.cantidad = cantidad

def calcularCostoTotal(frutas):
    costoTotal = sum(fruta.precioUnitario * fruta.cantidad for fruta in frutas)
    return costoTotal

def mostrarFrutasOrdenadasPorCosto(frutas):
    frutasOrdenadas = sorted(frutas, key=lambda fruta: fruta.precioUnitario, reverse=True)
    for fruta in frutasOrdenadas:
        print(f"{fruta.nombre}: ${fruta.precioUnitario * fruta.cantidad}")

def mostrarFrutaMasBarata(frutas):
    frutaMasBarata = min(frutas, key=lambda fruta: fruta.precioUnitario)
    print(f"La fruta más barata es: {frutaMasBarata.nombre} - ${frutaMasBarata.precioUnitario}")

def main():
    n = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    frutas = []
    for i in range(1, n + 1):
        id = i
        nombre = input(f"Ingrese el nombre de la fruta {i}: ")
        precioUnitario = float(input(f"Ingrese el precio unitario de {nombre}: "))
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
        frutas.append(Fruta(id, nombre, precioUnitario, cantidad))

    costoTotal = calcularCostoTotal(frutas)
    print("\nCosto total del salpicón:", costoTotal)

    print("\nFrutas ordenadas por costo:")
    mostrarFrutasOrdenadasPorCosto(frutas)

    print("\n")
    mostrarFrutaMasBarata(frutas)

if __name__ == "__main__":
    main()

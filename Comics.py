class Producto:
    def __init__(self, idProducto, nombre, precio, ubicacion, descripcion, casa, referencia, paisOrigen, unidades, garantia):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.paisOrigen = paisOrigen
        self.unidades = unidades
        self.garantia = garantia


class TiendaComics:
    def __init__(self):
        self.inventario = {}
        self.idCounter = 1

    def generarId(self):
        idGenerado = self.idCounter
        self.idCounter += 1
        return idGenerado

    def registrarProducto(self, nombre, precio, ubicacion, descripcion, casa, referencia, paisOrigen, unidades, garantia):
        idProducto = self.generarId()
        producto = Producto(idProducto, nombre, precio, ubicacion, descripcion, casa, referencia, paisOrigen, unidades, garantia)
        self.inventario[idProducto] = producto

    def mostrarProductosBodega(self):
        print("Productos en bodega:")
        for idProducto, producto in self.inventario.items():
            print(f"ID: {idProducto}, Nombre: {producto.nombre}, Precio: ${producto.precio}, Ubicación: {producto.ubicacion}")

    def buscarProductoPorNombre(self, nombre):
        for idProducto, producto in self.inventario.items():
            if producto.nombre.lower() == nombre.lower():
                print(f"ID: {idProducto}, Nombre: {producto.nombre}, Precio: ${producto.precio}, Descripción: {producto.descripcion}")
                return
        print("Producto no encontrado.")

    def modificarUnidadesCompradas(self, nombreProducto, nuevasUnidades):
        for idProducto, producto in self.inventario.items():
            if producto.nombre.lower() == nombreProducto.lower():
                if nuevasUnidades <= producto.unidades:
                    producto.unidades = nuevasUnidades
                    print("Unidades modificadas exitosamente.")
                else:
                    print("Error: La modificación no puede ser mayor al número inicial de unidades.")
                return
        print("Producto no encontrado.")



def mostrarMenu():
    print("\n*** Menú de opciones ***")
    print("1. Registrar un producto")
    print("2. Mostrar todos los productos en bodega")
    print("3. Buscar un producto por nombre")
    print("4. Modificar número de unidades compradas")
    print("5. Salir")



tienda = TiendaComics()


while True:
    mostrarMenu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario del producto: "))
        ubicacion = input("Ubicación en la tienda (A, B, C o D): ").upper()
        descripcion = input("Descripción del producto: ")
        casa = input("Casa a la que pertenece el producto: ")
        referencia = input("Referencia (código alfanumérico): ")
        paisOrigen = input("País de origen del producto: ")
        unidades = int(input("Número de unidades compradas del producto: "))
        garantia = input("Producto con garantía extendida (True/False): ").capitalize()
        tienda.registrarProducto(nombre, precio, ubicacion, descripcion, casa, referencia, paisOrigen, unidades, garantia == "True")

    elif opcion == "2":
        tienda.mostrarProductosBodega()

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        tienda.buscarProductoPorNombre(nombre)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto cuyas unidades desea modificar: ")
        nuevasUnidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        tienda.modificarUnidadesCompradas(nombre, nuevasUnidades)

    elif opcion == "5":
        print("¡Gracias por usar nuestro sistema de gestión de inventario!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

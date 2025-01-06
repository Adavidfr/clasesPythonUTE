class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}

    def agregarProducto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def buscarProducto(self, producto):
        if producto in self.productos:
            return f"{producto} está disponible en {self.nombre} con {self.productos[producto]} unidades."
        else:
            return f"{producto} no está disponible en {self.nombre}."

    def actualizarStock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
            if self.productos[producto] < 0:
                self.productos[producto] = 0
        else:
            self.productos[producto] = cantidad

    def mostrarStock(self):
        stock = f"Stock de {self.nombre}:\n"
        for producto, cantidad in self.productos.items():
            stock += f"{producto}: {cantidad} unidades\n"
        return stock

def main():
    tiendas = [
        Tienda("Tienda Norte"),
        Tienda("Tienda Centro"),
        Tienda("Tienda Sur")
    ]

    # Agregar productos de ejemplo
    productosEjemplo = [
        ("iPhone 12", 10),
        ("Samsung Galaxy S21", 15),
        ("Xiaomi Mi 11", 20)
    ]

    for tienda in tiendas:
        for producto, cantidad in productosEjemplo:
            tienda.agregarProducto(producto, cantidad)

    print("Bienvenido a Tiendas Micka.\nDisponemos de 3 tiendas:\n1. Tienda Norte\n2. Tienda Cetntro\n3. Tienda Sur\n\nA continuación se desplegará el menú, escoge una opción dentro del menú:")
    
    while True:
        
        print("\n1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar stock")
        print("4. Mostrar stock de todas las tiendas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tiendaNum = int(input("Ingrese el número de la tienda: ")) - 1
            if 0 <= tiendaNum < len(tiendas):
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                tiendas[tiendaNum].agregarProducto(producto, cantidad)
            else:
                print("Número de tienda no válido.")

        elif opcion == "2":
            producto = input("Ingrese el nombre del producto a buscar: ")
            for tienda in tiendas:
                print(tienda.buscarProducto(producto))

        elif opcion == "3":
            tiendaNum = int(input("Ingrese el número de la tienda: ")) - 1
            if 0 <= tiendaNum < len(tiendas):
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad a actualizar (puede ser negativa): "))
                tiendas[tiendaNum].actualizarStock(producto, cantidad)
            else:
                print("Número de tienda no válido.")

        elif opcion == "4":
            for tienda in tiendas:
                print(tienda.mostrarStock())

        elif opcion == "5":
            print("Gracias por usar el sistema de Tiendas Micka.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

main()
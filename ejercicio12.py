# Inventario inicial para dos tiendas y una bodega
inventario = {
    "iPhone 16": {"Tienda A": 15, "Tienda B": 10, "Bodega": 30},
    "Samsung Galaxy S22": {"Tienda A": 20, "Tienda B": 15, "Bodega": 40},
    "Xiaomi Redmi Note 13": {"Tienda A": 25, "Tienda B": 20, "Bodega": 50}
}

# Función para mostrar el inventario con un cuadro decorativo
def mostrarInventario():
    print("\n" + "=" * 40)
    print("         INVENTARIO ACTUAL         ")
    print("=" * 40)
    
    for producto, stock in inventario.items():
        print(f"\n{producto.center(38)}")
        print("-" * 40)
        for ubicacion, cantidad in stock.items():
            print(f"| {ubicacion.ljust(10)} | {str(cantidad).rjust(5)} unidades |")
        print("-" * 40)
    
    print("=" * 40 + "\n")

# Función para agregar un nuevo producto
def agregarProducto():
    producto = input("Ingresa el nombre del nuevo producto: ")
    if producto in inventario:
        print("El producto ya existe en el inventario.")
        return
    stockA = int(input("Ingresa el stock inicial para Tienda A: "))
    stockB = int(input("Ingresa el stock inicial para Tienda B: "))
    stockBodega = int(input("Ingresa el stock inicial para Bodega: "))
    inventario[producto] = {"Tienda A": stockA, "Tienda B": stockB, "Bodega": stockBodega}
    print(f"Producto '{producto}' agregado con éxito.")

# Función para registrar una venta
def registrarVenta():
    producto = input("Ingresa el nombre del producto que deseas vender: ")
    if producto not in inventario:
        print("Error: El producto no existe en el inventario.")
        return
    
    tienda = input("Selecciona la tienda desde donde deseas vender (Tienda A / Tienda B): ")
    if tienda not in ["tienda a", "tienda b"]:
        print("Error: Tienda no válida.")
        return
    
    cantidad = int(input(f"Ingresa la cantidad de '{producto}' que deseas vender desde {tienda}: "))
    
    if inventario[producto][tienda] >= cantidad:
        inventario[producto][tienda] -= cantidad
        print(f"Venta registrada: {cantidad} unidades de '{producto}' vendidas desde {tienda}.")
    else:
        faltante = cantidad - inventario[producto][tienda]
        if inventario[producto]["Bodega"] >= faltante:
            print(f"Stock insuficiente en {tienda}. Se tomarán {faltante} unidades de la bodega.")
            inventario[producto][tienda] = 0
            inventario[producto]["Bodega"] -= faltante
            print(f"Venta registrada: {cantidad} unidades de '{producto}' vendidas desde {tienda}.")
        else:
            print("Error: No hay suficiente stock total (incluyendo bodega) para realizar la venta.")
    
    mostrarInventario()

# Función para ingresar stock a un producto
def ingresarStock():
    producto = input("Ingresa el nombre del producto al que deseas agregar stock: ")
    if producto not in inventario:
        print("Error: El producto no existe en el inventario.")
        return
    
    ubicacion = input("Selecciona la ubicación donde deseas agregar stock (Tienda A / Tienda B / Bodega): ")
    if ubicacion not in ["Tienda A", "Tienda B", "Bodega"]:
        print("Error: Ubicación no válida.")
        return
    
    cantidad = int(input(f"Ingresa la cantidad de '{producto}' que deseas agregar a {ubicacion}: "))
    inventario[producto][ubicacion] += cantidad
    print(f"Se han agregado {cantidad} unidades de '{producto}' a {ubicacion}.")
    
    mostrarInventario()

# Menú principal
def menu():
    while True:
        print("\n" + "=" * 50)
        print("|     BIENVENIDO AL SISTEMA DE TIENDAS MIKA      |")
        print("=" * 50)  
        print("|             --- Menú de Inventario ---         |")
        print("|  1. Mostrar inventario                         |")
        print("|  2. Agregar nuevo producto                     |")
        print("|  3. Registrar venta                            |")
        print("|  4. Ingresar stock a un producto               |")
        print("|  5. Salir                                      |")
        print("=" * 50)
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrarInventario()
        elif opcion == "2":
            agregarProducto()
        elif opcion == "3":
            registrarVenta()
        elif opcion == "4":
            ingresarStock()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()

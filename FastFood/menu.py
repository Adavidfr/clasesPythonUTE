import tkinter as tk

ventana = tk.Tk()
ventana.title("McDonalds")
ventana.geometry("600x500")

saludo = tk.Label(ventana, text="Bienvenido a McDonalds") 
saludo.grid()

def modificarCantidad(label, cantidad_var, operacion, precio, label_total):
    if operacion == 'sumar':
        cantidad_var[0] += precio
    elif operacion == 'restar' and cantidad_var[0] > 0:  
        cantidad_var[0] -= precio
    label.config(text=str(cantidad_var[0]))  
    calcularTotal()  

def calcularTotal():
    total = (cantidadHamburguesa[0] + cantidadPapas[0] + cantidadGaseosa[0])
    labelTotal.config(text="Total: $" + str(total))

cantidadHamburguesa = [0.0]
cantidadPapas = [0.0]
cantidadGaseosa = [0.0]

precioHamburguesa = 3.50
precioPapas = 1.50
precioGaseosa = 1.00

# Hamburguesa
hamburguesa = tk.Label(ventana, text="Hamburguesa")
hamburguesa.grid(row=8, column=0)

precioHamburguesaLabel = tk.Label(ventana, text="Precio: $3.50")
precioHamburguesaLabel.grid(row=8, column=1)

cantidadLabelHamburguesa = tk.Label(ventana, text="0.0")
cantidadLabelHamburguesa.grid(row=8, column=2)

botonSumarHamburguesa = tk.Button(ventana, text="+", command=lambda: modificarCantidad(cantidadLabelHamburguesa, cantidadHamburguesa, 'sumar', precioHamburguesa, None))
botonSumarHamburguesa.grid(row=8, column=3)

botonRestarHamburguesa = tk.Button(ventana, text="-", command=lambda: modificarCantidad(cantidadLabelHamburguesa, cantidadHamburguesa, 'restar', precioHamburguesa, None))
botonRestarHamburguesa.grid(row=8, column=4)

# Papas
papas = tk.Label(ventana, text="Papas")
papas.grid(row=9, column=0)

precioPapasLabel = tk.Label(ventana, text="Precio: $1.50")
precioPapasLabel.grid(row=9, column=1) 

cantidadLabelPapas = tk.Label(ventana, text="0.0")
cantidadLabelPapas.grid(row=9, column=2)

botonSumarPapas = tk.Button(ventana, text="+", command=lambda: modificarCantidad(cantidadLabelPapas, cantidadPapas, 'sumar', precioPapas, None))
botonSumarPapas.grid(row=9, column=3)

botonRestarPapas = tk.Button(ventana, text="-", command=lambda: modificarCantidad(cantidadLabelPapas, cantidadPapas, 'restar', precioPapas, None))
botonRestarPapas.grid(row=9, column=4)

# Gaseosa
gaseosa = tk.Label(ventana, text="Gaseosa")
gaseosa.grid(row=10, column=0)

precioGaseosaLabel = tk.Label(ventana, text="Precio: $1.00")
precioGaseosaLabel.grid(row=10, column=1) 

cantidadLabelGaseosa = tk.Label(ventana, text="0.0")
cantidadLabelGaseosa.grid(row=10, column=2)

botonSumarGaseosa = tk.Button(ventana, text="+", command=lambda: modificarCantidad(cantidadLabelGaseosa, cantidadGaseosa, 'sumar', precioGaseosa, None))
botonSumarGaseosa.grid(row=10, column=3)

botonRestarGaseosa = tk.Button(ventana, text="-", command=lambda: modificarCantidad(cantidadLabelGaseosa, cantidadGaseosa, 'restar', precioGaseosa, None))
botonRestarGaseosa.grid(row=10, column=4)

# Label para mostrar el total final
labelTotal = tk.Label(ventana, text="Total: $0.0")
labelTotal.grid(row=11, column=0, columnspan=6)

ventana.mainloop()

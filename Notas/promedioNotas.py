import tkinter as tk
import iterar

notas = []

def calcularPromedio(notas):
    if len(notas) == 0:
        return 0
    else: 
        total = sum(notas)
        promedio = total / len(notas)
        return promedio
    
def agregar():
    nota = float(txtNota.get())
    notas.append(nota)
    print("Lista de notas", notas)
    
def llamarPromedio():
    promedio = calcularPromedio(notas)
    lblPromedio.config(text=f"promedio: {promedio}")
    

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Formulario de notas")
lblNota = tk.Label(ventana, text = "Ingrese nota: ").pack()
txtNota = tk.Entry(ventana)
txtNota.pack()
btnIngresar = tk.Button(text = "Ingresar", command=agregar).pack()
btnPromedio = tk.Button(text = "Promediar", command=llamarPromedio).pack()
lblPromedio = tk.Label(ventana, text="")
lblPromedio.pack()

ventana.mainloop()
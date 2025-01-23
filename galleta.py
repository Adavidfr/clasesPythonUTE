import tkinter as tk
import random 

def generarFortuna():
    mensajes=["encontrar el amor","sal de ahi","no volver con tu ex","vas ser tu dia de suerte","ten cuidado","algo bueno va ha suceder","algo malo va ha suceder"]
    fortuna=random.choice(mensajes)
    lblMensaje.config(text=fortuna)


ventana=tk.Tk()
ventana.geometry("400x400")

lbltitulo=tk.Label(text="galleta de la fortuna")
lbltitulo.pack()

btnbutton=tk.Button(text="generar fortuna", command=generarFortuna)
btnbutton.pack()

lblMensaje=tk.Label(text="",fg="RED")
lblMensaje.pack()

ventana.mainloop()
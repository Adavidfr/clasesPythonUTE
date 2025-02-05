import tkinter as tk    

root = tk.Tk()     

root.title("Celulares Mika")
root.geometry("540x260")

saludo = tk.Label(root, text="TITULO", font=("Arial", 20)) 
n1 = tk.Label(root, text="Ingrese n1: ", font=("Arial", 14))
textN1 = tk.Text(root, height=5, width=30, bg="light blue")

n2 = tk.Label(root, text="Ingrese n2: ", font=("Arial", 14))
textN2 = tk.Text(root, height=5, width=30, bg="light blue")

total = tk.Label(root, text="Total: ", font=("Arial", 14))
textTotal = tk.Text(root, height=5, width=30, bg="light blue")

button = tk.Button(root, text="Sumar", font=("Arial", 14 ), command=root.quit) 

saludo.pack()

n1.place(x=10 , y=40)
textN1.place(x=150 , y=40, height=30, width=200)

n2.place(x=10 , y=80)
textN2.place(x=150 , y=80, height=30, width=200)

total.place(x=220 , y=120)
textTotal.place(x=300 , y=120, height=30, width=200)

button.place(x=230 , y=180)

root.mainloop()
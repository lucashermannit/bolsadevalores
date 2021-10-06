import tkinter

ventana = tkinter.Tk()
ventana.geometry("720x380")

etiqueta = tkinter.Label(ventana, text = "Compra y Venta de acciones")
etiqueta.pack(fill = tkinter.X, expand = True)

def iniciar():
    print("iniciando...")

boton = tkinter.Button(ventana, text= "Iniciar", command = iniciar)
boton.pack()

ventana.mainloop()
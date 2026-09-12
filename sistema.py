import tkinter as tk
from tkinter import ttk, messagebox, Entry, Button
from fpdf import FPDF
from datetime import datetime
ventana=tk.Tk()
ventana.title("sistema de arte encantada")
ventana.geometry("900x500")
ventana.resizable(False, False)
#Funcionde añadir
def anadir():
    
    nombre = producto.get()

    try:
        precio_unitario = float(precio.get())
        cantidad = int(cantida.get())

        if nombre == "":
            messagebox.showwarning(
                "Aviso",
                "Ingrese el nombre del producto"
            )
            return

        if cantidad <= 0:
            messagebox.showwarning(
                "Aviso",
                "La cantidad debe ser mayor que 0"
            )
            return

        total = precio_unitario * cantidad

        tabla.insert(
            "",
            tk.END,
            values=(
                nombre,
                cantidad,
                f"${precio_unitario:.2f}",
                f"${total:.2f}"
            )
        )

        producto.delete(0, tk.END)
        cantida.delete(0, tk.END)
        precio.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un precio y una cantidad válidos"
        )
#Botoenimilia

def eliminar():
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showwarning(
            "Aviso",
            "Seleccione una venta de la tabla"
        )
        return

    for item in seleccionado:
        tabla.delete(item)
#borrar
def borrar():
    respuesta=messagebox.askyesno(
         "Confirmar",
         "¿Desea borrar todas las ventas?"
    )
    if respuesta:
        for item in tabla.get_children():
            tabla.delete(item)


#titulo
texto=tk.Label(ventana, text="Sistema de Arte Encantada", font=("arial", 16))
texto.grid(row=0, column=0)
texto.pack(pady=15)

#producto
tk.Label(ventana, text="productos:",font=("arial", 10) ).place(x=58, y=60)
producto=Entry(ventana, width=20, font=("arial", 10))
producto.place(x=129 , y=60)
#precio
tk.Label(ventana,text="precio:", font=("arial",10)).place(x=305,y=60 )
precio=Entry(ventana,width=20, font=("arial",10))
precio.place(x=355,y=60)
#cantidad
tk.Label(ventana, text="cantidad:", font=("arial",10)).place(x=550, y=60)
cantida=Entry(ventana, width=20, font=("arial", 10))
cantida.place(x=625, y=60 )
#botonañadir 
bnt_añadir=Button(ventana, text="Añadir", command=anadir, font=("arial", 10))
bnt_añadir.place(x=150,y=120)
#botoneliminar
btn_eliminar=Button(ventana,text="Eliminar",  command=eliminar,font=("arial",10))
btn_eliminar.place(x=350, y=120)
#BOTOBORRAR
btn_borrar=Button(ventana,text="Borrar",command=borrar,font=("arial",10))
btn_borrar.place(y=120,x=650)
# Tabla
comnula=(
    "Productos","Cantidad","Precio Unitario", "Precio Total"
)
tabla=ttk.Treeview(
    ventana,
    columns=comnula,
    show="headings",
    height=10
)
# Encabezados

tabla.heading("Productos",text="Productos")
tabla.heading("Precio Unitario",text="Precio Unitario")
tabla.heading("Cantidad",text="Cantidad")
tabla.heading("Precio Total",text="Precio Total")
# Ancho de columnas

tabla.column("Productos", width=250)
tabla.column("Precio Unitario", width=150)
tabla.column("Cantidad", width=100)
tabla.column("Precio Total", width=150)

tabla.place(
    x=100,
    y=180
)

ventana.mainloop()
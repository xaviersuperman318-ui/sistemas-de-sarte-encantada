import tkinter as tk
from tkinter import ttk, messagebox, Entry, Button
from fpdf import FPDF
from datetime import datetime

# =========================
# VENTANA
# =========================

ventana = tk.Tk()

ventana.title("Sistema de Arte Encantada")
ventana.geometry("900x500")
ventana.resizable(False, False)


# =========================
# TÍTULO
# =========================

texto = tk.Label(
    ventana,
    text="Sistema de Arte Encantada",
    font=("arial", 16)
)

texto.pack(pady=15)


# =========================
# PRODUCTO
# =========================

tk.Label(
    ventana,
    text="Producto:",
    font=("arial", 10)
).place(x=58, y=60)

producto = Entry(
    ventana,
    width=20,
    font=("arial", 10)
)

producto.place(x=129, y=60)


# =========================
# PRECIO
# =========================

tk.Label(
    ventana,
    text="Precio:",
    font=("arial", 10)
).place(x=305, y=60)

precio = Entry(
    ventana,
    width=20,
    font=("arial", 10)
)

precio.place(x=355, y=60)


# =========================
# CANTIDAD
# =========================

tk.Label(
    ventana,
    text="Cantidad:",
    font=("arial", 10)
).place(x=550, y=60)

cantida = Entry(
    ventana,
    width=20,
    font=("arial", 10)
)

cantida.place(x=625, y=60)


# =========================
# FUNCIÓN AÑADIR
# =========================

def añadir():
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

        # Limpiar campos
        producto.delete(0, tk.END)
        precio.delete(0, tk.END)
        cantida.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese un precio y una cantidad válidos"
        )


# =========================
# FUNCIÓN ELIMINAR
# =========================

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


# =========================
# FUNCIÓN BORRAR TODO
# =========================

def borrar():
    respuesta = messagebox.askyesno(
        "Confirmar",
        "¿Desea borrar todas las ventas?"
    )

    if respuesta:
        for item in tabla.get_children():
            tabla.delete(item)


# =========================
# BOTÓN AÑADIR
# =========================

btn_añadir = Button(
    ventana,
    text="Añadir",
    font=("arial", 10),
    command=añadir
)

btn_añadir.place(x=150, y=120)


# =========================
# BOTÓN ELIMINAR
# =========================

btn_eliminar = Button(
    ventana,
    text="Eliminar",
    font=("arial", 10),
    command=eliminar
)

btn_eliminar.place(x=350, y=120)


# =========================
# BOTÓN BORRAR
# =========================

btn_borrar = Button(
    ventana,
    text="Borrar",
    font=("arial", 10),
    command=borrar
)

btn_borrar.place(x=650, y=120)


# =========================
# TABLA
# =========================

columnas = (
    "Producto",
    "Cantidad",
    "Precio Unitario",
    "Precio Total"
)

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=10
)


# =========================
# ENCABEZADOS
# =========================

tabla.heading(
    "Producto",
    text="Producto"
)

tabla.heading(
    "Cantidad",
    text="Cantidad"
)

tabla.heading(
    "Precio Unitario",
    text="Precio Unitario"
)

tabla.heading(
    "Precio Total",
    text="Precio Total"
)


# =========================
# ANCHO DE COLUMNAS
# =========================

tabla.column(
    "Producto",
    width=250
)

tabla.column(
    "Cantidad",
    width=100
)

tabla.column(
    "Precio Unitario",
    width=150
)

tabla.column(
    "Precio Total",
    width=150
)


# =========================
# UBICACIÓN TABLA
# =========================

tabla.place(
    x=100,
    y=180
)


# =========================
# INICIAR
# =========================

ventana.mainloop()
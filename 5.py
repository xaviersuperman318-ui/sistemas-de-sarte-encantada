import tkinter as tk
from tkinter import ttk, messagebox, Entry, Button
from fpdf import FPDF
from datetime import datetime

# ==============================
# VENTANA PRINCIPAL
# ==============================

ventana = tk.Tk()
ventana.title("Sistema de Arte Encantada")
ventana.geometry("900x500")
ventana.resizable(False, False)

# ==============================
# TÍTULO
# ==============================

texto = tk.Label(
    ventana,
    text="Sistema de Arte Encantada",
    font=("Arial", 16)
)
texto.pack(pady=15)

# ==============================
# PRODUCTO
# ==============================

tk.Label(
    ventana,
    text="Producto:",
    font=("Arial", 10)
).place(x=58, y=60)

producto = Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)
producto.place(x=129, y=60)

# ==============================
# PRECIO
# ==============================

tk.Label(
    ventana,
    text="Precio:",
    font=("Arial", 10)
).place(x=305, y=60)

precio = Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)
precio.place(x=355, y=60)

# ==============================
# CANTIDAD
# ==============================

tk.Label(
    ventana,
    text="Cantidad:",
    font=("Arial", 10)
).place(x=550, y=60)

cantida = Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)
cantida.place(x=625, y=60)

# ==============================
# TABLA
# ==============================

columnas = (
    "Productos",
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

# Encabezados
tabla.heading("Productos", text="Producto")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Precio Unitario", text="Precio Unitario")
tabla.heading("Precio Total", text="Precio Total")

# Ancho de columnas
tabla.column("Productos", width=250)
tabla.column("Cantidad", width=100)
tabla.column("Precio Unitario", width=150)
tabla.column("Precio Total", width=150)

tabla.place(
    x=100,
    y=180
)

# ==============================
# TOTAL GENERAL
# ==============================

tk.Label(
    ventana,
    text="Total General:",
    font=("Arial", 12, "bold")
).place(x=550, y=410)

total_general = tk.Label(
    ventana,
    text="$0.00",
    font=("Arial", 12, "bold")
)
total_general.place(x=680, y=410)



# ==============================
# BOTÓN AÑADIR
# ==============================

btn_añadir = Button(
    ventana,
    text="Añadir",
    font=("Arial", 10),
)
btn_añadir.place(x=150, y=120)

# ==============================
# BOTÓN ELIMINAR
# ==============================

btn_eliminar = Button(
    ventana,
    text="Eliminar",
    font=("Arial", 10),
)
btn_eliminar.place(x=350, y=120)

# ==============================
# BOTÓN BORRAR
# ==============================

btn_borrar = Button(
    ventana,
    text="Borrar",
    font=("Arial", 10),
)
btn_borrar.place(x=650, y=120)

# ==============================
# EJECUTAR PROGRAMA
# ==============================

ventana.mainloop()


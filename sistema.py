
import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF
from datetime import datetime


# =========================
# VENTANA PRINCIPAL
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
    font=("Arial", 16)
)

texto.pack(pady=15)


# =========================
# PRODUCTO
# =========================

tk.Label(
    ventana,
    text="Producto:",
    font=("Arial", 10)
).place(x=58, y=60)

producto = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)

producto.place(x=129, y=60)


# =========================
# PRECIO
# =========================

tk.Label(
    ventana,
    text="Precio:",
    font=("Arial", 10)
).place(x=305, y=60)

precio = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)

precio.place(x=355, y=60)


# =========================
# CANTIDAD
# =========================

tk.Label(
    ventana,
    text="Cantidad:",
    font=("Arial", 10)
).place(x=550, y=60)

cantidad = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)

cantidad.place(x=625, y=60)


# =========================
# BOTÓN AÑADIR
# =========================

btn_añadir = tk.Button(
    ventana,
    text="Añadir",
    font=("Arial", 10),

)

btn_añadir.place(x=150, y=120)


# =========================
# BOTÓN ELIMINAR
# =========================

btn_eliminar = tk.Button(
    ventana,
    text="Eliminar",
    font=("Arial", 10)
)

btn_eliminar.place(x=350, y=120)


# =========================
# BOTÓN BORRAR
# =========================

btn_borrar = tk.Button(
    ventana,
    text="Borrar",
    font=("Arial", 10)
)

btn_borrar.place(x=650, y=120)


# =========================
# TABLA
# =========================

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


# =========================
# ENCABEZADOS
# =========================

tabla.heading(
    "Productos",
    text="Productos"
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
    "Productos",
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
# UBICACIÓN DE LA TABLA
# =========================

tabla.place(
    x=100,
    y=180
)
import tkinter as tk
from tkinter import ttk, messagebox, Entry, Button
from fpdf import FPDF
from datetime import datetime


# ==========================================
# VENTANA
# ==========================================

ventana = tk.Tk()
ventana.title("Sistema de Arte Encantada")
ventana.geometry("900x580")
ventana.resizable(False, False)


# ==========================================
# NÚMERO DE NOTA
# ==========================================

numero_nota = 1


# ==========================================
# CALCULAR TOTAL
# ==========================================

def calcular_total():

    total_general = 0

    for item in tabla.get_children():

        datos = tabla.item(item, "values")

        precio_total = float(
            datos[3].replace("$", "")
        )

        total_general += precio_total

    total_label.config(
        text=f"Total General: ${total_general:.2f}"
    )

    return total_general


# ==========================================
# AÑADIR PRODUCTO
# ==========================================

def anadir():

    nombre = producto.get().strip()

    try:

        precio_unitario = float(precio.get())
        cantidad = int(cantida.get())

        if nombre == "":
            messagebox.showwarning(
                "Aviso",
                "Ingrese el nombre del producto"
            )
            return

        if precio_unitario < 0:
            messagebox.showwarning(
                "Aviso",
                "El precio no puede ser negativo"
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

        calcular_total()

        producto.delete(0, tk.END)
        precio.delete(0, tk.END)
        cantida.delete(0, tk.END)

        producto.focus()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingrese un precio y una cantidad válidos"
        )


# ==========================================
# ELIMINAR PRODUCTO
# ==========================================

def eliminar():

    seleccionado = tabla.selection()

    if not seleccionado:

        messagebox.showwarning(
            "Aviso",
            "Seleccione un producto de la tabla"
        )

        return

    for item in seleccionado:
        tabla.delete(item)

    calcular_total()


# ==========================================
# BORRAR TODO
# ==========================================

def borrar():

    respuesta = messagebox.askyesno(
        "Confirmar",
        "¿Desea borrar todas las ventas?"
    )

    if respuesta:

        for item in tabla.get_children():
            tabla.delete(item)

        calcular_total()

        abono.delete(0, tk.END)
        nombre_cliente.delete(0, tk.END)

        saldo_label.config(
            text="Saldo: $0.00"
        )


# ==========================================
# CALCULAR ABONO Y SALDO
# ==========================================

def calcular_saldo():

    try:

        total = calcular_total()

        valor_abono = abono.get().strip()

        if valor_abono == "":
            valor_abono = 0
        else:
            valor_abono = float(valor_abono)

        if valor_abono < 0:

            messagebox.showwarning(
                "Aviso",
                "El abono no puede ser negativo"
            )

            return

        if valor_abono > total:

            messagebox.showwarning(
                "Aviso",
                "El abono no puede ser mayor que el total"
            )

            return

        saldo = total - valor_abono

        saldo_label.config(
            text=f"Saldo: ${saldo:.2f}"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingrese un abono válido"
        )


# ==========================================
# GENERAR NOTA DE VENTA
# ==========================================

def generar_nota():

    global numero_nota
    direccion = direccion_cliente.get().strip()
    telefono = telefono_cliente.get().strip()
    cliente = nombre_cliente.get().strip()
    


    if cliente == "":

        messagebox.showwarning(
            "Aviso",
            "Ingrese el nombre del cliente"
        )

        return

    if not tabla.get_children():

        messagebox.showwarning(
            "Aviso",
            "Agregue al menos un producto"
        )

        return

    # --------------------------------------
    # TOTAL
    # --------------------------------------

    total = calcular_total()

    # --------------------------------------
    # ABONO
    # --------------------------------------

    try:

        valor_abono = abono.get().strip()

        if valor_abono == "":
            valor_abono = 0
        else:
            valor_abono = float(valor_abono)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingrese un abono válido"
        )

        return

    # --------------------------------------
    # VALIDAR ABONO
    # --------------------------------------

    if valor_abono < 0:

        messagebox.showwarning(
            "Aviso",
            "El abono no puede ser negativo"
        )

        return

    if valor_abono > total:

        messagebox.showwarning(
            "Aviso",
            "El abono no puede ser mayor que el total"
        )

        return

    # --------------------------------------
    # SALDO
    # --------------------------------------

    saldo = total - valor_abono

    # --------------------------------------
    # FECHA
    # --------------------------------------

    fecha = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    # --------------------------------------
    # NOMBRE PDF
    # --------------------------------------

    nombre_archivo = (
        f"Nota_Venta_{numero_nota:06d}.pdf"
    )

    # --------------------------------------
    # CREAR PDF
    # --------------------------------------

    pdf = FPDF()

    pdf.add_page()

    # ENCABEZADO

    pdf.set_font(
        "Arial",
        "B",
        18
    )

    pdf.cell(
        0,
        10,
        "ARTE ENCANTADA",
        ln=True,
        align="C"
    )

    pdf.set_font(
        "Arial",
        "B",
        14
    )

    pdf.cell(
        0,
        10,
        "NOTA DE VENTA",
        ln=True,
        align="C"
    )

    pdf.ln(5)

    # DATOS

    pdf.set_font(
        "Arial",
        "",
        11
    )

    pdf.cell(
        0,
        8,
        f"Numero de nota: {numero_nota:06d}",
        ln=True
    )

    pdf.cell(
        0,
        8,
        f"Fecha: {fecha}",
        ln=True
    )

    pdf.cell(
        0,
        8,
        f"Cliente: {cliente}",
        ln=True
    )
    pdf.cell(
    0,
    8,
    f"Dirección: {direccion}",
    ln=True
    )
    pdf.cell(
    0,
    8,
    f"Teléfono: {telefono}",
    ln=True
)

    pdf.ln(5)

    # --------------------------------------
    # TABLA PDF
    # --------------------------------------

    pdf.set_font(
        "Arial",
        "B",
        10
    )

    pdf.cell(
        65,
        8,
        "Producto",
        border=1
    )

    pdf.cell(
        25,
        8,
        "Cantidad",
        border=1
    )

    pdf.cell(
        45,
        8,
        "Precio Unit.",
        border=1
    )

    pdf.cell(
        45,
        8,
        "Total",
        border=1
    )

    pdf.ln()

    # --------------------------------------
    # PRODUCTOS
    # --------------------------------------

    pdf.set_font(
        "Arial",
        "",
        10
    )

    for item in tabla.get_children():

        datos = tabla.item(
            item,
            "values"
        )

        nombre = datos[0]
        cantidad = datos[1]
        precio_unitario = datos[2]
        precio_total = datos[3]

        pdf.cell(
            65,
            8,
            nombre,
            border=1
        )

        pdf.cell(
            25,
            8,
            cantidad,
            border=1,
            align="C"
        )

        pdf.cell(
            45,
            8,
            precio_unitario,
            border=1,
            align="R"
        )

        pdf.cell(
            45,
            8,
            precio_total,
            border=1,
            align="R"
        )

        pdf.ln()

    # --------------------------------------
    # TOTAL
    # --------------------------------------

    pdf.ln(5)

    pdf.set_font(
        "Arial",
        "B",
        11
    )

    pdf.cell(
        135,
        8,
        "TOTAL:",
        align="R"
    )

    pdf.cell(
        45,
        8,
        f"${total:.2f}",
        border=1,
        align="R"
    )

    pdf.ln()

    # --------------------------------------
    # ABONO
    # --------------------------------------

    pdf.cell(
        135,
        8,
        "ABONO:",
        align="R"
    )

    pdf.cell(
        45,
        8,
        f"${valor_abono:.2f}",
        border=1,
        align="R"
    )

    pdf.ln()

    # --------------------------------------
    # SALDO
    # --------------------------------------

    pdf.cell(
        135,
        8,
        "SALDO PENDIENTE:",
        align="R"
    )

    pdf.cell(
        45,
        8,
        f"${saldo:.2f}",
        border=1,
        align="R"
    )

    pdf.ln(20)

    # --------------------------------------
    # MENSAJE
    # --------------------------------------

    pdf.set_font(
        "Arial",
        "I",
        10
    )

    pdf.cell(
        0,
        8,
        "Gracias por su compra.",
        align="C"
    )

    # --------------------------------------
    # GUARDAR PDF
    # --------------------------------------

    pdf.output(nombre_archivo)

    messagebox.showinfo(
        "Nota generada",
        f"Nota de venta generada correctamente.\n\n"
        f"Numero: {numero_nota:06d}\n"
        f"Total: ${total:.2f}\n"
        f"Abono: ${valor_abono:.2f}\n"
        f"Saldo: ${saldo:.2f}\n\n"
        f"Archivo: {nombre_archivo}"
    )

    numero_nota += 1


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="Sistema de Arte Encantada",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=10)


# ==========================================
# CLIENTE
# ==========================================

tk.Label(
    ventana,
    text="Cliente:",
    font=("Arial", 10)
).place(
    x=50,
    y=55
)

nombre_cliente = Entry(
    ventana,
    width=20,
    font=("Arial", 10)
)

nombre_cliente.place(
    x=110,
    y=55
)


# ==========================================
# PRODUCTO
# ==========================================

tk.Label(
    ventana,
    text="Producto:",
    font=("Arial", 10)
).place(
    x=280,
    y=55
)

producto = Entry(
    ventana,
    width=18,
    font=("Arial", 10)
)

producto.place(
    x=345,
    y=55
)


# ==========================================
# PRECIO
# ==========================================

tk.Label(
    ventana,
    text="Precio:",
    font=("Arial", 10)
).place(
    x=510,
    y=55
)

precio = Entry(
    ventana,
    width=10,
    font=("Arial", 10)
)

precio.place(
    x=560,
    y=55
)


# ==========================================
# CANTIDAD
# ==========================================

tk.Label(
    ventana,
    text="Cantidad:",
    font=("Arial", 10)
).place(
    x=660,
    y=55
)

cantida = Entry(
    ventana,
    width=8,
    font=("Arial", 10)
)

cantida.place(
    x=730,
    y=55
)


# ==========================================
# BOTÓN AÑADIR
# ==========================================

btn_anadir = Button(
    ventana,
    text="Añadir",
    command=anadir,
    font=("Arial", 10)
)

btn_anadir.place(
    x=150,
    y=100
)


# ==========================================
# BOTÓN ELIMINAR
# ==========================================

btn_eliminar = Button(
    ventana,
    text="Eliminar",
    command=eliminar,
    font=("Arial", 10)
)

btn_eliminar.place(
    x=300,
    y=100
)


# ==========================================
# BOTÓN BORRAR
# ==========================================

btn_borrar = Button(
    ventana,
    text="Borrar",
    command=borrar,
    font=("Arial", 10)
)

btn_borrar.place(
    x=450,
    y=100
)


# ==========================================
# BOTÓN NOTA
# ==========================================

btn_nota = Button(
    ventana,
    text="Generar Nota de Venta",
    command=generar_nota,
    font=("Arial", 10, "bold")
)

btn_nota.place(
    x=570,
    y=100
)


# ==========================================
# TABLA
# ==========================================

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
    height=12
)


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


tabla.place(
    x=100,
    y=150
)
# ==========================================
# DIRECCIÓN DEL CLIENTE
# ==========================================

tk.Label(
    ventana,
    text="Dirección:",
    font=("Arial", 10)
).place(
    x=50,
    y=85
)

direccion_cliente = Entry(
    ventana,
    width=25,
    font=("Arial", 10)
)

direccion_cliente.place(
    x=110,
    y=85
)


# ==========================================
# TELÉFONO DEL CLIENTE
# ==========================================

tk.Label(
    ventana,
    text="Teléfono:",
    font=("Arial", 10)
).place(
    x=300,
    y=85
)

telefono_cliente = Entry(
    ventana,
    width=18,
    font=("Arial", 10)
)

telefono_cliente.place(
    x=365,
    y=85
)


# ==========================================
# TOTAL GENERAL
# ==========================================

total_label = tk.Label(
    ventana,
    text="Total General: $0.00",
    font=("Arial", 14, "bold")
)

total_label.place(
    x=550,
    y=410
)


# ==========================================
# ABONO
# ==========================================

tk.Label(
    ventana,
    text="Abono:",
    font=("Arial", 11, "bold")
).place(
    x=100,
    y=450
)

abono = Entry(
    ventana,
    width=15,
    font=("Arial", 11)
)

abono.place(
    x=160,
    y=450
)


# ==========================================
# BOTÓN CALCULAR SALDO
# ==========================================

btn_saldo = Button(
    ventana,
    text="Calcular Saldo",
    command=calcular_saldo,
    font=("Arial", 10)
)

btn_saldo.place(
    x=290,
    y=447
)


# ==========================================
# SALDO
# ==========================================

saldo_label = tk.Label(
    ventana,
    text="Saldo: $0.00",
    font=("Arial", 14, "bold")
)

saldo_label.place(
    x=500,
    y=450
)


# ==========================================
# MENSAJE
# ==========================================

mensaje = tk.Label(
    ventana,
    text="Arte Encantada - Productos personalizados",
    font=("Arial", 9)
)

mensaje.place(
    x=100,
    y=525
)


# ==========================================
# EJECUTAR
# ==========================================

ventana.mainloop()

import tkinter as tk
from tkinter import Tk, Label, Button, Entry,Frame, messagebox, mainloop
ventana=tk.Tk()
ventana.title("sistema de arte encantada")
ventana.geometry("900x500")

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
bnt_añadir=Button(ventana, text="Añadir", font=("arial", 10))
bnt_añadir.place(x=150,y=120)
#botoneliminar
btn_eliminar=Button(ventana,text="Eliminar", font=("arial",10))
btn_eliminar.place(x=350, y=120)
#BOTOBORRAR
btn_borrar=Button(ventana,text="Borrar",font=("arial",10))
btn_borrar.place(y=120,x=650)



ventana.mainloop()
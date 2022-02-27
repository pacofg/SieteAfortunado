# Siete afortunadao

# Clases
    # Atributos
    #  Metodos
    # Ciclos 
    # Arreglos

# Interfaces graficas
    # Eventos

import tkinter

from tkinter import *

class SieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
        
    def crear_interfaz(self):
         #--- Crear ventana
        ventana = Tk()
        ventana.minsize(340,450)
        ventana.geometry('340x450')

         #--- Crear boton
        boton = Button(ventana, text="Jugar!", command=self.jugar, font='arial 18 bold')
        boton.pack()

         #---- Definimos la imagen del premio
        foto = PhotoImage(file=r'images/dinero.png')
        self.gano = Label(ventana,image=foto)

         #--- Definimos la posicion en la que apareceran los numeros
        self.campos = [StringVar() for elemento in range(3)]
        posicion = 10
        for campo in self.campos:
            label = Label(ventana, textvariable=campo, background='White', foreground='Black', font='arial 42 bold')
            label.place(x=posicion, y=100,width=100, height=100)
            posicion += 110
        mainloop()

     #--- Funcion del boton
    def jugar(self):
        print("Jugando!")

jugar = SieteAfortunado()
    

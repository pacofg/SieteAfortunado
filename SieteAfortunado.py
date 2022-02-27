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

        mainloop()

jugar = SieteAfortunado()
    

# Siete afortunadao

# Clases
    # Atributos
    #  Metodos
    # Ciclos 
    # Arreglos

# Interfaces graficas
    # Eventos

import tkinter
import random

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
        # print("Jugando!")
        hay_siete = False
         # Tenemos que generar 3 numeros aleatorios
        for i in range(3):
            valor = self.generar_numero()
            self.campos[i].set(valor)
            if(valor == 7) :
                hay_siete = True

         # Si alguno de los numeros generado es un 7 hemos ganado
        if(hay_siete):
             # Se muestra el premio en la ventana
            self.gano.pack(side=BOTTOM) 
        else:
             # Borramos el premio de la ventana
            self.gano.pack_forget()
        
    
     #--- Numero aleatorio entre 0 y 9, ambos inclusive
    def generar_numero(self):
        return random.randint(0,9)

jugar = SieteAfortunado()
    

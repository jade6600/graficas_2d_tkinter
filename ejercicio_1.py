from tkinter import *

#variables globales
BASE = 460
ALTURA = 220

# ventana pricipal
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# Frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white",width=500,height=500)
frame_graficacion.place(x=0,y=0)

#lienzo de graficacion
c =Canvas(frame_graficacion,width=500,height=500)
c.config(bg="white")
c.place(x=0,y=0)


# Dibujar rectangulos
# rectangulo
rectangulo = c.create_rectangle(70,100,305,250, fill="gray", outline="black")

#desplegar ventana pricipal
ventana_principal.mainloop()
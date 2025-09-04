from tkinter import *

#variables globales
BASE = 460
ALTURA = 220

# ventana pricipal
ventana_principal = Tk()
ventana_principal.title("Tren Sistemas")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# Frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white",width=480,height=240)
frame_graficacion.place(x=10,y=10)

# lienzo de graficacion
c = Canvas(frame_graficacion,width=BASE,height=ALTURA)
c.config(bg="white")
c.place(x=10,y=10)

# ---------------------------
# Dibujo del tren
# ---------------------------

# rectangulo
rectangulo = c.create_rectangle(70,100,335,180, fill="gray", outline="black")

# Cabina
cabina = c.create_rectangle(250,50,330,100, fill="gray", outline="black")

# Chimenea
chimenea = c.create_rectangle(120,50,150,100, fill="gray", outline="black")
chimenea_top = c.create_rectangle(110,30,160,50, fill="dimgray", outline="black")

# NOMBRE
texto = c.create_text(200,140, text="Soreth", font=("Arial",20,"bold"), fill="black")

# Carita
ventana = c.create_rectangle(260,60,320,100, fill="white", outline="black")
cara = c.create_oval(265,65,315,95, fill="gold", outline="black")
boca = c.create_oval(285,80,295,90, fill="red")
ojo1 = c.create_oval(275,72,283,80, fill="white")
ojo2 = c.create_oval(297,72,305,80, fill="white")
ceja1 = c.create_line(274,68,282,70, width=2, fill="black")
ceja2 = c.create_line(296,70,306,68, width=2, fill="black")

# Ruedas
rueda1 = c.create_oval(110,170,150,210, fill="dimgray", outline="black")
rueda2 = c.create_oval(170,170,210,210, fill="dimgray", outline="black")
rueda3 = c.create_oval(230,170,270,210, fill="dimgray", outline="black")

# ovalo
ovalo = c.create_oval(70,100,120,180, fill="gray", outline="black")

# Techo de la cabina
techo = c.create_rectangle(240,30,340,50, fill="dimgray", outline="black")

# ---------------------------

# frame de controles (solo para rellenar espacio)
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="lightgray",width=480,height=230)
frame_controles.place(x=10,y=260)

# desplegar ventana principal
ventana_principal.mainloop()
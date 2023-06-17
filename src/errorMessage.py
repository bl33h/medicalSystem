from tkinter import *
import customtkinter as ct

class ErrorMessage:
    def __init__(self, parent, mensaje):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Advertencia")

        etiError = ct.CTkLabel(self.win, text= mensaje, font=("Arial", 20, "bold"))
        
        buttonSalir = ct.CTkButton(self.win, text="Salir", command= lambda: self.close())
        
        etiError.pack()
        buttonSalir.pack()
    
    def close(self):
        self.win.destroy()
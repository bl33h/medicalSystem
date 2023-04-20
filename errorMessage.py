from tkinter import *
import customtkinter as ct

class ErrorMessage:
    def __init__(self, parent, mensaje):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Error")

        
        etiError = ct.CTkLabel(self.win, text="ERROR: " + mensaje, font=("Arial", 20, "bold"), text_color="red")
        
        buttonSalir = ct.CTkButton(self.win, text="Salir", command= lambda: self.close())
        
        etiError.pack()
        buttonSalir.pack()
    
    def close(self):
        self.win.destroy()
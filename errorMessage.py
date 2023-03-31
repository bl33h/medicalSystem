from tkinter import *

class ErrorMessage:
    def __init__(self, parent, mensaje):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Signup")
        
        etiError = Label(self.win, text=mensaje)
        buttonSalir = Button(self.win, text="Salir", command= lambda: self.close())
        
        etiError.pack()
        buttonSalir.pack()
    
    def close(self):
        self.win.destroy()
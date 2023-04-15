from tkinter import *
import connection as con

class Bodega:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        
        
        etiIdPaciente = Label(self.win, text="Id del paciente")
        
        etiIdPaciente.pack()
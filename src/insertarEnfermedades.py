from tkinter import *
import connection as con
import customtkinter as ct
from errorMessage import ErrorMessage

class insertarEnfermedades:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingresar enfermedad nueva")
        etiTitle = ct.CTkLabel(self.win, text="Ingresar enfermedad nueva", font=("Arial", 20, "bold"))

        # id de transferencia es serial. 
        
        etiNombreEnfermedad = ct.CTkLabel(self.win, text="Nombre de la enfermedad")
        inputNombreEnfermedad = ct.CTkEntry(self.win, width=200)

        etiSintomas = ct.CTkLabel(self.win, text="Sintomas")
        inputSintomas = ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.insert_enfermedades(inputNombreEnfermedad, inputSintomas ), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiNombreEnfermedad.pack(pady=5)
        inputNombreEnfermedad.pack(pady=5)
        etiSintomas.pack(pady=5)
        inputSintomas.pack(pady=5)

        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def insert_enfermedades(self, inputNombreEnfermedad, inputSintomas):
        query = r"""insert into enfermedades (nombre_enf, sintomas) values('""" + inputNombreEnfermedad.get() + r"""', '""" + inputSintomas.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
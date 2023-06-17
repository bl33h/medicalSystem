from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class AsignarMedico:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Asignar Medico")
        etiTitle = ct.CTkLabel(self.win, text="Asignar medico", font=("Arial", 20, "bold"))
        
        etiNum_col = ct.CTkLabel(self.win, text="Numero colegiado")
        inputNum_col = ct.CTkEntry(self.win, width=200)
        
        etiEstablecimiento = ct.CTkLabel(self.win, text="Id del establecimiento")
        inputEstablecimiento = ct.CTkEntry(self.win, width=200)

        etiFecha = ct.CTkLabel(self.win, text="Fecha de contratacion")
        inputFecha = ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.asigna_medico(inputNum_col, inputEstablecimiento, inputFecha), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiNum_col.pack()
        inputNum_col.pack(pady=5)
        etiEstablecimiento.pack()
        inputEstablecimiento.pack(pady=5)
        etiFecha.pack()
        inputFecha.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def asigna_medico(self,inputNum_col, inputEstablecimiento, inputFecha):
        query = r"""insert into medico_trabaja_en_establecimiento values('""" + inputNum_col.get() + r"""', '""" + inputEstablecimiento.get() + r"""', '""" + inputFecha.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
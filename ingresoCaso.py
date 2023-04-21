from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class IngresoCaso:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingreso caso")
        etiTitle = ct.CTkLabel(self.win, text="Ingreso caso", font=("Arial", 20, "bold"))
        
        etiDPI = ct.CTkLabel(self.win, text="DPI")
        inputDPI = ct.CTkEntry(self.win, width=200)
        
        etiNoColegiado = ct.CTkLabel(self.win, text="No. Colegiado")
        inputNoColegiado = ct.CTkEntry(self.win, width=200)
        
        etiIdCentro = ct.CTkLabel(self.win, text="Id centro de salud")
        inputIdCentro = ct.CTkEntry(self.win, width=200)
        
        etiArea = ct.CTkLabel(self.win, text="Area de salud")
        inputArea = ct.CTkEntry(self.win, width=200)
        
        etiFechaIngreso = ct.CTkLabel(self.win, text="Fecha de ingreso")
        inputFechaIngreso = ct.CTkEntry(self.win, width=200)
        
        etiDiagnostico = ct.CTkLabel(self.win, text="Diagnostico")
        inputDiagnostico = ct.CTkEntry(self.win, width=200)
        
        etiObservaciones = ct.CTkLabel(self.win, text="Observaciones")
        inputObservaciones = ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.inputPaciente(inputDPI, inputNoColegiado, inputIdCentro, inputArea, inputFechaIngreso, inputDiagnostico, inputObservaciones), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiDPI.pack()
        inputDPI.pack(pady=5)
        etiNoColegiado.pack()
        inputNoColegiado.pack(pady=5)
        etiIdCentro.pack()
        inputIdCentro.pack(pady=5)
        etiArea.pack()
        inputArea.pack(pady=5)
        etiFechaIngreso.pack()
        inputFechaIngreso.pack(pady=5)
        etiDiagnostico.pack()
        inputDiagnostico.pack(pady=5)
        etiObservaciones.pack()
        inputObservaciones.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def inputPaciente(self, inputDPI, inputNoColegiado, inputIdCentro, inputArea, inputFechaIngreso, inputDiagnostico, inputObservaciones):
        query = f"select * from crear_caso('{inputDPI.get()}', '{inputNoColegiado.get()}', '{inputIdCentro.get()}', '{inputArea.get()}', '{inputFechaIngreso.get()}', '{inputDiagnostico.get()}', '{inputObservaciones.get()}')"
        results = con.connect(query)
        if (results is None):
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
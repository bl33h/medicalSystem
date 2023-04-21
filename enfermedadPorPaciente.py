from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class IngresoEnfermedades:
    def __init__(self, parent, idCaso):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingreso Enfermedades")
        etiTitle = ct.CTkLabel(self.win, text="Ingreso Enfermedades", font=("Arial", 20, "bold"))
        
        etiIdCaso = ct.CTkLabel(self.win, text="Id Caso")
        inputIdCaso = ct.CTkEntry(self.win, width=200)
        inputIdCaso.insert(0, idCaso)
        
        etiIdEnfermedad = ct.CTkLabel(self.win, text="Id enfermedad")
        inputIdEnfermedad = ct.CTkEntry(self.win, width=200)
        
        etiEvolucion = ct.CTkLabel(self.win, text="Evolucion")
        inputEvolucion = StringVar()
        radiobutton_1 = ct.CTkRadioButton(self.win, text="Sano", variable= inputEvolucion, value="sano")
        radiobutton_2 = ct.CTkRadioButton(self.win, text="Controlado", variable= inputEvolucion, value="controlado")
        radiobutton_3 = ct.CTkRadioButton(self.win, text="Muerto", variable= inputEvolucion, value="muerto")
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.inputPaciente(inputIdCaso, inputIdEnfermedad, inputEvolucion), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiIdCaso.pack()
        inputIdCaso.pack(pady=5)
        etiIdEnfermedad.pack()
        inputIdEnfermedad.pack(pady=5)
        etiEvolucion.pack()
        radiobutton_1.pack(pady=5)
        radiobutton_2.pack(pady=5)
        radiobutton_3.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def inputPaciente(self, inputIdCaso, inputIdEnfermedad, inputEvolucion):
        query = f"insert into caso_enf values({inputIdCaso.get()}, {inputIdEnfermedad.get()}, '{inputEvolucion.get()}')"
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
            
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
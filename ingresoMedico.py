from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class IngresoMedico:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingreso Medico")
        etiTitle = ct.CTkLabel(self.win, text="Ingreso medico", font=("Arial", 20, "bold"))
        
        etiNum_col = ct.CTkLabel(self.win, text="Numero colegiado")
        inputNum_col = ct.CTkEntry(self.win, width=200)
        
        etiNombre = ct.CTkLabel(self.win, text="Nombre")
        inputNombre = ct.CTkEntry(self.win, width=200)
        
        etiApellido = ct.CTkLabel(self.win, text="Apellido")
        inputApellido = ct.CTkEntry(self.win, width=200)
        
        etiEspecialidad = ct.CTkLabel(self.win, text="Especialidad")
        inputEspecialidad = ct.CTkEntry(self.win, width=200)
        
        etiTelefono = ct.CTkLabel(self.win, text="Telefono")
        inputTelefono = ct.CTkEntry(self.win, width=200)
        
        etiDireccion = ct.CTkLabel(self.win, text="Direccion")
        inputDireccion = ct.CTkEntry(self.win, width=200)
        
        etiEmail = ct.CTkLabel(self.win, text="Email")
        inputEmail = ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Signup", command= lambda: self.inputMedico(inputNum_col, inputNombre, inputApellido, inputEspecialidad, inputTelefono, inputDireccion, inputEmail), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiNum_col.pack()
        inputNum_col.pack(pady=5)
        etiNombre.pack()
        inputNombre.pack(pady=5)
        etiApellido.pack()
        inputApellido.pack(pady=5)
        etiEspecialidad.pack()
        inputEspecialidad.pack(pady=5)
        etiTelefono.pack()
        inputTelefono.pack(pady=5)
        etiDireccion.pack()
        inputDireccion.pack(pady=5)
        etiEmail.pack()
        inputEmail.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def inputMedico(self,inputNum_col, inputNombre, inputApellido, inputEspecialidad, inputTelefono, inputDireccion, inputEmail):
        query = r"""insert into medico values('""" + inputNum_col.get() + r"""', '""" + inputNombre.get() + r"""', '""" + inputApellido.get() + r"""', '""" + inputEspecialidad.get() + r"""', '""" + inputTelefono.get() + r"""', '""" + inputDireccion.get() + r"""', '""" + inputEmail.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
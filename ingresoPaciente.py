from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class IngresoPaciente:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingreso paciente")
        etiTitle = ct.CTkLabel(self.win, text="Ingreso paciente", font=("Arial", 20, "bold"))
        
        etiDPI = ct.CTkLabel(self.win, text="DPI")
        inputDPI = ct.CTkEntry(self.win, width=200)
        
        etiNombre = ct.CTkLabel(self.win, text="Nombre")
        inputNombre = ct.CTkEntry(self.win, width=200)
        
        etiApellido = ct.CTkLabel(self.win, text="Apellido")
        inputApellido = ct.CTkEntry(self.win, width=200)
        
        etiBDay = ct.CTkLabel(self.win, text="Fecha de nacimiento")
        inputBday = ct.CTkEntry(self.win, width=200)

        inputSexo = IntVar()
        etiSexo = ct.CTkLabel(self.win, text="Sexo")
        radiobutton_1 = ct.CTkRadioButton(self.win, text="Hombre", variable= inputSexo, value=0)
        radiobutton_2 = ct.CTkRadioButton(self.win, text="Mujer", variable= inputSexo, value=1)
        
        etiIMC = ct.CTkLabel(self.win, text="IMC")
        inputIMC = ct.CTkEntry(self.win, width=200)
        
        etiAltura = ct.CTkLabel(self.win, text="Altura")
        inputAltura = ct.CTkEntry(self.win, width=200)
        
        etiPeso = ct.CTkLabel(self.win, text="Peso")
        inputPeso = ct.CTkEntry(self.win, width=200)

        etiTelefono = ct.CTkLabel(self.win, text="Telefono")
        inputTelefono = ct.CTkEntry(self.win, width=200)

        etiDireccion = ct.CTkLabel(self.win, text="Dirección")
        inputDireccion = ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.inputPaciente(inputDPI, inputNombre, inputApellido, inputBday, inputSexo, inputIMC, inputAltura, inputPeso, inputTelefono, inputDireccion), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiDPI.pack()
        inputDPI.pack(pady=5)
        etiNombre.pack()
        inputNombre.pack(pady=5)
        etiApellido.pack()
        inputApellido.pack(pady=5)
        etiBDay.pack()
        inputBday.pack(pady=5)
        etiSexo.pack()
        radiobutton_1.pack(pady=2)
        radiobutton_2.pack(pady=2)
        etiIMC.pack()
        inputIMC.pack(pady=5)
        etiAltura.pack()
        inputAltura.pack(pady=5)
        etiPeso.pack()
        inputPeso.pack(pady=5)
        etiTelefono.pack()
        inputTelefono.pack(pady=5)
        etiDireccion.pack()
        inputDireccion.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def inputPaciente(self, inputDPI, inputNombre, inputApellido, inputBday, inputSexo, inputIMC, inputAltura, inputPeso, inputTelefono, inputDireccion):
        query = r"""insert into paciente values('""" + inputDPI.get() + r"""', '""" + inputNombre.get() + r"""', '""" + inputApellido.get() + r"""', '""" + inputBday.get() + r"""', '""" + str(inputSexo.get()) + r"""', '""" + inputIMC.get() + r"""', '""" + inputAltura.get() + r"""', '""" + str(inputPeso.get()) + r"""', '""" + inputTelefono.get() + r"""', '""" + inputDireccion.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
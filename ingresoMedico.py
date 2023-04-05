from tkinter import *
from errorMessage import ErrorMessage
import connection as con

class IngresoMedico:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Ingreso Medico")
        
        etiNum_col = Label(self.win, text="Numero colegiado")
        inputNum_col = Entry(self.win)
        
        etiNombre = Label(self.win, text="Nombre")
        inputNombre = Entry(self.win)
        
        etiApellido = Label(self.win, text="Apellido")
        inputApellido = Entry(self.win)
        
        etiEspecialidad = Label(self.win, text="Especialidad")
        inputEspecialidad = Entry(self.win)
        
        etiTelefono = Label(self.win, text="Telefono")
        inputTelefono = Entry(self.win)
        
        etiDireccion = Label(self.win, text="Direccion")
        inputDireccion = Entry(self.win)
        
        etiEmail = Label(self.win, text="Email")
        inputEmail = Entry(self.win)
        
        buttonSignup = Button(self.win, text="Signup", command= lambda: self.inputMedico(inputNum_col, inputNombre, inputApellido, inputEspecialidad, inputTelefono, inputDireccion, inputEmail))
        buttonClose = Button(self.win, text="Close", command= lambda: self.close())
        
        etiNum_col.pack()
        inputNum_col.pack()
        etiNombre.pack()
        inputNombre.pack()
        etiApellido.pack()
        inputApellido.pack()
        etiEspecialidad.pack()
        inputEspecialidad.pack()
        etiTelefono.pack()
        inputTelefono.pack()
        etiDireccion.pack()
        inputDireccion.pack()
        etiEmail.pack()
        inputEmail.pack()
        buttonSignup.pack()
        buttonClose.pack()

        self.win.geometry("600x400")
        
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
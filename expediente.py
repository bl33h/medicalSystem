from tkinter import *

class ExpedienteWindow:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        
        etiNombrePaciente = Label(self.win, text="Nombre del paciente")
        etiCodigopaciente = Label(self.win, text="Codigo del paciente")
        
        inputNombrePaciente = Entry(self.win)
        inputCodigoPaciente = Entry(self.win)
        
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarPaciente(inputNombrePaciente, inputCodigoPaciente))
        
        etiNombrePaciente.pack()
        inputNombrePaciente.pack()
        etiCodigopaciente.pack()
        inputCodigoPaciente.pack()
        buttonBuscar.pack()
        
        
        self.win.geometry("300x200")
        
    def buscarPaciente(self,inputNombrePaciente, inputCodigoPaciente):
        etiNombreResultado = Label(self.win, text=inputNombrePaciente.get())
        etiCodigoResultado = Label(self.win, text=inputCodigoPaciente.get())
        
        etiNombreResultado.pack()
        etiCodigoResultado.pack()
        
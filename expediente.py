from tkinter import *
import connection as con
from resultadosExpediente import ResultadoExpediente

class ExpedienteWindow:
    def __init__(self, parent, administrador):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        
        etiIdPaciente = Label(self.win, text="Id del paciente")
        
        inputIdPaciente = Entry(self.win)
        
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente))

        buttonEditarUsuario = Button(self.win, text="Editar Usuario", command= lambda: self.editarUsuario(inputIdPaciente))
            
        etiIdPaciente.pack()
        inputIdPaciente.pack()
        buttonBuscar.pack()
        if (administrador == True):
            buttonEditarUsuario.pack()
        
        self.win.geometry("300x200")
        
    def buscarPaciente(self, inputIdPaciente):
        query = f"SELECT * FROM paciente p WHERE p.dpi = '{inputIdPaciente.get()}'"
        results = con.connect(query)
        column_names = con.column_names(query)
        ResultadoExpediente(self.win, results, column_names)
    
        
        
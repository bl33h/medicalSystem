from tkinter import *
import connection as con
from resultadosExpediente import ResultadoExpediente
from bodega import Bodega
from editarInfoUsuario import EditarInfoUsuario

class ExpedienteWindow:
    def __init__(self, parent, administrador, encargado_bodega):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        
        
        etiIdPaciente = Label(self.win, text="Id del paciente")
        
        inputIdPaciente = Entry(self.win)
        
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente))

        buttonEditarUsuario = Button(self.win, text="Editar Usuario", command= lambda: EditarInfoUsuario(self.win))
        buttonEncargadoBodega = Button(self.win, text="Encargado Bodega", command= lambda: Bodega())
        
        if (encargado_bodega == True):
            buttonEncargadoBodega.pack()
        elif (encargado_bodega == False):   
            etiIdPaciente.pack()
            inputIdPaciente.pack()
            buttonBuscar.pack()
        if (administrador == True):
            buttonEditarUsuario.pack()
            buttonEncargadoBodega.pack()
        
        self.win.geometry("400x300")
        
    def buscarPaciente(self, inputIdPaciente):
        query = f"SELECT * FROM paciente p WHERE p.dpi = '{inputIdPaciente.get()}'"
        results = con.connect(query)
        column_names = con.column_names(query)
        ResultadoExpediente(self.win, results, column_names)
    
        
        
from tkinter import *
import connection as con
from resultadosExpediente import ResultadoExpediente
from bodega import Bodega
from editarInfoUsuario import EditarInfoUsuario
from errorMessage import ErrorMessage
from InfoPaciente import infoPaciente
from Reporteria import Reporteria
from ingresoMedico import IngresoMedico
from ingresoPaciente import IngresoPaciente
from ingresoCaso import IngresoCaso
from enfermedadPorPaciente import IngresoEnfermedades
import customtkinter as ct
import transferencias as t
import insertarEnfermedades as i
from asignacionInsumosCaso import asignarInsumos

class ExpedienteWindow:
    def __init__(self, parent, administrador, encargado_bodega, inputUsername):
        
        con.funUsuario(inputUsername.get())
        
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Opciones")
        etiTitle = ct.CTkLabel(self.win, text="Opciones", font=("Arial", 20, "bold"))
        
        

        buttonInfoPaciente = ct.CTkButton(self.win, text="Información de paciente", command= lambda: infoPaciente(self.win), width=200)

        buttonReporteria = ct.CTkButton(self.win, text="Reporteria general", command= lambda: Reporteria(self.win), width=200)

        buttonEditarUsuario = ct.CTkButton(self.win, text="Editar Usuario", command= lambda: EditarInfoUsuario(self.win), width=200)
        buttonEncargadoBodega = ct.CTkButton(self.win, text="Encargado Bodega", command= lambda: Bodega(self.win), width=200)
        buttonIngresoMedico = ct.CTkButton(self.win, text="Ingreso Medico", command= lambda: IngresoMedico(self.win), width=200)
        buttonIngresoPaciente = ct.CTkButton(self.win, text="Ingreso Paciente", command= lambda: IngresoPaciente(self.win), width=200)
        buttonTransferirMedico = ct.CTkButton(self.win, text="Transferir Medico", command= lambda: t.transferirMedico(self.win), width=200)
        buttonIngresoEnfermedad = ct.CTkButton(self.win, text="Ingreso Enfermedad por Paciente", command= lambda: IngresoEnfermedades(self.win, idCaso = 0), width=200)
        buttonAsignarInsumos = ct.CTkButton(self.win, text="Asignacion de insumos a caso", command= lambda: asignarInsumos(self.win, idCaso = 0), width=200)

        buttonIngresoCaso = ct.CTkButton(self.win, text="Ingreso Caso", command= lambda: IngresoCaso(self.win), width=200)
        
        
        etiTitle.pack(pady=5)
        if (encargado_bodega == True):
            buttonEncargadoBodega.pack(pady=5)
        elif (encargado_bodega == False):   
            buttonInfoPaciente.pack(pady=5)
            buttonIngresoPaciente.pack(pady=5)
            buttonIngresoCaso.pack(pady=5)
            buttonIngresoEnfermedad.pack(pady=5)
            buttonAsignarInsumos.pack(pady=5)
        if (administrador == True):
            buttonEditarUsuario.pack(pady=5)
            buttonEncargadoBodega.pack(pady=5)
            buttonInfoPaciente.pack(pady=5)
            buttonReporteria.pack(pady=5)
            buttonIngresoMedico.pack(pady=5)
            buttonIngresoPaciente.pack(pady=5)
            buttonTransferirMedico.pack(pady=5)
            buttonIngresoCaso.pack(pady=5)
            buttonIngresoEnfermedad.pack(pady=5)
            buttonAsignarInsumos.pack(pady=5)
        
        self.win.geometry("500x500")
        
    def buscarPaciente(self, inputIdPaciente):
        query = f"select * from informacion_paciente('{inputIdPaciente.get()}')"
        results = con.connect(query)
        column_names = con.column_names(query)
        if results is not None:
            ResultadoExpediente(self.win, results, column_names)
        else:
            mensaje = "No se ha encontrado el paciente"
            ErrorMessage(self.win, mensaje)
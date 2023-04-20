from tkinter import *
import connection as con
import errorMessage as em
import customtkinter as ct

class Reporteria:
    def __init__(self, parent):
        self.widget_list_dataPersonal = []
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Reporteria")
        etiTitle = ct.CTkLabel(self.win, text="Reporteria", font=("Arial", 20, "bold"))
        self.widget_list_dataPersonal = []

        buttonEnfermedadesMortales = ct.CTkButton(self.win, text="Enfermedades más mortales", command= lambda: self.enfermedadesMortales(), width=300)
        buttonMedicosMasPacientes = ct.CTkButton(self.win, text="Médicos que más pacientes han atendido", command= lambda: self.medicosMasPacientes(), width=300)
        buttonPacientesMasAsistencias = ct.CTkButton(self.win, text="Pacientes con más asistencias", command= lambda: self.pacientesMasAsistencias(), width=300)
        buttonMedicinasPuntoTerminarse = ct.CTkButton(self.win, text="Insumos que están a punto de terminarse", command= lambda: self.medicinasPuntoTerminarse(), width=300)
        buttonUnidadesSaludMasPacientes = ct.CTkButton(self.win, text="Unidades de salud que más pacientes atienden", command= lambda: self.unidadesSaludMasPacientes(), width=300)

        etiTitle.pack()
        buttonEnfermedadesMortales.pack(pady=5)
        buttonMedicosMasPacientes.pack(pady=5)
        buttonPacientesMasAsistencias.pack(pady=5)
        buttonMedicinasPuntoTerminarse.pack(pady=5)
        buttonUnidadesSaludMasPacientes.pack(pady=5)
 
        
        self.win.geometry("600x300")

    def enfermedadesMortales(self):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query1 = "select * from get_top_enfermedades()"
        results = con.connect(query1)
        column_names1 = con.column_names(query1)
        if results is not None:
             listColumnas1 = list(column_names1)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas1[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicosMasPacientes(self):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query2 = "select * from get_top_medicos()"
        results = con.connect(query2)
        column_names2 = con.column_names(query2)
        if results is not None:
             listColumnas2 = list(column_names2)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas2[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def pacientesMasAsistencias(self):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query3 = "select * from get_pacientes_top_asistencias()"
        results = con.connect(query3)
        column_names3 = con.column_names(query3)
        if results is not None:
             listColumnas3 = list(column_names3)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas3[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicinasPuntoTerminarse(self):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        var_wait = IntVar()
        #crear un entry para que se ingrese el id del establecimiento
        etiEstablecimiento = ct.CTkLabel(self.win, text="Ingrese el id del establecimiento:", font=('Arial', 12, 'bold'))
        inputEstablecimiento = ct.CTkEntry(self.win)
        btnEstablecimiento = ct.CTkButton(self.win, text="Aceptar", command= lambda: var_wait.set(1))
        etiEstablecimiento.pack()
        self.widget_list_dataPersonal.append(etiEstablecimiento)
        inputEstablecimiento.pack()
        self.widget_list_dataPersonal.append(inputEstablecimiento)
        btnEstablecimiento.pack()
        self.widget_list_dataPersonal.append(btnEstablecimiento)
        self.win.wait_variable(var_wait)
        query4 = f"select * from reporte_insumos_por_establecimiento('{inputEstablecimiento.get()}')"
        results = con.connect(query4)
        column_names4 = con.column_names(query4)
        if results is not None:
             listColumnas4 = list(column_names4)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas4[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack() 
                self.widget_list_dataPersonal.append(etiResultado)
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def unidadesSaludMasPacientes(self):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query5 = "select * from get_top_establecimientos()"
        results = con.connect(query5)
        column_names5 = con.column_names(query5)
        if results is not None:
             listColumnas5 = list(column_names5)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas5[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)
        

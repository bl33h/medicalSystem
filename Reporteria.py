from tkinter import *
import connection as con
import errorMessage as em

class Reporteria:
    def __init__(self, parent):
        self.widget_list_dataPersonal = []
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Reporteria")
        etiTitle = Label(self.win, text="Reporteria", font=("Arial", 20, "bold"))
        
        # 5 botones, uno para cada reporte: enfermedades mas mortales, médicos que más pacientes han atendido, 
        # pacientes con más asistencias, medicinas o suministros que están a punto de terminarse, unidades de salud que más
        # pacientes atienden

        buttonEnfermedadesMortales = Button(self.win, text="Enfermedades más mortales", command= lambda: self.enfermedadesMortales(), width=35)
        buttonMedicosMasPacientes = Button(self.win, text="Médicos que más pacientes han atendido", command= lambda: self.medicosMasPacientes(), width=35)
        buttonPacientesMasAsistencias = Button(self.win, text="Pacientes con más asistencias", command= lambda: self.pacientesMasAsistencias(), width=35)
        buttonMedicinasPuntoTerminarse = Button(self.win, text="Insumos que están a punto de terminarse", command= lambda: self.medicinasPuntoTerminarse(), width=35)
        buttonUnidadesSaludMasPacientes = Button(self.win, text="Unidades de salud que más pacientes atienden", command= lambda: self.unidadesSaludMasPacientes(), width=35)

        etiTitle.pack()
        buttonEnfermedadesMortales.pack(pady=5)
        buttonMedicosMasPacientes.pack(pady=5)
        buttonPacientesMasAsistencias.pack(pady=5)
        buttonMedicinasPuntoTerminarse.pack(pady=5)
        buttonUnidadesSaludMasPacientes.pack(pady=5)
 
        
        self.win.geometry("400x300")

    def enfermedadesMortales(self):
        query1 = "select * from get_top_enfermedades()"
        results = con.connect(query1)
        column_names1 = con.column_names(query1)
        if results is not None:
             listColumnas1 = list(column_names1)
             for i in range(len(results)):
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas1[j]}: {results[i][j]} "
                etiResultado = Label(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicosMasPacientes(self):
        query2 = "select * from get_top_medicos()"
        results = con.connect(query2)
        column_names2 = con.column_names(query2)
        if results is not None:
             listColumnas2 = list(column_names2)
             for i in range(len(results)):
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas2[j]}: {results[i][j]} "
                etiResultado = Label(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def pacientesMasAsistencias(self):
        query3 = "select * from get_pacientes_top_asistencias()"
        results = con.connect(query3)
        column_names3 = con.column_names(query3)
        if results is not None:
             listColumnas3 = list(column_names3)
             for i in range(len(results)):
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas3[j]}: {results[i][j]} "
                etiResultado = Label(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicinasPuntoTerminarse(self):
        var_wait = IntVar()
        #crear un entry para que se ingrese el id del establecimiento
        etiEstablecimiento = Label(self.win, text="Ingrese el id del establecimiento:", font='Helvetica 10 bold')
        inputEstablecimiento = Entry(self.win)
        btnEstablecimiento = Button(self.win, text="Aceptar", command= lambda: var_wait.set(1))
        etiEstablecimiento.pack()
        inputEstablecimiento.pack()
        btnEstablecimiento.pack()
        self.win.wait_variable(var_wait)
        query4 = f"select * from reporte_insumos_por_establecimiento('{inputEstablecimiento.get()}')"
        results = con.connect(query4)
        column_names4 = con.column_names(query4)
        if results is not None:
             listColumnas4 = list(column_names4)
             for i in range(len(results)):
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas4[j]}: {results[i][j]} "
                etiResultado = Label(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def unidadesSaludMasPacientes(self):
        query5 = "select * from get_top_establecimientos()"
        results = con.connect(query5)
        column_names5 = con.column_names(query5)
        if results is not None:
             listColumnas5 = list(column_names5)
             for i in range(len(results)):
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas5[j]}: {results[i][j]} "
                etiResultado = Label(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)
        

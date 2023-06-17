from tkinter import *
import connection as con
import errorMessage as em
import customtkinter as ct

class Reporteria:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Reporteria")
        
        main_frame = ct.CTkFrame(self.win)
        main_frame.pack(fill=BOTH, expand=1)
        
        my_canvas = ct.CTkCanvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        
        
        second_frame = ct.CTkFrame(my_canvas)
        
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        
        etiTitle = ct.CTkLabel(second_frame, text="Reporteria", font=("Arial", 20, "bold"))

        self.widget_list_dataPersonal = []

        buttonEnfermedadesMortales = ct.CTkButton(second_frame, text="Enfermedades más mortales", command= lambda: self.enfermedadesMortales(second_frame), width=300)
        buttonMedicosMasPacientes = ct.CTkButton(second_frame, text="Médicos que más pacientes han atendido", command= lambda: self.medicosMasPacientes(second_frame), width=300)
        buttonPacientesMasAsistencias = ct.CTkButton(second_frame, text="Pacientes con más asistencias", command= lambda: self.pacientesMasAsistencias(second_frame), width=300)
        buttonMedicinasPuntoTerminarse = ct.CTkButton(second_frame, text="Insumos que están a punto de terminarse", command= lambda: self.medicinasPuntoTerminarse(second_frame), width=300)
        buttonUnidadesSaludMasPacientes = ct.CTkButton(second_frame, text="Unidades de salud que más pacientes atienden", command= lambda: self.unidadesSaludMasPacientes(second_frame), width=300)

        etiTitle.pack(pady=5)
        buttonEnfermedadesMortales.pack(pady=5)
        buttonMedicosMasPacientes.pack(pady=5)
        buttonPacientesMasAsistencias.pack(pady=5)
        buttonMedicinasPuntoTerminarse.pack(pady=5)
        buttonUnidadesSaludMasPacientes.pack(pady=5)
 
        
        self.win.geometry("600x300")

    def enfermedadesMortales(self, second_frame):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query1 = "select * from get_top_enfermedades()"
        results = con.connect(query1)
        column_names1 = con.column_names(query1)
        if results is not None:
             listColumnas1 = list(column_names1)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas1[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicosMasPacientes(self, second_frame):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query2 = "select * from get_top_medicos()"
        results = con.connect(query2)
        column_names2 = con.column_names(query2)
        if results is not None:
             listColumnas2 = list(column_names2)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas2[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def pacientesMasAsistencias(self, second_frame):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query3 = "select * from get_pacientes_top_asistencias()"
        results = con.connect(query3)
        column_names3 = con.column_names(query3)
        if results is not None:
             listColumnas3 = list(column_names3)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas3[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def medicinasPuntoTerminarse(self, second_frame):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        var_wait = IntVar()
        #crear un entry para que se ingrese el id del establecimiento
        etiEstablecimiento = ct.CTkLabel(second_frame, text="Ingrese el id del establecimiento:", font=('Arial', 12, 'bold'))
        inputEstablecimiento = ct.CTkEntry(second_frame)
        btnEstablecimiento = ct.CTkButton(second_frame, text="Aceptar", command= lambda: var_wait.set(1))
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
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas4[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack() 
                self.widget_list_dataPersonal.append(etiResultado)
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)

    def unidadesSaludMasPacientes(self, second_frame):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query5 = "select * from get_top_establecimientos()"
        results = con.connect(query5)
        column_names5 = con.column_names(query5)
        if results is not None:
             listColumnas5 = list(column_names5)
             for i in range(len(results)):
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack()
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas5[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack()
                self.widget_list_dataPersonal.append(etiResultado) 
        else:
            mensaje = "No se han encontrado resultados"
            em.ErrorMessage(self.win, mensaje)
        

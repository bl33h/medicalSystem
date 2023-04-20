from tkinter import *
import connection as con
import errorMessage as em
import customtkinter as ct

class infoPaciente:
    def __init__(self, parent):
        self.widget_list_dataPersonal = []
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Información de paciente")
        etiTitle = ct.CTkLabel(self.win, text="Información de paciente", font=("Arial", 20, "bold"))
        
        etiIdPaciente = ct.CTkLabel(self.win, text="Id del paciente")
        
        inputIdPaciente = ct.CTkEntry(self.win, width=200)
        
        buttonBuscar = ct.CTkButton(self.win, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente))
        
        etiTitle.pack(pady=5)
        etiIdPaciente.pack(pady=5)
        inputIdPaciente.pack(pady=5)
        buttonBuscar.pack(pady=5)
        
        self.win.geometry("600x600")
        
    def buscarPaciente(self, inputIdPaciente):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        query1 = f"select * from get_info_paciente('{inputIdPaciente.get()}')"
        results1 = con.connect(query1)
        column_names1 = con.column_names(query1)
        query2 = f"select * from get_sickness_history('{inputIdPaciente.get()}')"
        results2 = con.connect(query2)
        column_names2 = con.column_names(query2)
        if results1 is not None:
            listColumnas1 = list(column_names1)
            for i in range(len(results1)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado Informacion de paciente {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack(pady=5)
                texto = ""
                for j in range(len(results1[i])):
                    if listColumnas1[j] == "sexo":
                        if results1[i][j] == 0:
                            texto = texto + f"{listColumnas1[j]}: Hombre "
                            continue
                        else:
                            texto = texto + f"{listColumnas1[j]}: Mujer "
                            continue
                    #Agregar un salto de linea en la posicion 5
                    if j == 6:
                        texto = texto + "\n"  
                        continue 
                    texto = texto + f"{listColumnas1[j]}: {results1[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack(pady=5)
        else:
            mensaje = "No se ha encontrado la información del paciente"
            em.ErrorMessage(self.win, mensaje)
        if results2 is not None:
            listColumnas2 = list(column_names2)
            for i in range(len(results2)):
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado historial de enfermedades {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack(pady=5)
                texto = ""
                for j in range(len(results2[i])):
                    texto = texto + f"{listColumnas2[j]}: {results2[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack(pady=5)
        else:
            mensaje = "No se ha encontrado el historial del paciente"
            em.ErrorMessage(self.win, mensaje)

            ## 0 hombre
            ## 1 mujer

        
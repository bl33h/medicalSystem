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
        
        etiTitle = ct.CTkLabel(second_frame, text="Información de paciente", font=("Arial", 20, "bold"))
        
        etiIdPaciente = ct.CTkLabel(second_frame, text="Id del paciente")
        
        inputIdPaciente = ct.CTkEntry(second_frame, width=200)
        
        buttonBuscar = ct.CTkButton(second_frame, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente, second_frame))
        
        etiTitle.pack(pady=5)
        etiIdPaciente.pack(pady=5)
        inputIdPaciente.pack(pady=5)
        buttonBuscar.pack(pady=5)
        
        self.win.geometry("600x600")
        
    def buscarPaciente(self, inputIdPaciente, second_frame):
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
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado Informacion de paciente {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack(pady=5)
                self.widget_list_dataPersonal.append(etiNoResultado)
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
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack(pady=5)
                self.widget_list_dataPersonal.append(etiResultado)
        else:
            mensaje = "No se ha encontrado la información del paciente"
            em.ErrorMessage(second_frame, mensaje)
        if results2 is not None:
            listColumnas2 = list(column_names2)
            for i in range(len(results2)):
                etiNoResultado = ct.CTkLabel(second_frame, text=f"Resultado historial de enfermedades {i+1}:", text_color="#1e90ff", font=('Arial', 12, 'bold'))
                etiNoResultado.pack(pady=5)
                self.widget_list_dataPersonal.append(etiNoResultado)
                texto = ""
                for j in range(len(results2[i])):
                    texto = texto + f"{listColumnas2[j]}: {results2[i][j]} "
                etiResultado = ct.CTkLabel(second_frame, text=texto)
                etiResultado.pack(pady=5)
                self.widget_list_dataPersonal.append(etiResultado)
        else:
            mensaje = "No se ha encontrado el historial del paciente"
            em.ErrorMessage(self.win, mensaje)

            ## 0 hombre
            ## 1 mujer

        
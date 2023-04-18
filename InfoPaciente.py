from tkinter import *
import connection as con
import errorMessage as em
from resultadosExpediente import ResultadoExpediente



class infoPaciente:
    def __init__(self, parent):
        self.widget_list_dataPersonal = []
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Información de paciente")

        main_frame = Frame(self.win)
        main_frame.pack(fill=BOTH, expand=1)
        
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar2 = Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar2.pack(side=BOTTOM, fill=X)

        
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.configure(xscrollcommand=my_scrollbar2.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        
        second_frame = Frame(my_canvas)
        
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        
        etiIdPaciente = Label(second_frame, text="Id del paciente")
        
        inputIdPaciente = Entry(second_frame)

        print(inputIdPaciente.get())
        
        buttonBuscar = Button(second_frame, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente, second_frame, contador = 4))
        
        etiIdPaciente.grid(row=0, column=1)
        inputIdPaciente.grid(row=1, column=1)
        buttonBuscar.grid(row=2, column=1)
        
        self.win.geometry("400x300")
        
    def buscarPaciente(self, inputIdPaciente, second_frame, contador):
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
            #ResultadoExpediente(self.win, results1, column_names)
            for i in range(len(results1)):
                etiNoResultado = Label(second_frame, text=f"Resultado Informacion de paciente {i+1}:", fg="#1e90ff")
                etiNoResultado.grid(row=contador, column=1)
                contador = contador + 1
                texto = ""
                for j in range(len(results1[i])):
                    texto = texto + f"{listColumnas1[j]}: {results1[i][j]} "
                etiResultado = Label(second_frame, text=texto)
                etiResultado.grid(row=contador, column=1)
                contador = contador + 1 
        else:
            mensaje = "No se ha encontrado la información del paciente"
            em.ErrorMessage(self.win, mensaje)
        if results2 is not None:
            listColumnas2 = list(column_names2)
            for i in range(len(results2)):
                etiNoResultado = Label(second_frame, text=f"Resultado historial de enfermedades {i+1}:", fg="#1e90ff")
                etiNoResultado.grid(row=contador, column=1)
                contador = contador + 1
                texto = ""
                for j in range(len(results2[i])):
                    texto = texto + f"{listColumnas2[j]}: {results2[i][j]} "
                etiResultado = Label(second_frame, text=texto)
                etiResultado.grid(row=contador, column=1)
                contador = contador + 1 
        else:
            mensaje = "No se ha encontrado el historial del paciente"
            em.ErrorMessage(self.win, mensaje)

        
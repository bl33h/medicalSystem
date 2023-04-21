from tkinter import *
import connection as con
from errorMessage import ErrorMessage
from datetime import datetime
import customtkinter as ct
from tkinter import messagebox

class Bodega:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Bodega")

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
        
        self.widget_list_dataPersonal = []

        etiTitle = ct.CTkLabel(second_frame, text="Bodega", font=("Arial", 20, "bold"))
        
        etiInformacion = ct.CTkLabel(second_frame, text="Ingrese los valores de cada campo, si no desea utilizar ese filtro deje el campo vacio\nIngrese la cantidad de insumos que desea agregar", font=("Arial", 10, "bold"), text_color="red")
        
        etiIdEstablecimiento = ct.CTkLabel(second_frame, text="Id Establecimiento")
        etiIdInsumo = ct.CTkLabel(second_frame, text="Id Insumo")
        
        inputIdEstablecimiento = ct.CTkEntry(second_frame, width=200)
        inputIdInsumo = ct.CTkEntry(second_frame, width=200)
        
        buttonEditar = ct.CTkButton(second_frame, text="Editar Insumo Existente", command= lambda: self.editarRegistro(inputIdEstablecimiento, inputIdInsumo, second_frame, contador = 8), width=200)
        buttonAgregaInsumo = ct.CTkButton(second_frame, text="Agregar Insumo", command= lambda: self.agregarInsumo(inputIdEstablecimiento, inputIdInsumo, second_frame, contador = 8), width=200)
        buttonBuscar = ct.CTkButton(second_frame, text="Buscar", command= lambda: self.buscarRegistro(inputIdEstablecimiento, inputIdInsumo, second_frame, contador = 8), width=200)
        
        etiTitle.grid(row=0, column=1)
        etiInformacion.grid(row=1, column=1)
        etiIdEstablecimiento.grid(row=2, column=1)
        inputIdEstablecimiento.grid(row=3, column=1, pady=5)
        etiIdInsumo.grid(row=4, column=1)
        inputIdInsumo.grid(row=5, column=1, pady=5)
        buttonBuscar.grid(row=6, column=1, pady=5)
        buttonEditar.grid(row=7, column=1, pady=5)
        buttonAgregaInsumo.grid(row=8, column=1, pady=5)
        
        self.win.geometry("600x500")
        
        # Registro de usuario        
    def editarRegistro(self, inputIdEstablecimiento, inputIdInsumo, second_frame, contador):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        dicLabels = {}
        dicResults = {}
        listResults = []
        queryColumn = f"select * from editar_insumos()"
        queryResults = f"select * from editar_insumos('{inputIdInsumo.get()}','{inputIdEstablecimiento.get()}');"
        column_names = con.column_names(queryColumn) # Obtener los nombres de las columnas
        results = con.connect(queryResults) # Obtener los valores de las columnas
        cantidadAnteriorInsumos = 0
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = ct.CTkLabel(second_frame, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
                
        if(len(listResults) == 0):
            ErrorMessage = (second_frame, "No se ha encontrado nada")
            
        else:
            keys = [] #Permite tener valores repetidos en el diccionario
            for i in range(len(listResults)):
                key = listResults[i]
                while (key in dicResults):
                    key = str(key) + "1"
                dicResults[key] = ct.CTkEntry(second_frame, width=200)
                if(i == 0):
                    cantidadAnteriorInsumos =  int(listResults[i])
                dicResults[key].insert(0, listResults[i]) # Inserta el valor en el Entry
                keys.append(key)
            
            if (len(listResults) == len(column_names)):
                for i in range(len(column_names)):
                    if(column_names[i] == "administrador"):
                        continue
                    dicLabels[column_names[i]].grid(row=contador, column=1)
                    contador += 1
                    dicResults[keys[i]].grid(row=contador, column=1)
                    contador += 1
                    self.widget_list_dataPersonal.append(dicLabels[column_names[i]])
                    self.widget_list_dataPersonal.append(dicResults[keys[i]])
        buttonEnviar = ct.CTkButton(second_frame, text="Enviar datos", command= lambda: EnviarDatos(dicResults[keys[0]].get(), cantidadAnteriorInsumos, listResults[1], inputIdEstablecimiento, inputIdInsumo), width=100)
        buttonEnviar.grid(row=contador, column=1)
        self.widget_list_dataPersonal.append(buttonEnviar)
        
        def EnviarDatos(nuevoInsumo, cantidadAnteriorInsumos, fechaAnterior, inputIdEstablecimiento, inputIdInsumo):
            insumos = int(nuevoInsumo) + int(cantidadAnteriorInsumos)
            queryResults = f"update establecimiento_posee_insumos set cantidad = {insumos} , fecha_de_vencimiento = '{fechaAnterior}' where id_establecimiento = '{inputIdEstablecimiento.get()}'and id_insumo = '{inputIdInsumo.get()}';"
            results = con.connect(queryResults)
            if(results == ""):
                mensaje = "Ingresado con exito"
                ErrorMessage(self.win, mensaje)
    
    def buscarRegistro(self, inputIdEstablecimiento, inputIdInsumo, second_frame, contador):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        
        queryColumn = f"select * from obtener_insumos()"
        
        if (inputIdEstablecimiento.get() == "" and inputIdInsumo.get() == ""):
            queryResults = f"select * from obtener_insumos(null, null);"
        elif (inputIdEstablecimiento.get() == ""):
            queryResults = f"select * from obtener_insumos(null, '{inputIdInsumo.get()}');"
        elif (inputIdInsumo.get() == ""):
            queryResults = f"select * from obtener_insumos('{inputIdEstablecimiento.get()}', null);"
        else:
            queryResults = f"select * from obtener_insumos('{inputIdEstablecimiento.get()}', '{inputIdInsumo.get()}');"
        
        column_names = con.column_names(queryColumn) # Obtener los nombres de las columnas
        results = con.connect(queryResults) # Obtener los valores de las columnas
        
        if results is not None:
                listColumnas = list(column_names)
        for i in range(len(results)):
            etiNoResultado = Label(second_frame, text=f"Resultado {i+1}:", fg="#1e90ff")
            etiNoResultado.grid(row=contador, column=1)
            self.widget_list_dataPersonal.append(etiNoResultado)
            contador += 1
            texto = ""
            for j in range(len(results[i])):
                texto = texto + f"{listColumnas[j]}: {results[i][j]} "
            etiResultado = Label(second_frame, text=texto)
            etiResultado.grid(row=contador, column=1)
            self.widget_list_dataPersonal.append(etiResultado)
            contador += 1
        query = f"select* from generar_alertas('{inputIdEstablecimiento.get()}');" # Generador de alertas
        alertas = con.connect(query)
        if alertas is not None:
            for alerta in alertas:
                tipo_alerta = alerta[0]
                if tipo_alerta != "Vigente": # Solamente si el estado es diferente a vigente
                    nombre_insumo = alerta[1]
                    fecha_de_vencimiento = alerta[2]
                    cantidad = alerta[3]
                    messagebox.showinfo("¡Alerta!", f"El insumo: {nombre_insumo}\nSe encuentra: {tipo_alerta}\nFecha de vencimiento: {fecha_de_vencimiento}\nCantidad: {cantidad}\n")

        else:
            mensaje = "No se ha encontrado nada"
            ErrorMessage(self.win, mensaje)
            
    def agregarInsumo(self, inputIdEstablecimiento, inputIdInsumo, second_frame, contador):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        
        etiCantidad = ct.CTkLabel(second_frame, text="Cantidad")
        self.widget_list_dataPersonal.append(etiCantidad)
        etiFechaVencimiento = ct.CTkLabel(second_frame, text="Fecha de vencimiento")
        self.widget_list_dataPersonal.append(etiFechaVencimiento)
        
        inputCantidad = ct.CTkEntry(second_frame, width=200)
        self.widget_list_dataPersonal.append(inputCantidad)
        inputFechaVencimiento = ct.CTkEntry(second_frame, width=200)
        self.widget_list_dataPersonal.append(inputFechaVencimiento)
        
        etiCantidad.grid(row=contador, column=1)
        contador += 1
        inputCantidad.grid(row=contador, column=1)
        contador += 1
        etiFechaVencimiento.grid(row=contador, column=1)
        contador += 1
        inputFechaVencimiento.grid(row=contador, column=1)
        contador += 1
        
        buttonEnviarInfo = ct.CTkButton(second_frame, text="Enviar datos", command= lambda: EviarDatos(inputIdEstablecimiento, inputIdInsumo, inputCantidad, inputFechaVencimiento), width=100)
        self.widget_list_dataPersonal.append(buttonEnviarInfo)
        buttonEnviarInfo.grid(row=contador, column=1)
        
        def EviarDatos(inputIdEstablecimiento, inputIdInsumo, inputCantidad, inputFechaVencimiento):
            query = f"select * from insertar_insumos('{inputIdEstablecimiento.get()}', '{inputIdInsumo.get()}', {inputCantidad.get()}, '{inputFechaVencimiento.get()}');"
            results = con.connect(query)
            if (results == None):
                mensaje = "Ha ocurrido un error al agregar el insumo"
                ErrorMessage(self.win, mensaje=mensaje)
            else:
                mensaje = "Se ha agregado el insumo con id " + inputIdInsumo.get() + " al establecimiento con id " + inputIdEstablecimiento.get()
                ErrorMessage(self.win, mensaje=mensaje)
        
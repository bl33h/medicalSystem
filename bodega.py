from tkinter import *
import connection as con
from errorMessage import ErrorMessage
import customtkinter as ct

class Bodega:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Bodega")
        etiTitle = ct.CTkLabel(self.win, text="Bodega", font=("Arial", 20, "bold"))
        
        scrollbar = ct.CTkScrollbar(self.win)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.widget_list_dataPersonal = []
        
        etiInformacion = ct.CTkLabel(self.win, text="Ingrese los valores de cada campo, si no desea utilizar ese filtro deje el campo vacio", text_color="red")
        
        etiIdEstablecimiento = ct.CTkLabel(self.win, text="Id Establecimiento")
        etiIdInsumo = ct.CTkLabel(self.win, text="Id Insumo")
        
        inputIdEstablecimiento = ct.CTkEntry(self.win, width=200)
        inputIdInsumo = ct.CTkEntry(self.win, width=200)
        
        buttonEditar = ct.CTkButton(self.win, text="Editar", command= lambda: self.editarRegistro(inputIdEstablecimiento, inputIdInsumo), width=100)
        buttonBuscar = ct.CTkButton(self.win, text="Buscar", command= lambda: self.buscarRegistro(inputIdEstablecimiento, inputIdInsumo), width=100)
        
        etiTitle.pack(pady=5)
        etiInformacion.pack(pady=5)
        etiIdEstablecimiento.pack()
        inputIdEstablecimiento.pack(pady=5)
        etiIdInsumo.pack()
        inputIdInsumo.pack(pady=5)
        buttonBuscar.pack(pady=5)
        buttonEditar.pack(pady=5)
        
        self.win.geometry("700x700")
        
        # Registro de usuario        
    def editarRegistro(self, inputIdEstablecimiento, inputIdInsumo):
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
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = ct.CTkLabel(self.win, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
                
        if (len(listResults) == 0):
            ErrorMessage(self.win, "No se ha encontrado nada")
            
        else:
            keys = [] #Permite tener valores repetidos en el diccionario
            for i in range(len(listResults)):
                key = listResults[i]
                while (key in dicResults):
                    key = str(key) + "1"
                dicResults[key] = ct.CTkEntry(self.win, width=200)
                dicResults[key].insert(0, listResults[i]) # Inserta el valor en el Entry
                keys.append(key)
            
            if (len(listResults) == len(column_names)):
                for i in range(len(column_names)):
                    if(column_names[i] == "administrador"):
                        continue
                    dicLabels[column_names[i]].pack()
                    dicResults[keys[i]].pack()
                    self.widget_list_dataPersonal.append(dicLabels[column_names[i]])
                    self.widget_list_dataPersonal.append(dicResults[keys[i]])
    
    def buscarRegistro(self, inputIdEstablecimiento, inputIdInsumo):
        
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
                etiNoResultado = ct.CTkLabel(self.win, text=f"Resultado {i+1}:", text_color="#1e90ff")
                etiNoResultado.pack()
                texto = ""
                for j in range(len(results[i])):
                    texto = texto + f"{listColumnas[j]}: {results[i][j]} "
                etiResultado = ct.CTkLabel(self.win, text=texto)
                etiResultado.pack() 
        else:
            mensaje = "No se ha encontrado nada"
            ErrorMessage(self.win, mensaje)
         

        
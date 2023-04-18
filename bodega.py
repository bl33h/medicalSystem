from tkinter import *
import connection as con
from errorMessage import ErrorMessage

class Bodega:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Bodega")
        self.widget_list_dataPersonal = []
        
        etiInformacion = Label(self.win, text="Ingrese los valores de cada campo, si no desea utilizar ese filtro deje el campo vacio")
        etiInformacion.pack()
        
        etiIdEstablecimiento = Label(self.win, text="Id Establecimiento")
        etiIdInsumo = Label(self.win, text="Id Insumo")
        
        inputIdEstablecimiento = Entry(self.win)
        inputIdInsumo = Entry(self.win)
        
        buttonEditar = Button(self.win, text="Editar", command= lambda: self.editarRegistro(inputIdEstablecimiento, inputIdInsumo))
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarRegistro(inputIdEstablecimiento, inputIdInsumo))
        
        etiIdEstablecimiento.pack()
        inputIdEstablecimiento.pack()
        etiIdInsumo.pack()
        inputIdInsumo.pack()
        buttonBuscar.pack()
        buttonEditar.pack()
        
        self.win.geometry("600x500")
        
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
            dicLabels[column_names[i]] = Label(self.win, text=column_names[i].capitalize())
            
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
                dicResults[key] = Entry(self.win)
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
                etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
                etiNoResultado.pack()
                texto = ""
            for j in range(len(results[i])):
                texto = texto + f"{listColumnas[j]}: {results[i][j]} "
            etiResultado = Label(self.win, text=texto)
            etiResultado.pack() 
        else:
            mensaje = "No se ha encontrado nada"
            ErrorMessage(self.win, mensaje)
         

        
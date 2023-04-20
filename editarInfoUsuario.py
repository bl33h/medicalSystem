from tkinter import *
from errorMessage import ErrorMessage
import connection as con
import customtkinter as ct

class EditarInfoUsuario:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Editar Informacion de Usuario")
        self.widget_list_dataPersonal = []
        etiTitle = ct.CTkLabel(self.win, text="Editar Informacion de Usuario", font=("Arial", 20, "bold"))
        
        etiIdUsuario = ct.CTkLabel(self.win, text="Id del usuario")
        inputIdUsuario = ct.CTkEntry(self.win, width=200)
        buttonBuscar = ct.CTkButton(self.win, text="Buscar", command= lambda: self.buscarUsuario(inputIdUsuario), width=100)
        etiUsuario = ct.CTkLabel(self.win, text="Usuario", width=200)
        etiContrasena = ct.CTkLabel(self.win, text="Contraseña", width=200)
        inputUsuario = ct.CTkEntry(self.win, width=200)
        inputContrasena = ct.CTkEntry(self.win, width=200)
        buttonBuscarRegistro = ct.CTkButton(self.win, text="Buscar", command= lambda: self.buscarRegistroUsuario(inputUsuario, inputContrasena), width=100)
        
        etiTitle.pack(pady=5)
        etiIdUsuario.pack()
        inputIdUsuario.pack(pady=5)
        buttonBuscar.pack(pady=5)
        
        
        etiUsuario.pack()
        inputUsuario.pack(pady=5)
        etiContrasena.pack()
        inputContrasena.pack(pady=5)
        buttonBuscarRegistro.pack(pady=5)
        
        self.win.geometry("600x700")
        
    def buscarUsuario(self, inputIdUsuario):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        dicLabels = {}
        dicResults = {}
        listResults = []
        queryColumn = f"SELECT * FROM medico where num_col = '{inputIdUsuario.get()}'"
        queryResults = f"SELECT * FROM medico where num_col = '{inputIdUsuario.get()}'"
        column_names = con.column_names(queryColumn) # Obtener los nombres de las columnas
        results = con.connect(queryResults) # Obtener los valores de las columnas
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = ct.CTkLabel(self.win, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
                
        if (len(listResults) == 0):
            ErrorMessage(self.win, "No se encontro el usuario")
            
        else:
            keys = [] #Permite tener valores repetidos en el diccionario
            for i in range(len(listResults)):
                key = listResults[i]
                while (key in dicResults):
                    key = key + "1"
                dicResults[key] = ct.CTkEntry(self.win, width=200)
                dicResults[key].insert(0, listResults[i]) # Inserta el valor en el Entry
                keys.append(key)
            
            if (len(listResults) == len(column_names)):
                for i in range(len(column_names)):
                    dicLabels[column_names[i]].pack()
                    dicResults[keys[i]].pack()
                    self.widget_list_dataPersonal.append(dicLabels[column_names[i]])
                    self.widget_list_dataPersonal.append(dicResults[keys[i]])
            
            buttonModificar = ct.CTkButton(self.win, text="Modificar", command= lambda: ObtenerValoresNuevos(), width=100)
            buttonModificar.pack()
            self.widget_list_dataPersonal.append(buttonModificar)
            
            def ObtenerValoresNuevos():
                newValores = []
                for i in dicResults:
                    newValores.append(dicResults[i].get())
                self.ModificaValores(newValores, inputIdUsuario)
             
    def ModificaValores(self, newValores, inputIdUsuario):
        update = f"UPDATE medico SET num_col = '{newValores[0]}', nombre = '{newValores[1]}', apellido = '{newValores[2]}', especialidad = '{newValores[3]}', telefono = '{newValores[4]}', direccion = '{newValores[5]}', email = '{newValores[6]}' WHERE num_col = '{inputIdUsuario.get()}'"
        resultado = con.connect(update)
        if (resultado == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    
    # Registro de usuario        
    def buscarRegistroUsuario(self, inputUsuario, inputContrasena):
        for widget in self.widget_list_dataPersonal:
            widget.destroy()
        self.widget_list_dataPersonal = []
        dicLabels = {}
        dicResults = {}
        listResults = []
        queryColumn = f"SELECT * FROM usuarios"
        queryResults = f"SELECT * FROM usuarios where usuario = '{inputUsuario.get()}' and contrasena = '{inputContrasena.get()}' and administrador = false"
        column_names = con.column_names(queryColumn) # Obtener los nombres de las columnas
        results = con.connect(queryResults) # Obtener los valores de las columnas
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = ct.CTkLabel(self.win, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
                
        if (len(listResults) == 0):
            ErrorMessage(self.win, "No se encontro el usuario")
            
        else:
            keys = [] #Permite tener valores repetidos en el diccionario
            for i in range(len(listResults)):
                key = listResults[i]
                while (key in dicResults):
                    key = str(key) + "1"
                dicResults[key] = ct.CTkEntry(self.win)
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
            
            buttonModificar = ct.CTkButton(self.win, text="Modificar", command= lambda: ObtenerValoresNuevosRegistroUsuario())
            buttonModificar.pack()
            self.widget_list_dataPersonal.append(buttonModificar)
            
            def ObtenerValoresNuevosRegistroUsuario():
                newValores = []
                for i in dicResults:
                    newValores.append(dicResults[i].get())
                self.ModificalValoresRegistroUsuario(newValores, inputUsuario, inputContrasena)
             
    def ModificalValoresRegistroUsuario(self, newValores, inputUsuario, inputContrasena):
        update = f"UPDATE usuarios SET usuario = '{newValores[0]}', contrasena = '{newValores[1]}', id_establecimiento = '{newValores[2]}', administrador = false, encargado_bodega = '{newValores[4]}' where usuario = '{inputUsuario.get()}' and contrasena = '{inputContrasena.get()}'"
        resultado = con.connect(update)
        if (resultado == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
        
        
        
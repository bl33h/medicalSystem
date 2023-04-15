from tkinter import *
from errorMessage import ErrorMessage
import connection as con

class EditarInfoUsuario:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Editar Informacion de Usuario")
        self.widget_list = []
        
        etiIdUsuario = Label(self.win, text="Id del usuario")
        inputIdUsuario = Entry(self.win)
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarUsuario(inputIdUsuario))
        
        etiIdUsuario.pack()
        inputIdUsuario.pack()
        buttonBuscar.pack()
        
        self.win.geometry("600x800")
        
    def buscarUsuario(self, inputIdUsuario):
        for widget in self.widget_list:
            widget.destroy()
        self.widget_list = []
        dicLabels = {}
        dicResults = {}
        listResults = []
        queryColumn = f"SELECT * FROM medico where num_col = '{inputIdUsuario.get()}'"
        queryResults = f"SELECT * FROM medico where num_col = '{inputIdUsuario.get()}'"
        column_names = con.column_names(queryColumn) # Obtener los nombres de las columnas
        results = con.connect(queryResults) # Obtener los valores de las columnas
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = Label(self.win, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
                
        if (len(listResults) == 0):
            ErrorMessage(self.win, "No se encontro el usuario")
            
        else:
            for i in range(len(listResults)):
                dicResults[listResults[i]] = Entry(self.win)
                dicResults[listResults[i]].insert(0, listResults[i]) # Inserta el valor en el Entry
            
            if (len(listResults) == len(column_names)):
                for i in range(len(column_names)):
                    dicLabels[column_names[i]].pack()
                    dicResults[listResults[i]].pack()
                    self.widget_list.append(dicLabels[column_names[i]])
                    self.widget_list.append(dicResults[listResults[i]])
            
            buttonModificar = Button(self.win, text="Modificar", command= lambda: ObtenerValoresNuevos())
            buttonModificar.pack()
            self.widget_list.append(buttonModificar)
            
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
        
        
        
from tkinter import *

class ResultadoExpediente:
    def __init__(self, parent, results, column_names):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        dicLabels = {}
        dicResults = {}
        listResults = []
        
        for i in range(len(column_names)):
            dicLabels[column_names[i]] = Label(self.win, text=column_names[i].capitalize())
            
        for i in range(len(results)):
            listResults = list(results[i])
        
        for i in range(len(listResults)):
            dicResults[listResults[i]] = Entry(self.win)
            dicResults[listResults[i]].insert(0, listResults[i]) # Inserta el valor en el Entry
            
            
        if (len(listResults) == len(column_names)):
            for i in range(len(column_names)):
                dicLabels[column_names[i]].pack()
                dicResults[listResults[i]].pack()
                
        buttonModificar = Button(self.win, text="Modificar", command= lambda: ObtenerValoresNuevos())
        buttonModificar.pack()
        
        def ObtenerValoresNuevos():
            newValores = []
            for i in dicResults:
                newValores.append(dicResults[i].get())
            self.ModificaValores(newValores)
        
        self.win.geometry("600x600")
        
    def ModificaValores(self, newValores):
        for i in newValores:
            print(i)
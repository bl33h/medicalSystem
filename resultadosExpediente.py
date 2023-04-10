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
            dicResults[listResults[i]] = Label(self.win, text=listResults[i])
            
        if (len(listResults) == len(column_names)):
            for i in range(len(column_names)):
                dicLabels[column_names[i]].pack()
                dicResults[listResults[i]].pack()
        
        
        self.win.geometry("600x600")
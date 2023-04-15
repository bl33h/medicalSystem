from tkinter import *

class ResultadoExpediente:
    def __init__(self, parent, results, column_names):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        listColumnas = list(column_names)
        
        
        for i in range(len(results)):
            etiNoResultado = Label(self.win, text=f"Resultado {i+1}:", fg="#1e90ff")
            etiNoResultado.pack()
            texto = ""
            for j in range(len(results[i])):
                texto = texto + f"{listColumnas[j]}: {results[i][j]} "
            etiResultado = Label(self.win, text=texto)
            etiResultado.pack()    
        
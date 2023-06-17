from tkinter import *
import connection as con
import customtkinter as ct
from errorMessage import ErrorMessage

class asignarInsumos:
    def __init__(self, parent, idCaso):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Asignacion de insumos")
        etiTitle = ct.CTkLabel(self.win, text="Asignacion de insumos", font=("Arial", 20, "bold"))
        
        etiIdCaso = ct.CTkLabel(self.win, text="Id Caso")
        inputIdCaso = ct.CTkEntry(self.win, width=200)
        inputIdCaso.insert(0, idCaso)
        
        etiIdInsumo = ct.CTkLabel(self.win, text="Id insumo")
        inputIdInsumo= ct.CTkEntry(self.win, width=200)

        etiCantidad = ct.CTkLabel(self.win, text="Cantidad")
        inputCantidad= ct.CTkEntry(self.win, width=200)
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.inputAsignacionInsumos(inputIdCaso, inputIdInsumo, inputCantidad), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiIdCaso.pack()
        inputIdCaso.pack(pady=5)
        etiIdInsumo.pack()
        inputIdInsumo.pack(pady=5)
        etiCantidad.pack()
        inputCantidad.pack(pady=5)
        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def inputAsignacionInsumos(self, inputIdCaso, inputIdInsumo, inputCantidad):
        query = f"insert into caso_insumos values({inputIdCaso.get()}, {inputIdInsumo.get()}, '{inputCantidad.get()}')"
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            query = f"select * from update_medicines({inputIdCaso.get()})"
            results = con.connect(query)
            ErrorMessage(self.win, mensaje=mensaje)
            
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
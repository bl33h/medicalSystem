from tkinter import *
import connection as con
import customtkinter as ct
from errorMessage import ErrorMessage

class transferirMedico:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Transferir Medico")
        etiTitle = ct.CTkLabel(self.win, text="Transferir medico", font=("Arial", 20, "bold"))

        # id de transferencia es serial. 
        
        etiNum_col = ct.CTkLabel(self.win, text="Numero colegiado")
        inputNum_col = ct.CTkEntry(self.win, width=200)

        etiEstablecimientoOrigen = ct.CTkLabel(self.win, text="Id del establecimient de origen")
        inputEstablecimientoOrigen = ct.CTkEntry(self.win, width=200)

        etiEstablecimientoDestino = ct.CTkLabel(self.win, text="Id del establecimiento de destino")
        inputEstablecimientoDestino = ct.CTkEntry(self.win, width=200)

        etiFecha = ct.CTkLabel(self.win, text="Fecha")
        inputFecha = ct.CTkEntry(self.win, width=200)

        # descripcion
        etiDescripcion = ct.CTkLabel(self.win, text="Descripcion")
        inputDescripcion = ct.CTkEntry(self.win, width=200)
        
        
        
        buttonSignup = ct.CTkButton(self.win, text="Registrar", command= lambda: self.insert_transferencia(inputNum_col, inputEstablecimientoOrigen, inputEstablecimientoDestino, inputFecha, inputDescripcion), width=100)
        buttonClose = ct.CTkButton(self.win, text="Close", command= lambda: self.close(), width=100)
        
        etiTitle.pack(pady=5)
        etiNum_col.pack()
        inputNum_col.pack(pady=5)
        etiEstablecimientoOrigen.pack()
        inputEstablecimientoOrigen.pack(pady=5)
        etiEstablecimientoDestino.pack()
        inputEstablecimientoDestino.pack(pady=5)
        etiFecha.pack()
        inputFecha.pack(pady=5)
        etiDescripcion.pack()
        inputDescripcion.pack(pady=5)

        buttonSignup.pack(pady=5)
        buttonClose.pack(pady=5)

        self.win.geometry("600x1000")
        
    def insert_transferencia(self, inputNum_col, inputEstablecimientoOrigen, inputEstablecimientoDestino, inputFecha, inputDescripcion):
        query = r"""insert into transferencias (num_col_medico, id_origen, id_destino, fecha_transferencia, descripcion) values('""" + inputNum_col.get() + r"""', '""" + inputEstablecimientoOrigen.get() + r"""', '""" + inputEstablecimientoDestino.get() + r"""', '""" + inputFecha.get() + r"""', '""" + inputDescripcion.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "Ha ocurrido un error al registrar"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
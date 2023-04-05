from tkinter import *
from errorMessage import ErrorMessage
from ingresoMedico import IngresoMedico
import connection as con

class SignupWindow:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Signup")
        
        etiUsername = Label(self.win, text="Username")
        inputUsername = Entry(self.win)
        
        etiPassword = Label(self.win, text="Password")
        inputPassword = Entry(self.win)
        
        etiIdEstablecimiento = Label(self.win, text="Id Establecimiento")
        inputIdEstablecionto = Entry(self.win)
        
        buttonSignup = Button(self.win, text="Signup", command= lambda: self.checkSignUp(inputPassword, inputUsername, inputIdEstablecionto))
        buttonClose = Button(self.win, text="Close", command= lambda: self.close())
        
        etiUsername.pack()
        inputUsername.pack()
        etiPassword.pack()
        inputPassword.pack()
        etiIdEstablecimiento.pack()
        inputIdEstablecionto.pack()
        buttonSignup.pack()
        buttonClose.pack()

        self.win.geometry("300x200")
        
    def checkSignUp(self,inputPassword, inputUsername, inputIdEstablecimiento):
        valor = False
        errorPassword = False
        errorUser = False
        
        valor = self.checkLongitud(inputPassword.get())
        if(valor == True):
            mensaje = "La contraseña es muy larga el máximo es de 50 caracteres o esta vacio"
            ErrorMessage(self.win, mensaje=mensaje)
            errorPassword = True
            
            
        valor = self.checkLongitud(inputUsername.get())
        if(valor == True):
            mensaje = "El username es muy largo el máximo es de 50 caracteres o esta vacio"
            ErrorMessage(self.win, mensaje=mensaje)
            errorUser = True
        
        if (errorPassword == False and errorUser == False):
            self.insertValues(inputPassword, inputUsername, inputIdEstablecimiento)
    
    def checkLongitud(self, cadena):
        valor = False
        
        if (len(cadena) > 51 or len(cadena) == 0):
            valor = True
        return valor
    
    def insertValues(self, inputPassword, inputUsername, inputIdEstablecimiento):
        query = r"""insert into usuarios values ('""" + inputUsername.get() + r"""', '""" + inputPassword.get() + r"""', '""" + inputIdEstablecimiento.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
            IngresoMedico(self.win)
            
        else:
            mensaje = "El usuario y contrasena ya existen, o verifique que el id del establecimiento sea correcto"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
        
        
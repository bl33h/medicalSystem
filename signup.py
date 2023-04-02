from tkinter import *
from errorMessage import ErrorMessage
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
        
        buttonSignup = Button(self.win, text="Signup", command= lambda: self.checkSignUp(inputPassword, inputUsername))
        
        etiUsername.pack()
        inputUsername.pack()
        etiPassword.pack()
        inputPassword.pack()
        buttonSignup.pack()

        self.win.geometry("300x200")
        
    def checkSignUp(self,inputPassword, inputUsername):
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
            self.insertValues(inputPassword, inputUsername)
    
    def checkLongitud(self, cadena):
        valor = False
        
        if (len(cadena) > 51 or len(cadena) == 0):
            valor = True
        return valor
    
    def insertValues(self, inputPassword, inputUsername):
        query = r"""insert into usuarios values('""" + inputUsername.get() + r"""','""" + inputPassword.get() + r"""');"""
        results = con.connect(query)
        if (results == ""):
            mensaje = "Se ha registrado correctamente"
            ErrorMessage(self.win, mensaje=mensaje)
        else:
            mensaje = "El usuario y contrasena ya existen"
            ErrorMessage(self.win, mensaje=mensaje)
    
    def close(self):
        self.win.destroy()
        
        
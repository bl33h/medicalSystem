from tkinter import *

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
        checkLongitudPassword = self.checkLongitud(inputPassword)
        checkLongitudUsuario = self.checkLongitud(inputUsername)

        if(checkLongitudPassword == True):
            etiErrorPassword = Label(self.win, text="Password")
            etiErrorPassword.pack()
        if(checkLongitudUsuario == True):
            etiErrorUsername = Label(self.win, text="Username")
            etiErrorUsername.pack()
        
        
        etiUsername.pack()
        inputUsername.pack()
        etiPassword.pack()
        inputPassword.pack()
        buttonSignup.pack()

        self.win.geometry("300x200")
        
    def checkSignUp(self,inputPassword, inputUsername):
        checkLongitud()
    
    def checkLongitud(self, cadena):
        valor = False
        print(len(cadena))
        if (len(cadena) > 51):
            valor = True
        return valor
    
    def close(self):
        self.win.destroy()
        
        
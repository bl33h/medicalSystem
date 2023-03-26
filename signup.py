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
        
        etiUsername.pack()
        inputUsername.pack()
        etiPassword.pack()
        inputPassword.pack()
        buttonSignup.pack()

        self.win.geometry("300x200")
        
    def checkSignUp(self,inputPassword, inputUsername):
        print("Username: " + inputUsername.get())
        print("Password: " + inputPassword.get())
        self.close()
    
    def close(self):
        self.win.destroy()
        
        
from tkinter import *
from signup import SignupWindow

def principalWindow():
    parent = parent
    win = Toplevel(parent)
    win.title("Login")
    
    etiUsername = Label(win, text="Username")
    inputUsername = Entry(win)
    
    etiPassword = Label(win, text="Password")
    inputPassword = Entry(win)
    
    buttonLogin = Button(win, text="Login", command= lambda: login(inputPassword, inputUsername))
    buttonSignup = Button(win, text="Signup", command= lambda: signup(win))
    
    etiUsername.pack()
    inputUsername.pack()
    etiPassword.pack()
    inputPassword.pack()
    buttonLogin.pack()
    buttonSignup.pack()

    win.geometry("300x200")
    win.mainloop()
    
def login(inputPassword, inputUsername):
    Username = inputUsername.get()
    Password = inputPassword.get()
    print(Username)
    print(Password)
    
def signup(win):
    SignupWindow(win)
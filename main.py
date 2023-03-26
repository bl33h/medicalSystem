from tkinter import *
from signUp import SignupWindow
from expediente import ExpedienteWindow
import connection as con


def main():
    results = con.connect(r"""select * from prueba;""")
    print(results)
    principalWindow()
   
   

def principalWindow():
    win = Tk()
    win.title("Login")
    
    etiUsername = Label(win, text="Username")
    inputUsername = Entry(win)
    
    etiPassword = Label(win, text="Password")
    inputPassword = Entry(win)
    
    buttonLogin = Button(win, text="Login", command= lambda: login(inputPassword, inputUsername, win))
    buttonSignup = Button(win, text="Signup", command= lambda: signUp(win))
    
    etiUsername.pack()
    inputUsername.pack()
    etiPassword.pack()
    inputPassword.pack()
    buttonLogin.pack()
    buttonSignup.pack()

    win.geometry("300x200")
    win.mainloop()
    
def signUp(win):
    SignupWindow(win)
    
def login(inputPassword, inputUsername, win):
    if (inputPassword.get() == "123" and inputUsername.get() == "123"):
        ExpedienteWindow(win)


    
if __name__ == '__main__':
    main()
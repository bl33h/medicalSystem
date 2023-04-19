from tkinter import *
from tkinter import messagebox
from expediente import ExpedienteWindow
import connection as con
from signup import SignupWindow


def main():
    principalWindow()
   
   

def principalWindow():
    win = Tk()
    win.title("Login")
    etiTitle = Label(win, text="Login", font=("Arial", 20, "bold"))
    etiUsername = Label(win, text="Username")
    inputUsername = Entry(win)
    
    etiPassword = Label(win, text="Password")
    inputPassword = Entry(win, show = "*")
    
    buttonLogin = Button(win, text="Login", command= lambda: login(inputPassword, inputUsername, win), width=15)
    buttonCrearUsuario = Button(win, text="Crear Usuario", command= lambda: SignupWindow(win), width=15)
    
    etiTitle.pack(pady=5)
    etiUsername.pack()
    inputUsername.pack(pady=5)
    etiPassword.pack()
    inputPassword.pack(pady=5)
    buttonLogin.pack(pady=5)
    buttonCrearUsuario.pack(pady=5)

    win.geometry("300x250")
    win.mainloop()
    
# Login function
def login(inputUsername, inputPassword, win):
    usuario = inputUsername.get()
    contrasena = inputPassword.get()
    query = f"SELECT COUNT(*) FROM usuarios WHERE usuario='{usuario}' AND contrasena='{contrasena}'" # Query
    results = con.connect(query)
    query2 = f"SELECT administrador FROM usuarios WHERE usuario='{usuario}' AND contrasena='{contrasena}'"
    results2 = con.connect(query2)
    query3 = f"SELECT encargado_bodega FROM usuarios WHERE usuario='{usuario}' AND contrasena='{contrasena}'"
    results3 = con.connect(query3)
    try:
        results2 = results2[0][0]
        results3 = results3[0][0]
    except:
        pass
    
    # None type data verification
    if results is not None and results[0][0] == 1:
        ExpedienteWindow(win, results2, results3)
        
    # Error message if credentials do not match
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

if __name__ == '__main__':
    main()
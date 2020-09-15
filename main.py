from tkinter import *
from tkinter import Tk, Label, Button, messagebox, ttk
from api_test_lucas import get_TOKEN
import requests
import json
import os
import time


global token


class IOL_GUI_LOGIN :

    def __init__ (self, master=Tk()):
        ###Login page###
        self.user_gui=StringVar()
        self.pass_gui=StringVar()
        self.login_page=master
        self.login_page.title("Login IoL")
        self.login_page.geometry('300x150')
        ###Login Labels######
        self.login_Label=Label(self.login_page, text="Inicio Sesion", font=("Helvetica",13), anchor="center").grid(row=0,column=0, columnspan=2)
        self.user_Label=Label(self.login_page, text="Usuario", font=('Helvetica',10)).grid(row=1, column=0)
        self.pass_Label=Label(self.login_page, text="Contraseña", font=('Helvetica',10)).grid(row=2, column=0)
        ###Login Entry#####
        self.user_Entry=Entry(self.login_page,textvariable=self.user_gui).grid(row=1, column=1)
        self.pass_Entry=Entry(self.login_page,textvariable=self.pass_gui,show="*").grid(row=2, column=1)
        ###Login Buttons###
        self.login_Button=Button(self.login_page ,text="Login",command=self.login).grid(row=3,column=0, columnspan=2)
        
    def login(self):
        global token
        username=self.user_gui.get()
        password=self.pass_gui.get()
        _data= {
    'username': username,
    'password': password,
    'grant_type':'password'}
        print(_data)
        try:
            token=get_TOKEN(_data)
            self.login_page.destroy()
        except KeyError:
            messagebox.showwarning("Login failed", "Username or password incorrect!")
    def mainloop_window(self):

        self.login_page.mainloop()

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.geometry("800x500")
        main_window.title("IoL Aplicacion v0.1")
        
        # Crear el panel de pestañas.
        self.pes = ttk.Notebook(self)
        self.pes.pack(fill='both',expand='yes')
        
        # Crear el contenido de cada una de las pestañas.

        self.pes_estado=ttk.Frame(self.pes)

        
        # Añadirlas al panel con su respectivo texto.
        self.pes.add(self.pes_estado, text="Estado de Cuenta", padding=20)
        
        
        #self.notebook.pack(padx=10, pady=10)
        #self.pack()



'''
root =Tk()
root.title("MAIN WINDOW")
root.geometry('800x800')
'''
#iol=IOL_GUI_LOGIN()
#iol.mainloop_window()
print("esta ok")
#print(token)
main_window = Tk()
app = Application(main_window)
app.mainloop()
#root.mainloop()
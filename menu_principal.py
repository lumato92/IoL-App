from tkinter import *
import tkinter
from tkinter import ttk
import json

class Main_win :
    def __init__(self , data, main_win=Tk()):

        self.main_window=main_win
        self.main_window.title("Ventana principal")
        self.main_window.geometry("500x500")
        self.datos=data    
    ###Genero panel pestañas####
        self.pestana=ttk.Notebook(self.main_window)
        self.pestana.pack(fill='both', expand='yes')

    ### creo pestaña###
        self.p1=ttk.Frame(self.pestana)

    #Agrego pestaña creada####
        self.pestana.add(self.p1,text="Estado Cuenta")
    
    
    #AGREGO LABEL

        self.label1=Label(self.p1,text="Estado de Cuenta",font=('Helvetica',20),justify='center').grid(row=0, column=1, columnspan=4)
        self.label2=Label(self.p1,text="Numero de Cuenta",font=('Helvetica',10)).grid(row=1, column=0)
        self.label3=Label(self.p1,text="Disponible",font=('Helvetica',10)).grid(row=2, column=0)
        self.label4=Label(self.p1,text="Comprometido",font=('Helvetica',10)).grid(row=3, column=0)
        self.label5=Label(self.p1,text="Saldo",font=('Helvetica',10)).grid(row=4, column=0)
        self.label6=Label(self.p1,text="Valor Titulos",font=('Helvetica',10)).grid(row=5, column=0)
        self.label7=Label(self.p1,text="Total",font=('Helvetica',10)).grid(row=6, column=0)
        self.label8=Label(self.p1,text="Margen Descubierto",font=('Helvetica',10)).grid(row=7, column=0)
         
        self.data2=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['numero']),justify='center').grid(row=1, column=1)
        self.data3=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['disponible']),justify='right').grid(row=2, column=1)
        self.data4=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['comprometido']),justify='right').grid(row=3, column=1)
        self.data5=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['saldo']),justify='right').grid(row=4, column=1)
        self.data6=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['titulosValorizados']),justify='right').grid(row=5, column=1)
        self.data7=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['total']),justify='right').grid(row=6, column=1)
        self.data8=Entry(self.p1,textvariable=StringVar(value=self.datos['cuentas'][0]['margenDescubierto']),justify='right').grid(row=7, column=1)       



    def mainloop_window(self):

        self.main_window.mainloop()

def carga_Datos(): #Funcion de testeo
    with open('data.json') as test_data:
        return json.load(test_data)
data=carga_Datos()
IOL_main=Main_win(carga_Datos())
IOL_main.mainloop_window()
import json
from tkinter import ttk 
from tkinter import *

with open('panel_lider.json') as file:	
	datos=json.load(file)
print(len(datos['titulos']))
#print (datos['cuentas'].keys)
#datos1=(datos.get('cuentas',{}))
#print(type(datos))
23188
'''
for element in datos['cuentas'][0].items():
	print(element)
'''


win=Tk()
treev=ttk.Treeview(win,selectmode='browse')
treev.pack()
verscrlbar = ttk.Scrollbar(win,orient ="vertical",command = treev.yview)
verscrlbar.pack(side ='right', fill ='x')
treev.configure(xscrollcommand = verscrlbar.set)
treev["columns"] = ("1","2","3","4","5")
    # Defining heading 
treev['show'] = 'headings'
      
    # Assigning the width and anchor to  the 
    # respective columns 
treev.column("1", width = 200, anchor ='c') 
treev.column("2", width = 200, anchor ='se') 
treev.column("3", width = 200, anchor ='se')
treev.column("2", width = 200, anchor ='se') 
treev.column("3", width = 200, anchor ='se')

treev.heading("1", text ="Name") 
treev.heading("2", text ="Sex") 
treev.heading("3", text ="Age")
  
win.mainloop()
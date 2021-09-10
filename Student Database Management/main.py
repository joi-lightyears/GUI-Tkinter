import sqlite3
conn = sqlite3.connect("Student_Management_Database_jupyter.db")
c = conn.cursor()
options = ['Choose']
sql="SELECT * FROM Class"
c.execute(sql)
ids=c.fetchall()
for i in ids:
    options.append(str(i[0])+" - "+i[1]+" - "+i[2])

def update(rows):
    for i in rows:
        tableView.insert('','end',values=i)   
def selected():
    tableView.delete(*tableView.get_children())
#     for i in tableView.get_children():
#         tableView.delete(i)
    option= ClassOption.get()
    cid = option.split(" - ")[0]
    query ="SELECT * FROM Student WHERE ClassID = '" + str(cid) + "'"
    c.execute(query)
    rows = c.fetchall()
    update(rows)

from tkinter import *
from tkinter import ttk  
from tkinter import messagebox
win=Tk()
opts=StringVar()
wrapper1=LabelFrame(win,text="<Class Option Lookup>")
wrapper1.pack(padx=10,pady=10,fill='both',expand="yes")
wrapper2=LabelFrame(win,text="<Class Detail Lookup>")
wrapper2.pack(padx=10,pady=10,fill="both", expand="yes")
tableView= ttk.Treeview(wrapper2, columns=(1,2,3,4), show="headings", height="15")
tableView.pack(padx=10,pady=20)
tableView.heading(1, text="StudentID",)
tableView.heading(2, text="StudentName")
tableView.heading(3, text="StudentAddress")
tableView.heading(4, text="ClassID")


selectButton = Button(wrapper1,font=('arial', 12, 'bold'),text="Select Class",bg="#8590F7", command=selected)
selectButton.grid(row=0,column=1,padx=0,pady=0)
ClassOption = ttk.Combobox(wrapper1,font=('arial', 11, 'bold'), textvariable=opts, width=83)
ClassOption['values'] = options
ClassOption.grid(row=0,column=0,padx=10,pady=10)
ClassOption.current(0)
#ClassOption.bind("<<ComboboxSelected>>",lookupStudent) #de tra cuu data

# lbl1=Label(wrapper2, text="StudentID")
# lbl1.grid(row=0,column=0,padx=10,pady=10)


win.geometry("850x500")
win.title("STUDENT DATABASE MANAGEMENT")
win.mainloop()
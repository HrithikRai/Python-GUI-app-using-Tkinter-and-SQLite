# A BOOK STORE GUI APP WITH TKINTER AND SQLITE- One can add,update,delete,year the records,
# Maintain information like Author, Title, Year, ISBN of a book on a standalone application.
# While working on Tkinter keep a grid sketch of frontend ready for efficient coding.

from tkinter import *
import backend
import pandas as pd

def transporter():      # Gets the data from the view function and puts it up in the list box upon view button click 
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)       # END specifies that the new list will be put in the end of the list box

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    
    def duplicate_check():
        df = pd.DataFrame(backend.view())
        if title_text.get() in list(df[1]):
            return True
        else:
            return False
        
    msg = "Please enter complete and valid details."
    if  title_text.get()=="" or author_text.get()=="" or year_text.get()=="" or ISBN_text.get()=="":   
        list1.insert(END,msg)
    else:
        if duplicate_check()==True:
            list1.insert(END,"Avoid duplicate records...")
        else:
            backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())

def get_selected_row(event):
    try:
        global target       
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        target = selected_tuple
        return target
    except IndexError: # Specify the type of error in except
        list1.insert(END,"First click view all button")
        pass
        
def update_command():
    backend.update(target[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,"Record Updated Successfully")

def delete_command():
    backend.delete(target[0])
    list1.delete(0,END)
    list1.insert(END,"Record deleted successfully...")

def close_window():
    window.destroy()
     
                 
window=Tk()
window.title("Your Book Store Inventory")
window.configure(background="pink")
    
l1 =Label(window,text="Title")
l1.grid(row=0,column=0)


l2 =Label(window,text="Author")
l2.grid(row=0,column=2)


l3 =Label(window,text="year")
l3.grid(row=1,column=0)


l4 =Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text = StringVar()
e4 = Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)

b1= Button(window,text = "View all",width = 12,command = transporter)
b1.grid(row=2,column=3)


b2= Button(window,text = "Search Entry",width = 12,command=search_command)
b2.grid(row=3,column=3)


b3= Button(window,text = "Add Entry",width = 12,command=insert_command)
b3.grid(row=4,column=3)


b4= Button(window,text = "Update",width = 12,command=update_command)
b4.grid(row=5,column=3)


b5= Button(window,text = "Delete",width = 12,command=delete_command)
b5.grid(row=6,column=3)


b6= Button(window,text = "Close",width = 12,command=close_window)
b6.grid(row=7,column=3)


window.mainloop()
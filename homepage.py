from tkinter import *
import sqlite3
import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master

        self.add = Button(text="ADD APPOINTMENT", width=20, height=2, bg='steelblue')
        self.add.place(x=300, y=340)

        self.submit = Button(text="UPDATE APPOINTMENT", width=20, height=2, bg='steelblue')
        self.submit.place(x=500, y=340)

        self.submit = Button(text="DISPLAY APPOINTMENT", width=20, height=2, bg='steelblue')
        self.submit.place(x=700, y=340)



        
    
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1400x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()

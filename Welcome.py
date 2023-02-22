#import TimeAttack
from tkinter import *
from tkinter.ttk import *
from subprocess import call

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("500x500")



# function to open a new window
# on a button click
def openNewWindow():
    master.destroy()
    call(["python", "TimeAttack.py"])
    

#background = PhotoImage(file = "Japanese-Castle-Night.jpg")
label = Label(master, text ="Time Attack", font =("Impact", 60))


label.pack(pady = 10)

btn = Button(master, text ="Start", command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
master.mainloop()

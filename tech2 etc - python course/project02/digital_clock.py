from tkinter import *			#importing modules
from tkinter.ttk import *
from time import strftime

root=Tk()				
root.title("digital clock")		#giving title name

def clock():			
    str=strftime("%I:%M:%S %p")		#time format
    label.config(text=str)	
    label.after(1000,clock)		#setting speed of seconds

label=Label(root, font=("Arial", 80), background="silver", foreground="red")	  #modifying colors
label.pack(anchor="center")
clock()										  #calling the function
mainloop()									  #running the mainloop
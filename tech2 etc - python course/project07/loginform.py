from tkinter import *
root=Tk()
#creating form
root.geometry("200x200")

#function to display submitted
def getvalue():
    print("Submitted")

#Title of form
Label(root, text="Login Form", font="ar 12 bold").grid(row=0, column=3)

#Field Name with packing
name=Label(root, text="Name").grid(row=1, column=2)
phone=Label(root, text="Phone").grid(row=2, column=2)
gender=Label(root, text="Gender").grid(row=3, column=2)
emergency=Label(root, text="Emergency").grid(row=4, column=2)

#Variable for storing values
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
checkvalue=IntVar

#Creating Text box and packing
namebox=Entry(root, textvariable=namevalue).grid(row=1,column=3)
phonebox=Entry(root, textvariable=phonevalue).grid(row=2,column=3)
genderbox=Entry(root, textvariable=gendervalue).grid(row=3,column=3)
emergencybox=Entry(root, textvariable=emergencyvalue).grid(row=4,column=3)

#Creating checkbox and packing
checkbox=Checkbutton(text="remember me?", variable=checkvalue).grid(row=5,column=3)

#submit button and packing
Button(text="Submitt", command=getvalue).grid(row=6,column=3)

root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import os

root7 = Tk()
root7.geometry('1000x750')
root7.title('Bill Payment System')
root7.resizable(0,0)
root7.config(bg='black')

os.chdir(r'C:\Users\Nikhil\Downloads\SSN\First Year\2nd Semester\Software Development Project')
#billimage=PhotoImage(Image.open('billpay.png').resize((450,400)))
billplace=Label(root7,image=PhotoImage(''),bd=0,height=400,width=450)
billplace.place(x=55,y=55)

root7.mainloop()
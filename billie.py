from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk, Image

def billinghome():
    root7 = Tk()
    root7.title('Billing system')
    root7.geometry('1000x750')
    root7.resizable(0,0)
    root7.config(bg='Black')

    billimg = Image.open('billsystem.jpg')
    billtk = ImageTk.PhotoImage(billimg)
    billlabel = Label(root7, image=billtk, height=750, width=1000)
    billlabel.place(x=0,y=50)

    def paymentwindow():
        root7.destroy()
        payment()

    Topframe=Frame(root7,bg='black',width=1000,height=100)
    Topframe.place(x=0,y=0)

    #Introtext = Label(Topframe,text='SRI SWAMINATH CAFE NEW',font=('Copperplate Gothic Bold',30,'bold','italic')
      #                    ,bg='black',fg='white',activebackground='black')
    #Introtext.place(x=120,y=10,width=750)

    detailframe = Frame(root7, bg='black', width=500, height=400)
    detailframe.place(x=50, y=200)

    billtitle = Label(detailframe, text='BILL PAYMENT', font=('Rockwell',36, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    billtitle.place(x=70, y=20)

    seatno = Label(detailframe, text='ENTER THE SEAT NUMBER', font=('Copperplate Gothic Bold', 22, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    seatno.place(x=20, y=170)
    seatnoentry = Entry(detailframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    seatnoentry.place(x=140, y=220, width=200)

    getdetbutton = Button(detailframe, text='GET DETAILS', command=paymentwindow,font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                              cursor="hand2", bg="blue", fg="white", activebackground='blue')
    getdetbutton.place(x=135, y=290)

    root7.mainloop()

def payment():
    root8 = Tk()
    root8.title('Billing system')
    root8.geometry('1000x750')
    root8.resizable(0, 0)
    root8.config(bg='Black')

    billimg = Image.open('billsystem.jpg')
    billtk = ImageTk.PhotoImage(billimg)
    billlabel = Label(root8, image=billtk, height=750, width=1000)
    billlabel.place(x=0, y=50)

    Topframe = Frame(root8, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    # Introtext = Label(Topframe,text='SRI SWAMINATH CAFE NEW',font=('Copperplate Gothic Bold',30,'bold','italic')
    #                    ,bg='black',fg='white',activebackground='black')
    # Introtext.place(x=120,y=10,width=750)
    bodyframe = Frame(root8, bg='black', width=650, height=550)
    bodyframe.place(x=150,y=150)

    billtitle = Label(bodyframe, text='BILL PAYMENT', font=('Rockwell', 36, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    billtitle.place(x=150, y=20)

    cusname = Label(bodyframe, text='CUSTOMER NAME :', font=("Copperplate Gothic Bold", 18, "bold")
                      , bg='black', fg='white', activebackground='black')
    cusname.place(x=20,y=160)

    cusmobileno = Label(bodyframe, text='MOBILE NUMBER  :', font=("Copperplate Gothic Bold", 18, "bold")
                    , bg='black', fg='white', activebackground='black')
    cusmobileno.place(x=20, y=210)

    cusseatno = Label(bodyframe, text='SEAT NUMBER :', font=("Copperplate Gothic Bold", 18, "bold")
                    , bg='black', fg='white', activebackground='black')
    cusseatno.place(x=20, y=260)

    billamt = Label(bodyframe, text='ENTER THE BILL AMOUNT TO BE PAID :', font=("Copperplate Gothic Bold", 18, "bold")
                    , bg='black', fg='white', activebackground='black')
    billamt.place(x=20, y=360)
    addinfo = Label(bodyframe, text='(Inclusive of all taxes) ', font=("Copperplate Gothic Bold", 15, "bold")
                    , bg='black', fg='white', activebackground='black')
    addinfo.place(x=20, y=390)

    billamtentry = Entry(bodyframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    billamtentry.place(x=220, y=430, width=200)

    def resetfield():
        billamtentry.delete(0,END)

    def successwindow():
        messagebox.showinfo('Success!', 'The amount for the bill has been paid successfully')
        resetfield()
        root8.destroy()

    paybillbutton = Button(bodyframe, text='PAY BILL', command=successwindow,font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                          cursor="hand2", bg="red", fg="white", activebackground='red')
    paybillbutton.place(x=245, y=485)

    root8.mainloop()

billinghome()
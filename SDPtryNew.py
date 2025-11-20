from tkinter import *
from tkinter import messagebox, ttk
import csv
from PIL import Image, ImageTk
from customtkinter import *

global ue
global order
order = 1

two_seats = ["2A", "2B", "2C", "2D"]
four_seats = ["4A", "4B", "4C", "4D"]
six_seats = ["6A", "6B", "6C"]
eight_seats = ["8A", "8B", "8C"]

seat_choices={}

class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return self.queue

    def dequeue(self):
        x = self.queue[0]
        del self.queue[0]
        return x

q = queue()
print(q.queue)

def seatchooser():
    def stretch(event):
        global resized_tk
        width = event.width
        height = event.height
        resized_image = image_original.resize((width, height))  # Corrected resizing
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas1.create_image(0, 0, image=resized_tk, anchor="nw")

    root4 = Tk()
    root4.title("Customer View")
    root4.geometry('1500x800')
    root4.resizable(0, 0)
    root4.config(bg='black')
    # Set the size of the window to fill the entire screen without hiding the title bar
    root4.wm_attributes('-fullscreen', False)
    root4.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
    root4.rowconfigure(0, weight=1)

    image_original = Image.open("Customerbg.jpg")
    image_tk = ImageTk.PhotoImage(image_original)

    canvas1 = Canvas(root4, background="black", bd=0, highlightthickness=0, relief="ridge")
    canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
    canvas1.create_image((0, 0), image=image_tk, anchor="nw")
    canvas1.bind("<Configure>", stretch)

    def resetfield():
        seats.delete(0,END)

    # ADD TABLES IMAGES
    # 2seat and labels of availability

    img_2 = Image.open("2seat.png")
    img_2_resized = img_2.resize((150, 150))  # Corrected resizing
    img_2_tk = ImageTk.PhotoImage(img_2_resized)

    seat1 = Label(root4, image=img_2_tk)
    seat1.place(x=75, y=160)

    label2_1 = Label(root4, text="2A", background="green" if "2A" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label2_1.place(x=75, y=314, width=154)
    

    seat2 = Label(root4, image=img_2_tk)
    seat2.place(x=275, y=160)

    label2_2 = Label(root4, text="2B", background="green" if "2B" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label2_2.place(x=275, y=314, width=154)

    seat_3 = Label(root4, image=img_2_tk)
    seat_3.place(x=475, y=160)

    label2_3 = Label(root4, text="2C", background="green" if "2C" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label2_3.place(x=475, y=314, width=154)

    seat4 = Label(root4, image=img_2_tk)
    seat4.place(x=675, y=160)

    label2_4 = Label(root4, text="2D", background="green" if "2D" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label2_4.place(x=675, y=314, width=154)


    # 4seat

    img2 = ImageTk.PhotoImage(Image.open("4seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img2)
    seat1.place(x=75, y=390)

    label4_1 = Label(root4, text="4A", background="green" if "4A" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label4_1.place(x=75, y=544, width=154)

    seat2 = Label(root4, image=img2)
    seat2.place(x=275, y=390)

    label4_2 = Label(root4, text="4B", background="green" if "4B" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label4_2.place(x=275, y=544, width=154)

    seat3 = Label(root4, image=img2)
    seat3.place(x=475, y=390)

    label4_3 = Label(root4, text="4C", background="green" if "4C" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label4_3.place(x=475, y=544, width=154)

    seat4 = Label(root4, image=img2)
    seat4.place(x=675, y=390)

    label4_4 = Label(root4, text="4D", background="green" if "4D" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label4_4.place(x=675, y=544, width=154)

    # 6seat
    img3 = ImageTk.PhotoImage(Image.open("6seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img3)
    seat1.place(x=875, y=160)

    label6_1 = Label(root4, text="6A", background="green" if "6A" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label6_1.place(x=875, y=314, width=154)

    seat2 = Label(root4, image=img3)
    seat2.place(x=1075, y=160)

    label6_2 = Label(root4, text="6B", background="green" if "6B" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label6_2.place(x=1075, y=314, width=154)

    seat3 = Label(root4, image=img3)
    seat3.place(x=1275, y=160)

    label6_3 = Label(root4, text="6C", background="green" if "6C" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label6_3.place(x=1275, y=314, width=154)

    # 8seat

    img4 = ImageTk.PhotoImage(Image.open("8seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img4)
    seat1.place(x=875, y=390)

    label8_1 = Label(root4, text="8A", background="green" if "8A" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label8_1.place(x=875, y=544, width=154)

    seat2 = Label(root4, image=img4)
    seat2.place(x=1075, y=390)

    label8_2 = Label(root4, text="8B", background="green" if "8B" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label8_2.place(x=1075, y=544, width=154)

    seat3 = Label(root4, image=img4)
    seat3.place(x=1275, y=390)

    label8_3 = Label(root4, text="8C", background="green" if "8C" not in seat_choices else "red", fg='white', font=('Calibri', 20, 'bold'))
    label8_3.place(x=1275, y=544, width=154)

    headingframe = Frame(root4, bg='black', width=1500, height=130)
    headingframe.place(x=0, y=0)
    Introtext = Label(headingframe, text='SRI SWAMINATH CAFE NEW',
                      font=('Calibri', 60, 'bold')
                      , bg='black', fg='white', activebackground='black')
    Introtext.place(x=150, y=10, width=1200)

    # notes for colour identification
    note_label = Label(root4, text="NOTE!", bg="black", font=("new times roman", 13), fg="white").place(x=10, y=10)
    red = Label(root4, text="Red: Booked", bg="red", font=("new times roman", 13)).place(x=10, y=34)

    detailsframe = Frame(root4, bg='black',width=1500, height=200)
    detailsframe.place(x=0,y=625)
    
    #update the function
    def update(s,label,root):
        if label:
            label.config(bg="red")
            root.destroy()
            resetfield()
        resetfield()
    # create a function for booked successfully page
    def book():
        root_success=Toplevel(root4)
        root_success.title("Customer Seat Booking Confirmation Window")
        root_success.geometry('450x285')
        root_success.resizable(0,0)

        def stretch(event):
                global resized_tk
                global order
                width = event.width
                height = event.height
                resized_image = image_original.resize((width, height))  # Corrected resizing
                resized_tk = ImageTk.PhotoImage(resized_image)
                canvas1.create_image(0, 0, image=resized_tk, anchor="nw")

        image_original = Image.open("customerbg.jpg")
        image_tk = ImageTk.PhotoImage(image_original)
        canvas1 = Canvas(root_success, background="black", bd=0, highlightthickness=0, relief="ridge")
        canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
        canvas1.create_image((0, 0), image=image_tk, anchor="nw")
        canvas1.bind("<Configure>", stretch)

        seats_no=seats.get()
        seats_no=int(seats_no)
        s=None
        if seats_no:
            if 0 < seats_no<=2:
                if two_seats:
                    s=two_seats.pop(0)
                    if s=="2A":
                        label=label2_1
                    elif s=="2B":
                        label=label2_2
                    elif s=="2C":
                        label=label2_3
                    elif s=="2D":
                        label=label2_4

                else:
                    root_success.destroy()
                    messagebox.showinfo("NOTE","Two seater tables are Empty!")
                    resetfield()

            elif 2 < seats_no <=4:
                if four_seats:
                    s=four_seats.pop(0)
                    if s=="4A":
                        label=label4_1
                    elif s=="4B":
                        label=label4_2
                    elif s=="4C":
                        label=label4_3
                    elif s=="4D":
                        label=label4_4
                else:
                    root_success.destroy()
                    messagebox.showinfo("NOTE","Four seater Tables are Empty!")
                    resetfield()

            elif 4 < seats_no <= 6:
                if six_seats:
                    s=six_seats.pop(0)
                    if s=="6A":
                        label=label6_1
                    elif s=="6B":
                        label=label6_2
                    elif s=="6C":
                        label=label6_3
                else:
                    root_success.destroy()
                    messagebox.showinfo("NOTE","Six seater Tables are Empty!")
                    resetfield()

            elif 6 < seats_no <=8:
                if eight_seats:
                    s=eight_seats.pop(0)
                    if s=="8A":
                        label=label8_1
                    elif s=="8B":
                        label=label8_2
                    elif s=="8C":
                        label=label8_3
                else:
                    root_success.destroy()
                    messagebox.showinfo("NOTE","Eight seater Tables are Empty!")
                    resetfield()

            elif 0 > seats_no  or seats_no> 8:
                root_success.destroy()
                messagebox.showerror("ERROR!","Seats Available less than 8 per table only!!!")
                resetfield()
            if s:
                if s not in seat_choices.values():
                    data = q.queue[-1]
                    seat_choices[s] = data
                    # STORE THE DATA FOR UPDATING PURPOSES I.E:COLOUR
                    # Update the label color to red



        label_booked = CTkLabel(root_success,text="Dear "+ue+",\nYour table has been\nsuccessfully booked!\n Table no:"+str(s) , fg_color="green", width=400, height=50, font=("New Times Roman",24,'bold'),
                                    corner_radius=0, bg_color="black", text_color="white", anchor=N)
        label_booked.place(x=25, y=70)

        refresh_button=Button(root_success,text="Refresh!",font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                         bg="red", fg="white", activebackground='red',command=lambda : update(s,label,root_success))
        refresh_button.place(x=140, y=205)
        print(q.queue)
        print(seat_choices)

        root_success.mainloop()



    # enter to book

    noofseatslabel = Label(detailsframe, text="Enter the number of seats", background="black", fg='white', font=('Copperplate Gothic Bold', 20, 'bold'))
    noofseatslabel.place(x=550,y=10)

    Nameframe = Label(detailsframe, text='Welcome, '+ue, font=("Copperplate Gothic Bold", 20, 'bold'), bg='black', fg='white')
    Nameframe.place(x=60, y=10)

    seats = Entry(detailsframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    seats.place(x=625, y=50)

    book = Button(detailsframe, text="Book",font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2", fg="white",bg='blue',activebackground='blue', command=book)
    book.place(x=715, y=95)

    def loginpageaction():
        root4.destroy()
        introscreen()

    Loginbutton = Button(detailsframe, text='Back to Login Page', command=loginpageaction,font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                         bg="#FF006A", fg="white", activebackground='#FF006A')
    Loginbutton.place(x=1130, y=100)

    root4.mainloop()

def managerview():
    class Table:
        def __init__(self, root, lst):
            self.style = ttk.Style()
            self.style.theme_use("default")
            self.style.configure("Treeview",background="grey", foreground="black",rowheight=30,
                                 fieldbackground="silver",font=("times new roman", 16))
            self.style.configure("Treeview.Heading", font=("times new roman", 18))
            self.style.map("Treeview", background=[('selected', 'green')])

            self.tree = ttk.Treeview(root, columns=("S.No", "Name", "Phone number", "Alloted seats"), show="headings")
            self.tree.heading("S.No", text="S.No")
            self.tree.heading("Name", text="Name of the customer")
            self.tree.heading("Phone number", text="Phone number")
            self.tree.heading("Alloted seats", text="Alloted seats")
            self.tree.place(x=150, y=200)

            # Insert data into the treeview
            for i, row in enumerate(lst, start=1):
                self.tree.insert("", "end", values=(i, *row))

            # Center-align all cells
            for col in self.tree["columns"]:
                self.tree.column(col, anchor="center")

    root5 = Tk()
    root5.title("Customer")
    width = root5.winfo_screenwidth()
    height = root5.winfo_screenheight()

    # Set the size of the window to fill the entire screen without hiding the title bar
    root5.geometry("%dx%d" % (width, height))
    root5.wm_attributes('-fullscreen', False)

    image_original = Image.open("manager.jpg")
    image_tk = ImageTk.PhotoImage(image_original)

    canvas1 = Canvas(root5, background="black", bd=0, highlightthickness=0, relief="ridge")
    canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
    canvas1.create_image((0, 0), image=image_tk, anchor="nw")

    # take the data
    lst = [("Raj", "8263427232", "1A"),
           ("Aaryan", "34534343434", "4B"),
           ("Vaishnavi", "3434342323", '1D'),
           ("Rachna", "789888767", "3B"),
           ("Shubham", "656577685", "2C")]

    t = Table(root5, lst)

    # Manviewframe = Frame(root5, bg='black', width=450, height=900)
    # Manviewframe.place(x=1100, y=0)

    manager = Label(root5, text="Name :xxxxxx", font=("times new roman", 25), bg="grey").place(x=1230, y=450)
    id = Label(root5, text="ID :YYYYY", font=("times new roman", 25), bg="grey").place(x=1230, y=500)

    def loginpageaction():
        root5.destroy()
        introscreen()

    def billpayaction():
        root5.destroy()
        billpayment()

    Billpaybutton = Button(root5, text='Pay Bill', command=billpayaction,
                           font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                           bg="green", fg="white", activebackground='green')
    Billpaybutton.place(x=1250, y=630)

    Loginbutton = Button(root5, text='Back to Login Page', command=loginpageaction,
                         font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                         bg="green", fg="white", activebackground='green')
    Loginbutton.place(x=1150, y=700)

    root5.mainloop()


def billpayment():
    def billinghome():
        root7 = Tk()
        root7.title('Billing system')
        root7.geometry('1000x750')
        root7.resizable(0, 0)
        root7.config(bg='Black')

        billimg = Image.open('billsystem.jpg')
        billtk = ImageTk.PhotoImage(billimg)
        billlabel = Label(root7, image=billtk, height=750, width=1000)
        billlabel.place(x=0, y=50)

        def resetfield():
            seatnoentry.delete(0, END)

        def billentry():
            se = seatnoentry.get()

            if se=='':
                messagebox.showinfo('Error!', 'Enter a valid seat number!')
                resetfield()

            elif se in two_seats or se in four_seats or se in six_seats or se in eight_seats:
                paymentwindow()
                resetfield()

            else:
                messagebox.showinfo('Error!', 'The entered seat number does not exist!')
                resetfield()

        def paymentwindow():
            root7.destroy()
            payment()

        Topframe = Frame(root7, bg='black', width=1000, height=100)
        Topframe.place(x=0, y=0)

        Introtext = Label(Topframe,text='SRI SWAMINATH CAFE NEW',font=('Copperplate Gothic Bold',30,'bold','italic')
                            ,bg='black',fg='white',activebackground='black')
        Introtext.place(x=120,y=10,width=750)

        detailframe = Frame(root7, bg='black', width=500, height=400)
        detailframe.place(x=50, y=200)

        billtitle = Label(detailframe, text='BILL PAYMENT', font=('Rockwell', 36, 'bold', 'italic')
                          , bg='black', fg='white', activebackground='black')
        billtitle.place(x=70, y=20)

        seatno = Label(detailframe, text='ENTER THE SEAT NUMBER', font=('Copperplate Gothic Bold', 22, 'bold', 'italic')
                       , bg='black', fg='white', activebackground='black')
        seatno.place(x=20, y=170)
        seatnoentry = Entry(detailframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
        seatnoentry.place(x=140, y=220, width=200)

        getdetbutton = Button(detailframe, text='GET DETAILS', command=billentry,
                              font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
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

        Introtext = Label(Topframe,text='SRI SWAMINATH CAFE NEW',font=('Copperplate Gothic Bold',30,'bold','italic')
                            ,bg='black',fg='white',activebackground='black')
        Introtext.place(x=120,y=10,width=750)
        bodyframe = Frame(root8, bg='black', width=650, height=550)
        bodyframe.place(x=150, y=150)

        billtitle = Label(bodyframe, text='BILL PAYMENT', font=('Rockwell', 36, 'bold', 'italic')
                          , bg='black', fg='white', activebackground='black')
        billtitle.place(x=150, y=20)

        cusname = Label(bodyframe, text='CUSTOMER NAME :', font=("Copperplate Gothic Bold", 18, "bold")
                        , bg='black', fg='white', activebackground='black')
        cusname.place(x=20, y=160)

        cusmobileno = Label(bodyframe, text='MOBILE NUMBER  :', font=("Copperplate Gothic Bold", 18, "bold")
                            , bg='black', fg='white', activebackground='black')
        cusmobileno.place(x=20, y=210)

        cusseatno = Label(bodyframe, text='SEAT NUMBER :', font=("Copperplate Gothic Bold", 18, "bold")
                          , bg='black', fg='white', activebackground='black')
        cusseatno.place(x=20, y=260)

        billamt = Label(bodyframe, text='ENTER THE BILL AMOUNT TO BE PAID :',
                        font=("Copperplate Gothic Bold", 18, "bold")
                        , bg='black', fg='white', activebackground='black')
        billamt.place(x=20, y=360)
        addinfo = Label(bodyframe, text='(Inclusive of all taxes) ', font=("Copperplate Gothic Bold", 15, "bold")
                        , bg='black', fg='white', activebackground='black')
        addinfo.place(x=20, y=390)

        billamtentry = Entry(bodyframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
        billamtentry.place(x=220, y=430, width=200)

        def resetfield():
            billamtentry.delete(0, END)

        def successwindow():
            messagebox.showinfo('Success!', 'The amount for the bill has been paid successfully!')
            resetfield()
            root8.destroy()
            managerview()

        paybillbutton = Button(bodyframe, text='PAY BILL', command=successwindow,
                               font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                               cursor="hand2", bg="red", fg="white", activebackground='red')
        paybillbutton.place(x=245, y=485)

        root8.mainloop()

    billinghome()


def customersystem():
    global userentry
    root2 = Tk()
    root2.geometry('1000x750')
    root2.title('Customer Entry')
    root2.resizable(0, 0)
    root2.config(bg='black')

    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root2, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    Topframe = Frame(root2, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    Toptext = Label(root2, text='ENTER THE DETAILS OF THE CUSTOMER', font=('Rockwell', 32, 'bold')
                    , bg='black', fg='white', activebackground='black')
    Toptext.place(x=60, y=10, width=900)

    def resetfield():
        userentry.delete(0, END)
        phoneentry.delete(0, END)

    def cusentry():
        global ue,order
        ue = userentry.get()
        pe = phoneentry.get()

        if ue == '' or pe == '':
            messagebox.showinfo('Error', 'Enter all the required values')
            resetfield()
        elif pe.isdigit() != True:
            messagebox.showinfo('Error', 'Enter a valid phone number')
            resetfield()
        elif (pe.isdigit() and len(pe) != 10) or str(pe)[0] == '0':
            messagebox.showinfo('Error', 'Enter a valid phone number')
            resetfield()
        else:
            c = 0
            q.enqueue([order,ue,pe])
            cusfile = open('Customer.csv', 'a', newline='')
            cuswriter = csv.writer(cusfile, delimiter=',')
            nl = [order, ue, pe]
            order += 1
            cuswriter.writerow(nl)
            messagebox.showinfo('Customer Details', 'Details noted down successfully')
            resetfield()
            cusfile.close()
            root2.destroy()
            seatchooser()

    Cusloginframe = Frame(root2, bg='black', width=450, height=400)
    Cusloginframe.place(x=300, y=200)

    Submitbutton = Button(Cusloginframe, text='Submit', command=cusentry, font=("Copperplate Gothic Bold", 20, "bold"),
                          bd=0, cursor="hand2",
                          bg="green", fg="white", activebackground='green')
    Submitbutton.place(x=160, y=300)

    usertext = Label(Cusloginframe, text='Name of the customer', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    usertext.place(x=14, y=50)
    phonetext = Label(Cusloginframe, text='Phone Number', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    phonetext.place(x=14, y=170)

    userentry = Entry(Cusloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    userentry.place(x=14, y=110, width=410)
    phoneentry = Entry(Cusloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    phoneentry.place(x=14, y=230, width=410)

    root2.mainloop()


def mansignup():
    root3.destroy()
    root6 = Tk()
    root6.geometry('1000x750')
    root6.title('Manager Sign Up')
    root6.resizable(0, 0)
    root6.config(bg='black')

    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root6, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    Topframe = Frame(root6, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    Toptext = Label(root6, text='ENTER THE DETAILS OF THE NEW MANAGER', font=('Rockwell', 28, 'bold')
                    , bg='black', fg='white', activebackground='black')
    Toptext.place(x=20, y=10, width=950)

    def resetfield():
        nameentry.delete(0, END)
        emailentry.delete(0, END)
        passentry.delete(0, END)

    def mandetails():
        ne = nameentry.get()
        ee = emailentry.get()
        pe = passentry.get()

        if ne == '' or ee == '' or pe == '':
            messagebox.showinfo('Error', 'Enter all the required values')
            resetfield()
        else:
            c = 0
            manfile = open('Manager.csv', 'a', newline='')
            manwriter = csv.writer(manfile, delimiter=',')
            nl = [ne, ee, pe]
            manwriter.writerow(nl)
            messagebox.showinfo('Manager Details', 'Account created successfully')
            resetfield()
            manfile.close()
            root6.destroy()
            managersystem()

    Mansignupframe = Frame(root6, bg='black', width=450, height=500)
    Mansignupframe.place(x=250, y=170)

    Createbutton = Button(Mansignupframe, text='Create Account', command=mandetails,
                          font=("Copperplate Gothic Bold", 20, "bold"), bd=0,
                          cursor="hand2", bg="green", fg="white", activebackground='green')
    Createbutton.place(x=80, y=420)

    nametext = Label(Mansignupframe, text='Name of the manager', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    nametext.place(x=20, y=50)
    emailtext = Label(Mansignupframe, text='Email ID', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    emailtext.place(x=20, y=170)
    passtext = Label(Mansignupframe, text='Password', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    passtext.place(x=20, y=290)

    nameentry = Entry(Mansignupframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    nameentry.place(x=20, y=110, width=410)
    emailentry = Entry(Mansignupframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    emailentry.place(x=20, y=230, width=410)
    passentry = Entry(Mansignupframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black', show="*")
    passentry.place(x=20, y=350, width=410)

    root6.mainloop()


def managersystem():
    global root3
    root3 = Tk()
    root3.geometry('1000x750')
    root3.title('Manager Entry')
    root3.resizable(0, 0)
    root3.config(bg='black')

    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root3, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    Topframe = Frame(root3, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    Toptext = Label(root3, text='ENTER THE DETAILS OF THE MANAGER', font=('Rockwell', 32, 'bold')
                    , bg='black', fg='white', activebackground='black')
    Toptext.place(x=20, y=10, width=950)

    def resetfield():
        nameentry.delete(0, END)
        emailentry.delete(0, END)
        passentry.delete(0, END)

    def manentry():
        ne = nameentry.get()
        ee = emailentry.get()
        pe = passentry.get()

        if ne == '' or ee == '' or pe == '':
            messagebox.showinfo('Error', 'Enter all the required values')
            resetfield()
        else:
            manfile = open('Manager.csv', 'r', newline='')
            manreader = csv.reader(manfile, delimiter=',')
            for i in manreader:
                if i[0] == 'Name of the Manager':
                    continue
                else:
                    if ne == i[0] and ee == i[1] and pe == i[2]:
                        messagebox.showinfo('Manager Details', 'Login successful')
                        resetfield()
                        manfile.close()
                        root3.destroy()
                        managerview()
                        break
            else:
                messagebox.showinfo('Error', 'One or more fields do not match properly')
                resetfield()

    Manloginframe = Frame(root3, bg='black', width=500, height=550)
    Manloginframe.place(x=250, y=180)

    Submitbutton = Button(Manloginframe, text='Submit', command=manentry, font=("Copperplate Gothic Bold", 20, "bold"),
                          bd=0,
                          cursor="hand2", bg="green", fg="white", activebackground='green')
    Submitbutton.place(x=180, y=410)

    createacctbutton = Button(Manloginframe, text='New Manager? Create account', command=mansignup,
                              font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                              cursor="hand2", bg="blue", fg="white", activebackground='blue')
    createacctbutton.place(x=10, y=480)

    nametext = Label(Manloginframe, text='Name of the manager', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    nametext.place(x=20, y=50)
    emailtext = Label(Manloginframe, text='Email ID', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    emailtext.place(x=20, y=170)
    passtext = Label(Manloginframe, text='Password', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    passtext.place(x=20, y=290)

    nameentry = Entry(Manloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    nameentry.place(x=20, y=110, width=410)
    emailentry = Entry(Manloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    emailentry.place(x=20, y=230, width=410)
    passentry = Entry(Manloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black', show="*")
    passentry.place(x=20, y=350, width=410)

    root3.mainloop()


def introscreen():
    root1 = Tk()
    root1.geometry('1000x750')
    root1.title('Login Page')
    root1.resizable(0, 0)
    root1.config(bg='black')

    def customerlogin():
        root1.destroy()
        customersystem()

    def managerlogin():
        root1.destroy()
        managersystem()

    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root1, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    Topframe = Frame(root1, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    Introtext = Label(Topframe, text='Welcome to Sri Swaminath Cafe New',
                      font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    Introtext.place(x=120, y=10, width=750)
    Bottomtext = Label(Topframe, text='Experience the delicacies of South India at the right price',
                       font=('Copperplate Gothic Bold', 18, 'bold', 'italic')
                       , bg='black', fg='white', activebackground='black')
    Bottomtext.place(x=50, y=60, width=900)

    Loginframe = Frame(root1, bg='black', width=400, height=400)
    Loginframe.place(x=300, y=200)

    Loginframetext = Label(Loginframe, text='LOGIN AS', font=('Rockwell', 32, 'bold'), bg='black', fg='white',
                           activebackground='black')
    Loginframetext.place(x=80, y=30, width=250)

    customerbutton = Button(Loginframe, text='Customer', command=customerlogin, font=('Rockwell', 24, 'bold'),
                            cursor='hand2', bd=0, bg='blue', fg='white', activebackground='blue')
    customerbutton.place(x=80, y=140, width=250)

    managerbutton = Button(Loginframe, text='Hotel Manager', command=managerlogin, font=('Rockwell', 24, 'bold'),
                           cursor='hand2', bd=0, bg='red', fg='white', activebackground='red')
    managerbutton.place(x=80, y=260, width=250)

    root1.mainloop()

introscreen()
print(seat_choices)
#Importing all the necessary modules
from tkinter import *
from tkinter import messagebox, ttk
import csv
from PIL import Image, ImageTk
from customtkinter import *
import ast
import re
import full_mail

#Making variables global to make use of them over the whole program
global seat_choices
global ue
global ne
global ee
global se
global pe
global order
order = 1

#Usage of data structures starts here
two_seats = ["2A", "2B", "2C", "2D"]
four_seats = ["4A", "4B", "4C", "4D"]
six_seats = ["6A", "6B", "6C"]
eight_seats = ["8A", "8B", "8C"]

#Creation of dictionary to store the data of the customer and their seat number
seat_choices={}

#Queue data structure's implementation
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
seat_choices={}
def load_state(filename='state.csv'):
    global two_seats,four_seats,six_seats,eight_seats,seat_choices

    """
    Read seat choices dictionary from a CSV file.

    Parameters:
    - filename: Name of the CSV file to read from. Default is 'state.csv'.

    Returns:
    - seat_choices: Dictionary containing seat choices data.
    """
    seat_choices = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 2:
                print("Error: Insufficient data in row:", row)
                continue
            seat_choices[row[0]] = ast.literal_eval(row[1])
    
        # Update seat lists based on seat_choices
    two_seats = ["2A", "2B", "2C", "2D"]
    four_seats = ["4A", "4B", "4C", "4D"]
    six_seats = ["6A", "6B", "6C"]
    eight_seats = ["8A", "8B", "8C"]
    for seat in list(seat_choices.keys()):
        if seat in two_seats:
            two_seats.remove(seat)
        elif seat in four_seats:
            four_seats.remove(seat)
        elif seat in six_seats:
            six_seats.remove(seat)
        elif seat in eight_seats:
            eight_seats.remove(seat)

    
load_state()
#The "Customer Point of View" window
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
    Introtext = Label(headingframe, text='SRI SWAMINATH CAFE NEW', font=('Calibri', 60, 'bold'), bg='black', fg='white', activebackground='black')
    Introtext.place(x=150, y=10, width=1200)

    # notes for colour identification
    note_label = Label(root4, text="NOTE!", bg="black", font=("new times roman", 13), fg="white").place(x=10, y=10)
    green = Label(root4, text="Green : Available", bg="green", font=("new times roman", 13), fg="white").place(x=10, y=35)
    red = Label(root4, text="Red : Booked", bg="red", font=("new times roman", 13), fg="white").place(x=10, y=65)

    detailsframe = Frame(root4, bg='black',width=1500, height=200)
    detailsframe.place(x=0,y=625)
    
    #update the function
    def update(s,label,root):
        if label:
            label.config(bg="red")
            with open("Seat1.txt", 'w') as a:
             for i, j in seat_choices.items():
                if ee in j:
                    a.write(i)
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
        if seats_no>0:
            if 1 <= seats_no<=2:
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
                    messagebox.showerror("NOTE","Two seater tables are Empty!")
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
                    messagebox.showerror("NOTE","Four seater Tables are Empty!")
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
                    messagebox.showerror("NOTE","Six seater Tables are Empty!")
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
                    messagebox.showerror("NOTE","Eight seater Tables are Empty!")
                    resetfield()

            elif 0 > seats_no  or seats_no> 8:
                root_success.destroy()
                messagebox.showerror("ERROR!","Seats Available less than 8 per table only!!!")
                resetfield()
            if s:
                if s not in seat_choices.values():
                    data = q.queue[-1]
                    seat_choices[s] = data
        if seats_no == 0:
            root_success.destroy()
            messagebox.showerror("ERROR!", "Enter valid number of seats!!!")
            resetfield()
                    
                    # STORE THE DATA FOR UPDATING PURPOSES I.E:COLOUR
                    # Update the label color to red

        label_booked = CTkLabel(root_success,text="Dear "+ue+",\nYour table has been\nsuccessfully booked!\n Table no : "+str(s) , fg_color="green", width=400, height=50, font=("New Times Roman",24,'bold'),
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
        save_state(seat_choices)
        root4.destroy()
        introscreen()
        full_mail.send_email(ee)
        full_mail.send_email_admin("Sriswaminathcafe4@gmail.com"
                                           ""
                                           "")

    Loginbutton = Button(detailsframe, text='Back to Login Page', command=loginpageaction,font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                         bg="#FF006A", fg="white", activebackground='#FF006A')
    Loginbutton.place(x=1130, y=100)

    root4.mainloop()

def manager_view():
    global ne
    global ee
    class Table:
        def __init__(self, root, lst):
            self.style = ttk.Style()
            self.style.theme_use("default")
            self.style.configure("Treeview",background="grey", foreground="black",rowheight=30,
                                 fieldbackground="silver",font=("times new roman", 16))
            self.style.configure("Treeview.Heading", font=("times new roman", 18))
            self.style.map("Treeview", background=[('selected', 'green')])

            self.tree = ttk.Treeview(root, columns=("Order No", "Name", "Phone number", "Alloted seats"), show="headings")
            self.tree.heading("Order No", text="Order No")
            self.tree.heading("Name", text="Name of customer")
            self.tree.heading("Phone number", text="Phone number")
            self.tree.heading("Alloted seats", text="Alloted seats")
            self.tree.place(x=150, y=200)

            #Insert data into the treeview
            for row in listdata:
                self.tree.insert("", "end", values=(row))

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
    listdata = []
    for i in seat_choices:
        listdata.append((seat_choices[i][0],seat_choices[i][1],seat_choices[i][2],i))
    print(listdata)

    t = Table(root5, listdata)

    def update_manager_info(manager_name, manager_id):
        # Update manager information labels
        manager.config(text=f"Name: {manager_name}")
        #id.config(text=f"ID: {manager_id}")

    # Initial manager info (replace with actual data or default values)
    manager_name = ne
    manager_id = ee

    manager = Label(root5, text=f"Name: {manager_name}", font=("times new roman", 25), bg="grey")
    manager.place(x=1125, y=450)
    id = Label(root5, text=f"ID: {manager_id}", font=("times new roman", 25), bg="grey")
    id.place(x=1125, y=500)

    def set_manager_info(new_manager_name, new_manager_id):
        nonlocal manager_name, manager_id
        manager_name = new_manager_name
        manager_id = new_manager_id
        update_manager_info(manager_name, manager_id)

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

    Homebutton = Button(root5, text='Back to Login Page', command=loginpageaction,
                         font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                         bg="#FF006A", fg="white", activebackground='#FF006A')
    Homebutton.place(x=1150, y=700)

    root5.mainloop()



def billpayment():
    # Function to display the billing home screen
    def billinghome():
        global se
        root7 = Tk()
        root7.title('Billing system')
        root7.geometry('1000x750')
        root7.resizable(0, 0)
        root7.config(bg='Black')

        # Load and display the background image
        billimg = Image.open('billsystem.jpg')
        billtk = ImageTk.PhotoImage(billimg)
        billlabel = Label(root7, image=billtk, height=750, width=1000)
        billlabel.place(x=0, y=50)

        # Function to reset the seat number entry field
        def resetfield():
            try:
                seatnoentry.delete(0, END)
            except TclError:
                pass

        # Function to handle bill entry
        def billentry():
            global se
            se = seatnoentry.get()

            if se == '':
                messagebox.showerror('Error !', 'Enter a valid seat number !')
                resetfield()
            elif se in seat_choices.keys():
                paymentwindow(se)
                resetfield()
            else:
                messagebox.showerror('Error !', 'The entered seat number does not exist !')
                resetfield()

        # Function to display the payment window
        def paymentwindow(se):
            root7.destroy()
            payment(seat_choices[se][1], seat_choices[se][2], se)

        # Top frame and text for the billing home screen
        Topframe = Frame(root7, bg='black', width=1000, height=100)
        Topframe.place(x=0, y=0)

        Introtext = Label(Topframe, text='SRI SWAMINATH CAFE NEW', font=('Copperplate Gothic Bold', 30, 'bold', 'italic')
                          , bg='black', fg='white', activebackground='black')
        Introtext.place(x=120, y=10, width=750)

        # Detail frame for entering seat number
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

        # Button to get seat details
        getdetbutton = Button(detailframe, text='GET DETAILS', command=billentry,
                              font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                              cursor="hand2", bg="blue", fg="white", activebackground='blue')
        getdetbutton.place(x=135, y=280)

        # Button to go back to login page
        def loginpageaction():
            root7.destroy()
            introscreen()

        Homebutton = Button(detailframe, text='Back to Login Page', command=loginpageaction,
                            font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                            bg="#FF006A", fg="white", activebackground='#FF006A')
        Homebutton.place(x=75, y=340)

        root7.mainloop()

    # Function to handle the payment process
    def payment(ue, pe, se):
        root8 = Tk()
        root8.title('Billing system')
        root8.geometry('1000x750')
        root8.resizable(0, 0)
        root8.config(bg='Black')

        # Load and display the background image
        billimg = Image.open('billsystem.jpg')
        billtk = ImageTk.PhotoImage(billimg)
        billlabel = Label(root8, image=billtk, height=750, width=1000)
        billlabel.place(x=0, y=50)

        # Top frame and text for the payment window
        Topframe = Frame(root8, bg='black', width=1000, height=100)
        Topframe.place(x=0, y=0)

        Introtext = Label(Topframe, text='SRI SWAMINATH CAFE NEW', font=('Copperplate Gothic Bold', 30, 'bold', 'italic')
                          , bg='black', fg='white', activebackground='black')
        Introtext.place(x=120, y=10, width=750)

        # Body frame for payment details
        bodyframe = Frame(root8, bg='black', width=650, height=550)
        bodyframe.place(x=150, y=150)

        billtitle = Label(bodyframe, text='BILL PAYMENT', font=('Rockwell', 36, 'bold', 'italic')
                          , bg='black', fg='white', activebackground='black')
        billtitle.place(x=150, y=20)

        cusname = Label(bodyframe, text=f'CUSTOMER NAME : {ue}', font=("Copperplate Gothic Bold", 18, "bold")
                        , bg='black', fg='white', activebackground='black')
        cusname.place(x=20, y=160)

        cusmobileno = Label(bodyframe, text=f'MOBILE NUMBER  : {pe}', font=("Copperplate Gothic Bold", 18, "bold")
                            , bg='black', fg='white', activebackground='black')
        cusmobileno.place(x=20, y=210)

        cusseatno = Label(bodyframe, text=f'SEAT NUMBER : {se}', font=("Copperplate Gothic Bold", 18, "bold")
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
        global bill_amt
        bill_amt = billamtentry.get()

        # Function to reset the bill amount entry field
        def resetfield():
            try:
                billamtentry.delete(0, END)
            except TclError:
                pass

        # Function to check the validity of the bill amount and proceed with the payment
        def billcheck():
            global se
            bee = billamtentry.get()

            if bee == '':
                messagebox.showerror('Error !', 'Enter the valid bill amount !')
                resetfield()
            elif bee.isdigit() != True:
                messagebox.showerror('Error !', 'Enter a valid bill amount !')
                resetfield()
            else:
                successwindow()
                resetfield()

        # Function to display a success message and update records after successful payment
        def successwindow():
            messagebox.showinfo('Success !', 'The amount for the bill has been paid successfully !')
            removed = seat_choices.pop(se, None)
            name_to_search = ue
            bill_amount = billamtentry.get()

            # Read the CSV file
            with open("Customer.csv", mode='r', newline='') as infile:
                reader = csv.reader(infile)
                rows = list(reader)
            
            # Update the relevant rows
            updated_rows = []
            for row in rows:
                if name_to_search in row:
                    # Create the bill content with SE and bill amount
                    bill_content = f'bill_{se}:{bill_amount}'
                    row.append(bill_content)
                updated_rows.append(row)
            
            # Write the updated rows back to the CSV file
            with open("Customer.csv", mode='w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(updated_rows)
            if se.startswith('2'):
                two_seats.append(se)
            elif se.startswith('4'):
                four_seats.append(se)
            elif se.startswith('6'):
                six_seats.append(se)
            elif se.startswith('8'):
                eight_seats.append(se)
            # Check the queue and remove the processed entries
            for i in seat_choices:
                for j in q.queue:
                    if seat_choices[i] == j:
                        pass
                    else:
                        q.dequeue()

            # Close the payment window and return to the manager view
            root8.destroy()
            manager_view()

        # Button to pay the bill
        paybillbutton = Button(bodyframe, text='PAY BILL', command=billcheck,
                               font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                               cursor="hand2", bg="red", fg="white", activebackground='red')
        paybillbutton.place(x=245, y=485)

        root8.mainloop()

    # Call the billing home function to start the process
    billinghome()


#To create a user friendly interface for the customer to enter their details
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

    Toptext = Label(root2, text='ENTER THE DETAILS OF THE CUSTOMER', font=('Rockwell', 32, 'bold'), bg='black', fg='white', activebackground='black')
    Toptext.place(x=60, y=10, width=900)

    def resetfield():
        userentry.delete(0, END)
        phoneentry.delete(0, END)
        emailentry.delete(0,END)

    def email_check(email):
        pattern = r'^[a-zA-Z0-9]+@gmail\.com$'
        return bool(re.match(pattern, email))

    def cusentry():
        global ue
        global order
        global pe
        global ee
        ee=emailentry.get()
        ue = userentry.get()
        pe = phoneentry.get()

        if ue == '' or pe == '':
            messagebox.showerror('Error !', 'Enter all the required values !')
            resetfield()
        elif pe.isdigit() != True:
            messagebox.showerror('Error !', 'Enter a valid phone number !')
            resetfield()
        elif (pe.isdigit() and len(pe) != 10) or str(pe)[0] == '0':
            messagebox.showerror('Error !', 'Enter a valid phone number !')
            resetfield()
        elif email_check(ee) != True:
            messagebox.showerror('Error', 'Enter a valid email ID')
            resetfield()
        else:
            c = 0
            q.enqueue([order,ue,pe])
            cusfile = open('Customer.csv', 'a', newline='')
            cuswriter = csv.writer(cusfile, delimiter=',')
            nl = [order, ue, pe]
            order += 1
            cuswriter.writerow(nl)
            messagebox.showinfo('Customer Details', 'Details noted down successfully !')
            resetfield()
            cusfile.close()
            root2.destroy()
            seatchooser()

    Cusloginframe = Frame(root2, bg='black', width=470, height=500)
    Cusloginframe.place(x=300, y=200)

    def backtohome():
        root2.destroy()
        introscreen()

    homebutton = Button(Cusloginframe, text='Back to Home Page', command=backtohome,
                        font=('Copperplate gothic bold', 20, 'bold'),
                        cursor='hand2', bd=0, bg='#FF006A', fg='white', activebackground='#FF006A')
    homebutton.place(x=60, y=435, width=350)

    Submitbutton = Button(Cusloginframe, text='Submit', command=cusentry, font=("Copperplate Gothic Bold", 20, "bold"),
                          bd=0, cursor="hand2",bg="green", fg="white", activebackground='green')
    Submitbutton.place(x=160, y=375)

    usertext = Label(Cusloginframe, text='Name of the customer', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                     , bg='black', fg='white', activebackground='black')
    usertext.place(x=29, y=30)

    # Add a new Label for the phone number
    phone_label = Label(Cusloginframe, text='Phone Number', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                        , bg='black', fg='white', activebackground='black')
    phone_label.place(x=29, y=150)

    # Add a new Label for the email
    email_label = Label(Cusloginframe, text='Email', font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                        , bg='black', fg='white', activebackground='black')
    email_label.place(x=29, y=270)

    userentry = Entry(Cusloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    userentry.place(x=30, y=90, width=410)

    # Add a new Entry for the phone number
    phoneentry = Entry(Cusloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    phoneentry.place(x=30, y=210, width=410)

    # Add a new Entry for the email
    emailentry = Entry(Cusloginframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
    emailentry.place(x=30, y=330, width=410)

    root2.mainloop()

def mansignup():
    # Close the previous window
    root3.destroy()

    # Create a Tkinter window for manager sign up
    root6 = Tk()
    root6.geometry('1000x750')  # Set window size
    root6.title('Manager Sign Up')  # Set window title
    root6.resizable(0, 0)  # Disable window resizing
    root6.config(bg='black')  # Set background color

    # Load and display background image
    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root6, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    # Create top frame for displaying title
    Topframe = Frame(root6, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    # Title text for manager sign up
    Toptext = Label(root6, text='ENTER THE DETAILS OF THE NEW MANAGER', font=('Rockwell', 28, 'bold')
                    , bg='black', fg='white', activebackground='black')
    Toptext.place(x=20, y=10, width=950)

    # Function to clear entry fields
    def resetfield():
        nameentry.delete(0, END)
        emailentry.delete(0, END)
        passentry.delete(0, END)

    # Function to handle manager sign up details
    def mandetails():
        ne = nameentry.get()  # Get manager name
        ee = emailentry.get()  # Get manager email
        pe = passentry.get()  # Get manager password

        def email_check(email):
            pattern = r'^[a-zA-Z0-9]+@gmail\.com$'
            return bool(re.match(pattern, email))
        # Validation checks
        if ne == '' or ee == '' or pe == '':
            messagebox.showerror('Error !', 'Enter all the required values !')
            resetfield()  # Clear entry fields
        elif email_check(ee) != True:
            messagebox.showerror('Error', 'Enter a valid email ID')
            resetfield()
        else:
            # Write manager details to CSV file
            manfile = open('Manager.csv', 'a', newline='')
            manwriter = csv.writer(manfile, delimiter=',')
            nl = [ne, ee, pe]
            manwriter.writerow(nl)
            messagebox.showinfo('Manager Details', 'Account created successfully !')
            resetfield()  # Clear entry fields
            manfile.close()
            root6.destroy()  # Close current window
            managersystem()  # Open manager login window

    # Create frame for manager sign up fields
    Mansignupframe = Frame(root6, bg='black', width=450, height=500)
    Mansignupframe.place(x=250, y=170)

    # Button to submit manager sign up details
    Createbutton = Button(Mansignupframe, text='Create Account', command=mandetails,
                          font=("Copperplate Gothic Bold", 20, "bold"), bd=0,
                          cursor="hand2", bg="green", fg="white", activebackground='green')
    Createbutton.place(x=80, y=420)

    # Labels and entry fields for manager sign up details
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

    root6.mainloop()  # Start the Tkinter event loop to keep the window open

    
def managersystem():
    global ne, ee, root3  # Declare variables as global to access them outside the function
    
    # Create a Tkinter window for manager login
    root3 = Tk()
    root3.geometry('1000x750')  # Set window size
    root3.title('Manager Entry')  # Set window title
    root3.resizable(0, 0)  # Disable window resizing
    root3.config(bg='black')  # Set background color

    # Load and display background image
    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root3, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    # Create top frame for displaying title
    Topframe = Frame(root3, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    # Title text for manager login
    Toptext = Label(root3, text='ENTER THE DETAILS OF THE MANAGER', font=('Rockwell', 32, 'bold')
                    , bg='black', fg='white', activebackground='black')
    Toptext.place(x=20, y=10, width=950)

    # Function to clear entry fields
    def resetfield():
        nameentry.delete(0, END)
        emailentry.delete(0, END)
        passentry.delete(0, END)

    # Function to handle manager login
    def manentry():
        global ne, ee  # Access global variables
        ne = nameentry.get()  # Get manager name
        ee = emailentry.get()  # Get manager email
        pe = passentry.get()  # Get manager password

        def email_check(email):
            pattern = r'^[a-zA-Z0-9]+@gmail\.com$'
            return bool(re.match(pattern, email))
        # Validation checks
        if ne == '' or ee == '' or pe == '':
            messagebox.showerror('Error !', 'Enter all the required values !')
            resetfield()  # Clear entry fields
        elif email_check(ee) != True:
            messagebox.showerror('Error', 'Enter a valid email ID')
            resetfield()
        else:
            # Read manager details from CSV file
            manfile = open('Manager.csv', 'r', newline='')
            manreader = csv.reader(manfile, delimiter=',')
            for i in manreader:
                if i[0] == 'Name of the Manager':
                    continue
                else:
                    # Check if entered details match with records
                    if ne == i[0] and ee == i[1] and pe == i[2]:
                        messagebox.showinfo('Manager Details', 'Login successful !')
                        resetfield()  # Clear entry fields
                        manfile.close()
                        root3.destroy()  # Close current window
                        manager_view()  # Open manager view window
                        break
            else:
                messagebox.showerror('Error !', 'One or more fields do not match properly !')
                resetfield()  # Clear entry fields

    # Create frame for manager login fields
    Manloginframe = Frame(root3, bg='black', width=500, height=620)
    Manloginframe.place(x=250, y=120)

    # Button to submit manager login details
    Submitbutton = Button(Manloginframe, text='Submit', command=manentry, font=("Copperplate Gothic Bold", 20, "bold"),
                          bd=0,
                          cursor="hand2", bg="green", fg="white", activebackground='green')
    Submitbutton.place(x=180, y=410)

    # Button to navigate to manager sign up window
    createacctbutton = Button(Manloginframe, text='New Manager? Create account', command=mansignup,
                              font=("Copperplate Gothic Bold", 18, "bold"), bd=0,
                              cursor="hand2", bg="blue", fg="white", activebackground='blue')
    createacctbutton.place(x=10, y=480)

    # Labels and entry fields for manager login
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

    def backtohome():
        root3.destroy()
        introscreen()

    homebutton = Button(Manloginframe, text='Back to Home Page', command=backtohome,
                        font=('Copperplate gothic bold', 20, 'bold'),
                        cursor='hand2', bd=0, bg='#FF006A', fg='white', activebackground='#FF006A')
    homebutton.place(x=60, y=550, width=350)

    root3.mainloop()  # Start the Tkinter event loop to keep the window open

def introscreen():
    # Create a Tkinter window for the login screen
    root1 = Tk()
    root1.geometry('1000x750')  # Set window size
    root1.title('Login Page')  # Set window title
    root1.resizable(0, 0)  # Disable window resizing
    root1.config(bg='black')  # Set background color

    # Function to handle customer login
    def customerlogin():
        root1.destroy()  # Close current window
        customersystem()  # Call the customer login system function

    # Function to handle manager login
    def managerlogin():
        root1.destroy()  # Close current window
        managersystem()  # Call the manager login system function

    # Load and display background image
    bgimage = PhotoImage(file='Restaurant bg.png')
    bgplace = Label(root1, image=bgimage, bd=0, height=750, width=1000, bg='black')
    bgplace.place(x=0, y=0)

    # Create top frame for displaying title
    Topframe = Frame(root1, bg='black', width=1000, height=100)
    Topframe.place(x=0, y=0)

    # Title text for the introduction
    Introtext = Label(Topframe, text='Welcome to Sri Swaminath Cafe New',
                      font=('Copperplate Gothic Bold', 24, 'bold', 'italic')
                      , bg='black', fg='white', activebackground='black')
    Introtext.place(x=120, y=10, width=750)

    # Subtitle text for the introduction
    Bottomtext = Label(Topframe, text='Experience the delicacies of South India at the right price',
                       font=('Copperplate Gothic Bold', 18, 'bold', 'italic')
                       , bg='black', fg='white', activebackground='black')
    Bottomtext.place(x=50, y=60, width=900)

    # Frame for login buttons
    Loginframe = Frame(root1, bg='black', width=400, height=400)
    Loginframe.place(x=300, y=200)

    # Text indicating login options
    Loginframetext = Label(Loginframe, text='LOGIN AS', font=('Rockwell', 32, 'bold'), bg='black', fg='white',
                           activebackground='black')
    Loginframetext.place(x=80, y=30, width=250)

    # Button for customer login
    customerbutton = Button(Loginframe, text='Customer', command=customerlogin, font=('Rockwell', 24, 'bold'),
                            cursor='hand2', bd=0, bg='blue', fg='white', activebackground='blue')
    customerbutton.place(x=80, y=140, width=250)

    # Button for manager login
    managerbutton = Button(Loginframe, text='Restaurant Manager', command=managerlogin, font=('Rockwell', 24, 'bold'),
                           cursor='hand2', bd=0, bg='red', fg='white', activebackground='red')
    managerbutton.place(x=30, y=260, width=350)

    root1.mainloop()  # Start the Tkinter event loop to keep the window open
def save_state(seat_choices, filename='state.csv'):
    """
    Write seat choices dictionary to a CSV file.

    Parameters:
    - seat_choices: Dictionary containing seat choices data.
    - filename: Name of the CSV file to write to. Default is 'state.csv'.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in seat_choices.items():
            writer.writerow([key, str(value)])
introscreen()
save_state(seat_choices)
print(seat_choices)

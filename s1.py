from tkinter import *
from tkinter import messagebox, ttk
import csv
from PIL import Image, ImageTk
from customtkinter import *
global ue
global order
order = 1

class queue:
    def __init__(self):
        self.queue = []


    def add(self, item):
        self.queue.append(item)

    def enqueue(self, item):
        self.queue.insert(len(self.queue), item)
        return self.queue

    def dequeue(self):
        x = self.queue[0]
        del self.queue[0]
        return x
q=queue()


class Tree:

    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.children = []

    def addchild(self, childnode):
        self.children.append(childnode)

    def exists(self,nodename,value):
        if self.name == nodename and self.value == value:
            return True
        if self.value == value:
            return True
        for child in self.children:
            if child.exists(nodename,value):
                return True
        return False

    def updatevalue(self, nodename, newvalue):
        if self.name == nodename:
            self.value = newvalue
            return True
        for child in self.children:
            if child.updatevalue(nodename, newvalue):
                return True
        return False

    def inorder_traversal(self):
        elements = []
        if self.children:
            mid = len(self.children) // 2
            for child in self.children[:mid]:
                elements += child.inorder_traversal()
        elements.append(self.value)
        if self.children:
            for child in self.children[mid:]:
                elements += child.inorder_traversal()
        return elements

    def collectdata(self):
        data = []
        self.collectdatarecursive(data, 0)
        return data

    def collectdatarecursive(self, data, level):
        value = self.value if self.value is None else ''
        data.append((self.name, value, level))
        for child in self.children:
            child.collectdatarecursive(data, level + 1)

def writetreetocsv(root, filename):
    data = root.collectdata()
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Value', 'Level'])  # Writing header
        writer.writerows(data)

def loadtreefromcsv(filename):
    nodes = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            name, value, level = row[0], row[1], row[2]
            if value=='':
                value = None
            else:
                try:
                    value = value
                except ValueError:
                    value = value
            nodes.append((name, value, level, Tree(name, value)))

    if not nodes:
        return None

    tree = nodes[0][3]
    for i in range(1, len(nodes)):
        name, value, level, node = nodes[i]
        parentnode = findparent(nodes, i)
        if parentnode:
            parentnode.addchild(node)

    return tree

def findparent(nodes, index):
    nodelevel = nodes[index][2]
    for i in range(index - 1, -1, -1):
        if nodes[i][2] < nodelevel:
            return nodes[i][3]
    return None

def get_input_value(prompt):
    value = input(prompt)
    if value.lower() == 'none':
        return None
    try:
        return int(value)  # Try to convert to int
    except ValueError:
        try:
            return float(value)  # Try to convert to float
        except ValueError:
            return value  # Otherwise, return as string

def updatenode(tree,nodename,newvalue):
    if tree is None:
        return False
    return tree.updatevalue(nodename,newvalue)

filename = "Customerdata.csv"
try:
    tree = loadtreefromcsv(filename)
    if tree:
        print("Tree loaded from CSV.")
    else:
        raise FileNotFoundError

except FileNotFoundError:
    print("CSV file not found or empty. Creating a new tree.")
    tree = Tree('Tree','Sri Swaminath Cafe New')
    twoseater = Tree('twoseater','Two Seater')
    fourseater = Tree('fourseater','Four Seater')
    sixseater = Tree('sixseater','Six Seater')
    eightseater = Tree('eightseater','Eight Seater')

    twoA = Tree('twoA',None)
    twoB = Tree('twoB',None)
    twoC = Tree('twoC',None)
    twoD = Tree('twoD',None)
    fourA = Tree('fourA',None)
    fourB = Tree('fourB',None)
    fourC = Tree('fourC',None)
    fourD = Tree('fourD',None)
    sixA = Tree('sixA',None)
    sixB = Tree('sixB',None)
    sixC = Tree('sixC',None)
    eightA = Tree('eightA',None)
    eightB = Tree('eightB',None)
    eightC = Tree('eightC',None)

    tree.addchild(twoseater)
    tree.addchild(fourseater)
    tree.addchild(sixseater)
    tree.addchild(eightseater)

    twoseater.addchild(twoA)
    twoseater.addchild(twoB)
    twoseater.addchild(twoC)
    twoseater.addchild(twoD)

    fourseater.addchild(fourA)
    fourseater.addchild(fourB)
    fourseater.addchild(fourC)
    fourseater.addchild(fourD)

    sixseater.addchild(sixA)
    sixseater.addchild(sixB)
    sixseater.addchild(sixC)

    eightseater.addchild(eightA)
    eightseater.addchild(eightB)
    eightseater.addchild(eightC)

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

    label2_1 = Label(root4, text="2A", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label2_1.place(x=75, y=314, width=154)

    seat2 = Label(root4, image=img_2_tk)
    seat2.place(x=275, y=160)

    label2_2 = Label(root4, text="2B", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label2_2.place(x=275, y=314, width=154)

    seat_3 = Label(root4, image=img_2_tk)
    seat_3.place(x=475, y=160)

    label2_3 = Label(root4, text="2C", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label2_3.place(x=475, y=314, width=154)

    seat4 = Label(root4, image=img_2_tk)
    seat4.place(x=675, y=160)

    label2_4 = Label(root4, text="2D", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label2_4.place(x=675, y=314, width=154)

    # 4seat

    img2 = ImageTk.PhotoImage(Image.open("4seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img2)
    seat1.place(x=75, y=390)

    label4_1 = Label(root4, text="4A", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label4_1.place(x=75, y=544, width=154)

    seat2 = Label(root4, image=img2)
    seat2.place(x=275, y=390)

    label4_2 = Label(root4, text="4B", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label4_2.place(x=275, y=544, width=154)

    seat3 = Label(root4, image=img2)
    seat3.place(x=475, y=390)

    label4_3 = Label(root4, text="4C", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label4_3.place(x=475, y=544, width=154)

    seat4 = Label(root4, image=img2)
    seat4.place(x=675, y=390)

    label4_4 = Label(root4, text="4D", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label4_4.place(x=675, y=544, width=154)

    # 6seat
    img3 = ImageTk.PhotoImage(Image.open("6seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img3)
    seat1.place(x=875, y=160)

    label6_1 = Label(root4, text="6A", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label6_1.place(x=875, y=314, width=154)

    seat2 = Label(root4, image=img3)
    seat2.place(x=1075, y=160)

    label6_2 = Label(root4, text="6B", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label6_2.place(x=1075, y=314, width=154)

    seat3 = Label(root4, image=img3)
    seat3.place(x=1275, y=160)

    label6_3 = Label(root4, text="6C", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label6_3.place(x=1275, y=314, width=154)

    # 8seat

    img4 = ImageTk.PhotoImage(Image.open("8seat.png").resize((150, 150)))

    seat1 = Label(root4, image=img4)
    seat1.place(x=875, y=390)

    label8_1 = Label(root4, text="8A", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label8_1.place(x=875, y=544, width=154)

    seat2 = Label(root4, image=img4)
    seat2.place(x=1075, y=390)

    label8_2 = Label(root4, text="8B", background="green", fg='white', font=('Calibri', 20, 'bold'))
    label8_2.place(x=1075, y=544, width=154)

    seat3 = Label(root4, image=img4)
    seat3.place(x=1275, y=390)

    label8_3 = Label(root4, text="8C", background="green", fg='white', font=('Calibri', 20, 'bold'))
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

    # create a function for booked successfully page
    def book(seat_no):
        seatno = seat_no.get()
        if seatno.isdigit():
            filename = 'Customerdata.csv'
            data = q.get()

            label_text = ""
            seat_label = None
        # Define a function to calculate the x position based on seat category
            def calculate_x_position(category):
                if category == 'two':
                    return 75
                elif category == 'four':
                    return 275
                elif category == 'six':
                    return 875
                elif category == 'eight':
                    return 1075
                else:
                    return 0  # Default to 0 if category is not recognized
            
            # Define a function to calculate the y position based on seat number
            def calculate_y_position(category):
                if category in ['two', 'four']:
                    return 160
                elif category in ['six', 'eight']:
                    return 390
                else:
                    return 0  # Default to 0 if category is not recognized

            # Define seat categories and their corresponding seat numbers and ranges
            seat_categories = {
                'two': {'seats': ['A', 'B', 'C', 'D'], 'range': (1, 2)},
                'four': {'seats': ['A', 'B', 'C', 'D'], 'range': (3, 4)},
                'six': {'seats': ['A', 'B', 'C'], 'range': (5, 6)},
                'eight': {'seats': ['A', 'B', 'C'], 'range': (7, 8)}
            }

            # Convert entered seat number to integer for comparison
            seatno_int = int(seatno)

            # Iterate through seat categories to find the appropriate category and seat
            for category, seat_info in seat_categories.items():
                seat_range = seat_info['range']
                if seat_range[0] <= seatno_int <= seat_range[1]:
                    for seat in seat_info['seats']:
                        if tree.exists(category + seat, None):
                            updatenode(tree, category + seat, data)
                            writetreetocsv(tree, filename)
                            label_text = category + seat
                            seat_label = Label(root4, text=category + seat, background="#00FF00", fg='black',
                                               font=('Calibri', 20, 'bold'))
                            seat_label.place(x=calculate_x_position(category), y=calculate_y_position(category), width=154)
                            break  # Found available seat, break out of loop
                    else:
                        continue  # No available seat in this category, continue to next category
                    break  # Found available seat, break out of loop
                
            if not label_text:
                messagebox.showinfo("Error!", "No available seats in the selected range. Please try again later.")
            else:
                resetfield()

                def update():
                    seat_label.config(background="#FF0000", fg='white')

                root4_child = Toplevel(root4)
                root4_child.title("Customer Seat Booking Confirmation Window")
                root4_child.geometry('450x285')
                root4_child.resizable(0, 0)

                image_original = Image.open("customerbg.jpg")
                image_tk = ImageTk.PhotoImage(image_original)

                canvas1 = Canvas(root4_child, background="black", bd=0, highlightthickness=0, relief="ridge")
                canvas1.place(relwidth=1, relheight=1)
                canvas1.create_image((0, 0), image=image_tk, anchor="nw")

                def stretch(event):
                    width = event.width
                    height = event.height
                    resized_image = image_original.resize((width, height))
                    resized_tk = ImageTk.PhotoImage(resized_image)
                    canvas1.create_image(0, 0, image=resized_tk, anchor="nw")

                canvas1.bind("<Configure>", stretch)

                label_booked = CTkLabel(root4_child, text=f"Dear {ue},\nYour table has been\nsuccessfully booked!\n Table no: {label_text}",
                                        fg_color="green", width=400, height=50, font=("New Times Roman", 24, 'bold'),
                                        corner_radius=0, bg_color="black", text_color="white", anchor=N)
                label_booked.place(x=25, y=70)

                button = Button(root4_child, text='Update', font=("Copperplate Gothic Bold", 20, "bold"), bd=0, cursor="hand2",
                                bg="red", fg="white", activebackground='red', command=update)
                button.place(x=140, y=205)

                root4_child.mainloop()
        else:
            messagebox.showinfo("Error!", "Enter the number of seats!!")
            resetfield()


        # enter to book

        noofseatslabel = Label(detailsframe, text="Enter the number of seats", background="black", fg='white', font=('Copperplate Gothic Bold', 20, 'bold'))
        noofseatslabel.place(x=550,y=10)

        Nameframe = Label(detailsframe, text='Welcome, '+ue, font=("Copperplate Gothic Bold", 20, 'bold'), bg='black', fg='white')
        Nameframe.place(x=60, y=10)

        seats = Entry(detailsframe, font=("Times New Roman", 20, 'bold'), bg='white', fg='black')
        seats.place(x=625, y=50)
        q.enqueue(seats.get())
        q.enqueue(seats.get())

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
            self.style.configure("Treeview",
                                 background="grey",
                                 foreground="black",
                                 rowheight=30,
                                 fieldbackground="silver",
                                 font=("times new roman", 16))
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

        getdetbutton = Button(detailframe, text='GET DETAILS', command=paymentwindow,
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
            messagebox.showinfo('Success!', 'The amount for the bill has been paid successfully')
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

print(q.queue)


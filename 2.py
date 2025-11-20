from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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

root = Tk()
root.title("Customer")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the size of the window to fill the entire screen without hiding the title bar
root.geometry("%dx%d" % (width, height))
root.wm_attributes('-fullscreen', False)

image_original = Image.open("manager.jpg")
image_tk = ImageTk.PhotoImage(image_original)

canvas1 = Canvas(root, background="black", bd=0, highlightthickness=0, relief="ridge")
canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
canvas1.create_image((0,0), image=image_tk, anchor="nw")

# take the data
lst = [("Raj", "8263427232", "1A"),
       ("Aaryan", "34534343434", "4B"),
       ("Vaishnavi", "3434342323", '1D'),
       ("Rachna", "789888767", "3B"),
       ("Shubham", "656577685", "2C")]

t = Table(root, lst)

manager=Label(root,text="Name :xxxxxx",font=("times new roman",25),bg="grey").place(x=1250,y=450)
id=Label(root,text="ID :YYYYY",font=("times new roman",25),bg="grey").place(x=1250,y=500)


root.mainloop()

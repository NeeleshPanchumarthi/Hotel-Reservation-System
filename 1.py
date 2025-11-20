from tkinter import *
from PIL import ImageTk, Image
from customtkinter import *
from tkinter import messagebox

def stretch(event):
    global resized_tk
    width = event.width
    height = event.height
    resized_image = image_original.resize((width, height))  # Corrected resizing
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas1.create_image(0, 0, image=resized_tk, anchor="nw")

root = Tk()
root.title("customer")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the size of the window to fill the entire screen without hiding the title bar
root.geometry("%dx%d" % (width, height))
root.wm_attributes('-fullscreen', False)
root.columnconfigure((0,1,2,3), weight=1, uniform='a')
root.rowconfigure(0, weight=1)

image_original = Image.open("bg.png")
image_tk = ImageTk.PhotoImage(image_original)

canvas1 = Canvas(root, background="black", bd=0, highlightthickness=0, relief="ridge")
canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
canvas1.create_image((0,0), image=image_tk, anchor="nw")
canvas1.bind("<Configure>", stretch)

#ADD TABLES IMAGES 
#2seat and labels of availability

img_2 = Image.open("2seat.png")
img_2_resized = img_2.resize((150, 150))  # Corrected resizing
img_2_tk = ImageTk.PhotoImage(img_2_resized)

seat1 = Label(root, image=img_2_tk)
seat1.place(x=10, y=95)

label2_1=Label(root,text="1A",background="#c65911")
label2_1.place(x=10,y=249,width=154)

seat2=Label(root,image=img_2_tk)
seat2.place(x=1340,y=95)

label2_2=Label(root,text="2A",background="#c65911")
label2_2.place(x=1340,y=249,width=154)

seat_3=Label(root,image=img_2_tk)
seat_3.place(x=10,y=540)

label2_3=Label(root,text="3A",background="#c65911")
label2_3.place(x=10,y=694,width=154)

seat4=Label(root,image=img_2_tk)
seat4.place(x=1340,y=540)

label2_4=Label(root,text="4A",background="#c65911")
label2_4.place(x=1340,y=694,width=154)


#4seat

img2=ImageTk.PhotoImage(Image.open("4seat.png").resize((150,150)))

seat1=Label(root,image=img2)
seat1.place(x=400,y=95)

label4_1=Label(root,text="1B",background="#c65911")
label4_1.place(x=400,y=249,width=154)

seat2=Label(root,image=img2)
seat2.place(x=950,y=95)

label4_2=Label(root,text="2B",background="#c65911")
label4_2.place(x=950,y=249,width=154)

seat3=Label(root,image=img2)
seat3.place(x=400,y=540)

label4_3=Label(root,text="3B",background="#c65911")
label4_3.place(x=400,y=694,width=154)

seat4=Label(root,image=img2)
seat4.place(x=950,y=540)

label4_4=Label(root,text="4B",background="#c65911")
label4_4.place(x=950,y=694,width=154)

#6seat
img3=ImageTk.PhotoImage(Image.open("6seat.png").resize((150,150)))

seat1=Label(root,image=img3)
seat1.place(x=10,y=315.5)

label6_1=Label(root,text="1C",background="#c65911")
label6_1.place(x=10,y=469.5,width=154)

seat2=Label(root,image=img3)
seat2.place(x=1340,y=315.5)

label6_2=Label(root,text="2C",background="#c65911")
label6_2.place(x=1340,y=469.5,width=154)

#8seat

img4=ImageTk.PhotoImage(Image.open("8seat.png").resize((200,200)))

seat1=Label(root,image=img4)
seat1.place(x=650,y=315.5)

label8_1=Label(root,text="1D",background="#c65911")
label8_1.place(x=650,y=520,width=204)

#notes for colour identification
note_label = Label(root, text="NOTE!",bg="#c65911",font=("new times roman",13),fg="white").place(x=10,y=10)
red=Label(root,text="Red: Booked",bg="red",font=("new times roman",13)).place(x=10,y=34)
#create a button for entering the no of seats required
seats=CTkEntry(master=root,placeholder_text="Enter the number of seats",fg_color=("#c65911"),text_color="white",width=195,height=40,corner_radius=10,placeholder_text_color="white", border_width=0,bg_color="#964B00",font=("times new roman",17))
seats.place(x=650,y=710)

#create a function to update the booking

def update(seat):
    
    seat.config(bg="#FF0000")
    

#create a function for booked successfully page
def book():
 seat=seats.get()
 if seat:
    
    
    def stretch(event):
        global resized_tk
        width = event.width
        height = event.height
        resized_image = image_original.resize((width, height))  # Corrected resizing
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas1.create_image(0, 0, image=resized_tk, anchor="nw")

    root = Toplevel()
    root.title("customer")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    
#refresh the second window
    def refresh(seat):
        update(seat)
        root.destroy()
# Set the size of the window to fill the entire screen without hiding the title bar
    root.geometry("%dx%d" % (width, height))
    root.wm_attributes('-fullscreen', False)
    root.columnconfigure((0,1,2,3), weight=1, uniform='a')
    root.rowconfigure(0, weight=1)

    image_original = Image.open("greentick.png")
    image_tk = ImageTk.PhotoImage(image_original)

    canvas1 = Canvas(root, background="black", bd=0, highlightthickness=0, relief="ridge")
    canvas1.place(relwidth=1, relheight=1)  # Place the canvas to cover the entire window
    canvas1.create_image((0,0), image=image_tk, anchor="nw")
    canvas1.bind("<Configure>", stretch)
    #successfull boooked
    label_booked=CTkLabel(root,    
                   text="""     
    successfully booked!
Table no:
""", fg_color="green", width=300, height=35, font=("New Times Roman",15),
corner_radius=0, bg_color="black", text_color="black",anchor=N)
    label_booked.place(x=650, y=460)

    #refresh button
    button=CTkButton(root,text="Refresh",fg_color="#008000",hover_color="#00cc66",corner_radius=20,bg_color="brown",command=lambda:refresh(label2_1))
    button.place(x=720,y=750)
    root.mainloop()
 else:
    messagebox.showinfo("Error","Enter the number of seats!!")
    
#enter to book
book=CTkButton(master=root,text="Book",fg_color="#008000",hover_color="#00cc66",bg_color="brown",corner_radius=20,command=book)
book.place(x=670,y=760)


root.mainloop()

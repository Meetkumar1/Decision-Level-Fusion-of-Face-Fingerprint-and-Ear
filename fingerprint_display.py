from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Fingerprint_model:
    def __init__(self):
        root = Toplevel()
        root.title("fingerprint")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.state('zoomed')

       
        image = Image.open(r'pics/1_1.jpg')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

    ## Resizable Image
    def resize_image(self,event):
        new_width = 250
        new_height = 250
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo
  
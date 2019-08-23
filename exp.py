import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import PIL
from PIL import Image, ImageTk
import cv2
from fingerprint_display import *
from login import *
from tkinter import filedialog
import tkinter.messagebox as tkm
import functools

root = Tk()
root.title("Multimodal Biometric Authentication")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')


## Function for resizing the Image

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo


## Resizable Image

image = Image.open(r'pics/background.gif')
global copy_of_image
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

## Function

def webcam_face():
     
    width, height = 250, 250
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    cv2.namedWindow("test")

    img_counter = 0
    face_flag = 0

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)

        
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "capture_face_{}.jpg".format(img_counter)
            face_image = frame
            cv2.imshow('face_test_image',face_image)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            face_flag = 1
            img_counter += 1
            cv2.waitKey(600)
            break
    if face_flag == 1:
        webcam_face.has_been_called = True        
    
    cam.release()
    cv2.destroyAllWindows()
webcam_face.has_been_called = False

def webcam_ear():
     
    width, height = 250, 250
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    cv2.namedWindow("test")

    img_counter = 0
    ear_flag = 0

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)

        
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "capture_ear_{}.jpg".format(img_counter)
            ear_image = frame
            cv2.imshow('ear_test_image',ear_image)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            ear_flag = 1
            img_counter += 1
            cv2.waitKey(600)
            break
    if ear_flag == 1:
        webcam_ear.has_been_called = True            
    
    cam.release()
    cv2.destroyAllWindows()
webcam_ear.has_been_called = False    

def fingerprint():     
    Fingerprint_model()


def func_login():
    
    if webcam_face.has_been_called == False and webcam_ear.has_been_called == False:
        tkm.showerror("Required field","Image of Face Required\nImage of Ear Required") 
    if webcam_face.has_been_called == True and webcam_ear.has_been_called == False:
        tkm.showerror("Required field","Image of Ear Required") 
    if webcam_face.has_been_called == False and webcam_ear.has_been_called == True:
        tkm.showerror("Required field","Image of Face Required")    
    if webcam_face.has_been_called and webcam_ear.has_been_called:
        Login_model()
        
    


## Adding Buttons

face_button = Button(root, fg="black", highlightbackground='dark blue', font=("Courier New",30,'bold'), activeforeground="white", text='Face', height=1, width= 15, padx=10, pady=10, command = webcam_face)
face_button.place(relx=0.50, rely=0.4, anchor=CENTER)

ear_button = Button(root, fg="black", bg="blue", highlightbackground='dark blue', font=("Courier New",30,'bold'), activeforeground="white", text='Ear',height=1, width= 15, padx=10, pady=10, command = webcam_ear)
ear_button.place(relx=0.50, rely=0.55, anchor=CENTER)

fingerprint_button = Button(root, fg="black", bg="blue", highlightbackground='dark blue', font=("Courier New",30,'bold'), activeforeground="white", height=1, width= 15,text='Fingerprint', padx=10, pady=10, command=fingerprint)
fingerprint_button.place(relx=0.50, rely=0.7, anchor=CENTER)

log_in = Button(root, fg="black", bg="blue", highlightbackground='dark blue', font=("Courier New",30,'bold'), activeforeground="white", text='Login', height=1, width= 7,padx=10, pady=10, command = func_login)
log_in.place(relx=0.50, rely=0.85, anchor=CENTER)

quit = Button(root, fg="black", bg="blue", highlightbackground='dark blue', font=("Courier New",30,'bold'), activeforeground="white", text="Quit", height=1, width= 5,command=root.destroy, padx=10, pady=10)
quit.place(relx=0.90, rely=0.2, anchor=CENTER)



root.mainloop()

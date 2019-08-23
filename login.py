from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as tkm
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
import cv2
import os




class Login_model:
    def __init__(self):
        
        ## FINGERPRINT

        # Fingerprint image files count
        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/fingerprint_model/dataset/training_set/yes"))
        fingerprint_file_count_yes = len(files)
        fingerprint_count_yes = fingerprint_file_count_yes + 1

        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/fingerprint_model/dataset/training_set/no"))
        fingerprint_file_count_no = len(files)
        fingerprint_count_no = fingerprint_file_count_no + 1

        ## Testing Fingerprint
        fingerprint_loaded_model = load_model('fingerprint_1.h5')

        fingerprint_test_image = image.load_img("pics/1_1.jpg",target_size=(64, 64))
        fingerprint_temp_image = image.load_img("pics/1_1.jpg",target_size=(250, 250))
        fingerprint_test_image = image.img_to_array(fingerprint_test_image)
        # adding the batch size as predict method expects
        fingerprint_test_image = np.expand_dims(fingerprint_test_image, axis=0)
        # Predicting the test image
        fingerprint_result= fingerprint_loaded_model.predict(fingerprint_test_image)
        fingerprint_decision = fingerprint_result[0][0]
        print(fingerprint_file_count_yes)
        print(fingerprint_file_count_no)
        
        ## FACE

        # Face image files count
        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/face_model/dataset/training_set/yes"))
        face_file_count_yes = len(files)
        face_count_yes = face_file_count_yes + 1

        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/face_model/dataset/training_set/no"))
        face_file_count_no = len(files)
        face_count_no = face_file_count_no + 1

        ## Testing Face
        face_loaded_model = load_model('face_1.h5')

        face_temp_image = image.load_img("capture_face_0.jpg",target_size=(250, 250))
        #face_test_image = image.load_img("test_face.jpg",target_size=(64, 64))
        face_test_image = image.img_to_array(face_test_image)
        # adding the batch size as predict method expects
        face_test_image = np.expand_dims(face_test_image, axis=0)
        # Predicting the test image
        face_result= face_loaded_model.predict(face_test_image)
        face_decision = face_result[0][0]
        print(face_file_count_yes)
        print(face_file_count_no)

        ## EAR

        # Ear image files count
        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/ear_model/dataset/training_set/yes"))
        ear_file_count_yes = len(files)
        ear_count_yes = ear_file_count_yes + 1

        path, dirs, files = next(os.walk("/Users/meetkumarpatel/Desktop/ear_model/dataset/training_set/no"))
        ear_file_count_no = len(files)
        ear_count_no = ear_file_count_no + 1

        ## Testing Ear
        ear_loaded_model = load_model('ear_1.h5')

        ear_temp_image = image.load_img("capture_ear_0.jpg",target_size=(250, 250))
        #ear_test_image = image.load_img("test_ear.jpg",target_size=(64, 64))
        ear_test_image = image.img_to_array(ear_test_image)
        # adding the batch size as predict method expects
        ear_test_image = np.expand_dims(ear_test_image, axis=0)
        # Predicting the test image
        ear_result= ear_loaded_model.predict(ear_test_image)
        ear_decision = ear_result[0][0]
        print(ear_file_count_yes)
        print(ear_file_count_no)
        

        if fingerprint_decision > 0.5 and face_decision > 0.5 and ear_decision > 0.5:
            tkm.showinfo("Result","ACCESS_GRANTED")
            """
            Database updation
            Add all the images to respective datasets if access is granted
            Upto the limit (25000 images)
            """

            if fingerprint_file_count_yes < 25000:
                fingerprint_temp_image.save("/Users/meetkumarpatel/Desktop/fingerprint_model/dataset/training_set/yes/fingerprint_train_yes_img_{}.jpg".format(fingerprint_count_yes))
            if face_file_count_yes < 25000:
                face_temp_image.save("/Users/meetkumarpatel/Desktop/face_model/dataset/training_set/yes/face_train_yes_img_{}.jpg".format(face_count_yes))
            if ear_file_count_yes < 25000:
                ear_temp_image.save("/Users/meetkumarpatel/Desktop/ear_model/dataset/training_set/yes/ear_train_yes_img_{}.jpg".format(ear_count_yes))

        elif fingerprint_decision <= 0.5 or face_decision <= 0.5 or ear_decision <= 0.5:
            if fingerprint_decision <=0.5 and face_decision <=0.5 and ear_decision <=0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFingerprint Unauthorized\nFace Unauthorized\nEar Unauthorized")
            if fingerprint_decision <=0.5 and face_decision <=0.5 and ear_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFingerprint Unauthorized\nFace Unauthorized")
            if face_decision <=0.5 and ear_decision <=0.5 and fingerprint_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFace Unauthorized\nEar Unauthorized")
            if fingerprint_decision <=0.5 and ear_decision <=0.5 and face_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFingerprint Unauthorized\nEar Unauthorized")
            if fingerprint_decision <=0.5 and ear_decision > 0.5 and face_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFingerprint Unauthorized")
            if face_decision <=0 and ear_decision > 0.5 and fingerprint_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nFace Unauthorized")
            if ear_decision <=0.5 and fingerprint_decision > 0.5 and face_decision > 0.5:
                tkm.showerror("Result","ACCESS DENIED:\nEar Unauthorized")
                
                


            


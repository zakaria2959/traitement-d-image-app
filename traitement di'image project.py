from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import cv2
from matplotlib import pyplot as plt
import cv2 as cv

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np




class ImageConverter:
    def __init__(self, master):
        self.master = master
        master.title("traitement d'image app")
        

        self.image_path = None
        self.image_path1 = None

        self.label3 = Label(master,image=icon)
        # Place the label in the center of the window
        self.label3.place(relx=0.5, rely=0.5, anchor=CENTER)

        

        self.label = Label(master)
        # Place the label in the center of the window
        self.label.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.label1 = Label(master)
        # Place the label in the center of the window
        self.label1.place(relx=0.75, rely=0.5, anchor=CENTER)
        

        self.load_button = Button(master, text="Load Image", command=self.load_image,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12)) #(flat, raised, sunken, groove, ridge)
        self.load_button.grid(column=0,row=0,padx=2,pady=2)
        root.columnconfigure(0, weight=1)
        


        self.grayscale_button = Button(master, text="Grayscale", command=self.convert_to_grayscale,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        self.grayscale_button.grid(column=1,row=0,padx=2,pady=2)
        root.columnconfigure(1, weight=1)
        


        self.binary_button = Button(master, text="Binary", command=self.convert_to_binary,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        self.binary_button.grid(column=2,row=0,padx=2,pady=2)
        root.columnconfigure(2, weight=1)
        


        histogram_button = Button(root, text="Display Histogram", command=self.display_histogram,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        histogram_button.grid(column=3,row=0,padx=2,pady=2)
        root.columnconfigure(3, weight=1)
        

        histogram_button = Button(root, text="Add noise", command=self.add_noise,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        histogram_button.grid(column=4,row=0,padx=2,pady=2)
        root.columnconfigure(4, weight=1)


        self.binary_button = Button(master, text="save image", command=self.save_image,background="red",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        self.binary_button.grid(column=5,row=0,padx=2,pady=2)
        root.columnconfigure(5, weight=1)
        

        self.binary_button = Button(master, text="f3i", command=self.convert_to_binary,background="#2A5E8F",fg="white",relief="flat",width=15, height=1,font=("calibri",12))
        self.binary_button.grid(column=6,row=0,padx=2,pady=2)
        root.columnconfigure(6, weight=1)


    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        img = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo

    def convert_to_grayscale(self):
            img = Image.open(self.image_path).convert('L')
            photo = ImageTk.PhotoImage(img)
            self.label1.configure(image=photo)
            self.label1.image = photo

    def convert_to_binary(self):
            img = Image.open(self.image_path).convert('L')
            b = img.point(lambda x: 0 if x < 128 else 255, '1')
            photo = ImageTk.PhotoImage(b)
            self.label1.configure(image=photo)
            self.label1.image = photo

    def add_noise(self):
    # Add random Gaussian noise to the image
      self.noise_image = cv2.imread(self.image_path)

      noise = np.random.normal(0, 15, self.noise_image.shape[:2])
      noise = np.stack([noise]*3, axis=-1)
      noise_image = np.clip(self.noise_image + noise, 0, 255).astype(np.uint8)
      noise_pil = Image.fromarray(noise_image)
      noise_tk = ImageTk.PhotoImage(noise_pil)

      self.label1.configure(image=noise_tk)
      self.label1.image = noise_tk

              
    def display_histogram(self):
       
           # Convert image to grayscale and calculate histogram
        img = Image.open(self.image_path).convert('L')
        hist, bins = np.histogram(img, bins=256)
        
        # Plot histogram using matplotlib
        plt.figure()
        plt.bar(bins[:-1], hist, width=1)
        plt.title("Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.show()
    
    def save_image(self):
        if self.image_path is None:
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if not file_path:
            return

        img = Image.open(self.image_path)
        img.save(file_path)


        
root = Tk()
icon = PhotoImage(file = r"D:\m1 s2\tm\deskto\projet\icons.png")

root.iconphoto(False, icon)
#button = Button(root, text="Quit", command=root.destroy)
#button.grid(column=3,row=1,padx=2,pady=2)
root.geometry("1100x550")
root.config(bg="#EEEEEE")
app = ImageConverter(root)
root.mainloop()

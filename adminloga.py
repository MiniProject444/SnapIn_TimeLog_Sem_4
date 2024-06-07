import io
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os
import mysql.connector
from PIL import Image, ImageTk, ImageFilter, ImageDraw
from css import *
from datetime import datetime
import datetime
import pandas as pd
from openpyxl import Workbook, load_workbook
from FaceRecognitionApp import FaceRecognitionApp
from wid import SlidePanel
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import os
from logedin import logedin
class adminlog:
    def __init__(self, root):
        self.root = root
        self.loged= root
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="", database="facee")
        self.mycursor = self.mydb.cursor()
        self.opne = None
        self.admin()

    def admin(self):
        self.root.title("Face recognition")
        self.root.configure(bg='#A8DEEA')
        self.root.attributes('-fullscreen', True)  # Fullscreen mode
        
        # Load the image
        image_path = os.path.abspath("Frame2.png")
        bg_image_original = Image.open(image_path)
        
        # Resize the image to match the screen resolution
        bg_image_resized = bg_image_original.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        
        # Convert the resized image to PhotoImage
        self.bg_photo = ImageTk.PhotoImage(bg_image_resized)

        # Create a Label to place the image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.namee = tk.Entry(self.root, font=("Arial", 18))
        self.namee.place(relx=0.4453, rely=0.44, relwidth=0.257, relheight=0.06)
        
        self.passw = tk.Entry(self.root, font=("Arial", 18), show='*')
        self.passw.place(relx=0.4453, rely=0.546, relwidth=0.257, relheight=0.06)

        # Other widgets and bindings
        image_path1 = os.path.abspath("button2.png")
        bg_image_original1 = Image.open(image_path1)
        
        # Resize the image to match the screen resolution
        bg_image_resized1 = bg_image_original1.resize((400,85), Image.LANCZOS)
        
        # Convert the resized image to PhotoImage
        self.bg_photo1= ImageTk.PhotoImage(bg_image_resized1)
        bu = tk.Button(master=self.root, text="",color=None, image=self.bg_photo1, command=self.lin, fg="black")
        bu.place(relx=0.378, rely=0.7247, relwidth=0.2359, relheight=0.078)

        self.btm = get_buttonb(self.root, 'Back to main', 'gray', self.back_to_main, fg='black')
        self.btm.place(relx=0.9, rely=0.01, relwidth=0.09)
        
        self.root.bind('<Escape>', self.close)
    def back_to_main(self):
        self.root.destroy()
        self.parent.create_main_window()

    def lin(self):
        admins = {"101": '12333', "102": '1233', "103": '1233', "104": '1233'}
        try:
            self.entered_id = self.namee.get()  
            entered_password = self.passw.get()
            if (self.entered_id.strip() in admins.keys()) and admins[self.entered_id]==entered_password:
                messagebox.showinfo("Welcome", "Successfully logged in")
                self.da=tk.Toplevel(self.root)
                daf=logedin(parent=self.da,id=self.entered_id.strip(),call=self.start)
            else:
                messagebox.showerror("Not Admin", "Please try with correct ID and password",parent=self.root)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid ID and password",parent=self.root)

    def resize_imageb(self,image_path, relwidth, relheight):
        # Open the image file using PIL and preserve the original color space and gamma information
        original_image = Image.open(image_path).convert('RGB')
        
        # Calculate the new dimensions based on relative width and height
        new_width = int(original_image.width * relwidth)
        new_height = int(original_image.height * relheight)
        
        # Resize the image
        resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
        
        # Convert the resized image to a PhotoImage object using ImageTk.PhotoImage
        return ImageTk.PhotoImage(resized_image)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        self.bg_image_resized = self.bg_image_original.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)
        self.bg_label.config(image=self.bg_photo)
    
    def close(self,event):
        try:
            self.root.destroy()
        except:
            pass

    def start(self):
        self.root.mainloop()
    
if __name__ == "__main__":
    rr=tk.Tk()
    app = adminlog(root=rr)
    rr.mainloop()
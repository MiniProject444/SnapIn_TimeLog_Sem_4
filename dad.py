from tkinter import StringVar, ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import smtplib
from openpyxl import Workbook, load_workbook
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO


def conf():
    # Query to select the Excel data from the database
    select_query = "SELECT excel_data FROM facedata4 where admin_id=%s and subject=%s"
    val = ('101', clicked.get())
    mycursor.execute(select_query, val)
    data = mycursor.fetchone()
    if data:
        # Create a new Excel workbook in memory
        wb = Workbook()
        ws = wb.active
        ws.title = "Face Data"
        ws.append(["login_id", "Present", "Arrived", "Lecture"])  # Header row
        wb_data = data[0]  # Extract binary data
        bio = BytesIO(wb_data)  # Use BytesIO object to handle the Excel data in memory

        # Send the Excel file via email
        send_email(bio,app_password="nbri nljt jiqk adsy",receiver_email=to.get())
    else:
        messagebox.showerror("Error", "Data not found for provided ID and subject", parent=sub)

def send_email(file_stream, receiver_email, app_password, sender_email='soham56kadam@gmail.com'):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'SUCCSSFULL'

    part = MIMEBase('application', "octet-stream")
    part.set_payload(file_stream.getvalue())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="FaceData.xlsx"')
    message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)  # Use app password here
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

    messagebox.showinfo("Email Sent", "Excel file has been sent successfully!", parent=sub)


def resize_image(event):
    new_width = event.width
    new_height = event.height
    bg_image_resized = bg_image_original.resize((new_width, new_height))
    bg_photo = ImageTk.PhotoImage(bg_image_resized)
    bg_label.config(image=bg_photo)
    # Important: save the image object by setting it as an attribute to the label to prevent garbage collection.
    bg_label.image = bg_photo

# Establish connection to the database
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="facee")
mycursor = mydb.cursor()

# Query to fetch subjects
sql = "SELECT subject FROM facedata4 WHERE admin_id=%s"
val = ('101',)
mycursor.execute(sql, val)
options = [item[0] for item in mycursor.fetchall()]  # Unpack the tuple from fetchall

# Create the main window
sub = tk.Tk()
sub.geometry('550x400')

# Load the background image
bg_image_original = Image.open("bgche.png")
bg_image_resized = bg_image_original.resize((550, 400))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

# Display the background image using a label
bg_label = tk.Label(sub, image=bg_photo)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
bg_label.bind('<Configure>', resize_image)
# Save a reference to the photo to avoid garbage collection
bg_label.image = bg_photo

to=ctk.CTkEntry(sub,font=('Helvetica bold', 14),placeholder_text="Enter email address to sent",placeholder_text_color='black',bg_color='#0a94b0')
to.place(relx=0.36,rely=0.27,relwidth=0.6,relheight=0.1)

# Dropdown for selecting subjects
clicked = tk.StringVar(sub)
clicked.set("Choose a subject")  # default value

drop = ttk.OptionMenu(sub, clicked, clicked.get(), *options)
drop.place(relx=0.36,rely=0.44,relheight=0.078,relwidth=0.6)

# Confirmation button
co = tk.Button(sub, text="Confirm",bg='#0000ff' ,font=('Times Roman', 13),command=conf)
co.place(relx=0.28,rely=0.66,relheight=0.1,relwidth=0.45)

# Main application loop
sub.mainloop()
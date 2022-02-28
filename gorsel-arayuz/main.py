from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import pymysql
from tkinter import messagebox
from AddAnime import *
from DeleteAnime import *
from ViewAnime import *

mypass = "root"
mydatabase = "anime"

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database=mydatabase
)
cur = con.cursor()

root = Tk()
root.title("Anime")
root.minsize(width=400, height=400)
root.geometry("700x600")
same = True
n = 0.25

# arkaplan resmi için yardım alındı!!!
background_image = Image.open("animebg1.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#5211D4", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Anime & Manga \n Veritabanı", bg='black', fg='white',
                     font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Anime & Manga Ekle", bg='black', fg='white', command=addAnime)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Kayıt Sil", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Kayıt Listesini Görüntüle", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Çıkış", bg='black', fg='white', command=root.destroy)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()

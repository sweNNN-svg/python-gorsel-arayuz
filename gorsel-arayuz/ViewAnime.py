from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import pymysql

# mysql bağlantısı
#veritab = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #passwd="",
  #database="sirket"
#)
mypass = ""
mydatabase="anime"

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database=mydatabase
)
cur = con.cursor()

# tablo adi
animeTable = "animes"

#veri görüntülenme için yardımm alındı
def View(): 
    
    root = Tk()
    root.title("Kayıtlar!")
    root.minsize(width=400,height=400)
    root.geometry("1200x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#180750")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#260EAF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Anime & Manga \n Kayıtlarını Görüntüle", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    #yadım alınmak zorunlu
    Label(labelFrame, text="%-10s%-20s%-30s%-20s%-30s%-30s%-40s%-40s%-40s"%('aid','Ana Başlık','Kaynak','Tip','Durum','Baslama Tarihi','Bitis Tarihi','Yayin','Studyo'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getanimes = "select * from "+animeTable
    try:
        cur.execute(getanimes)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s%-20s%-30s%-30s%-30s%-30s%-30s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("HATA!!! Kayıtlar Veritabanından Alınamadı!")
    
    buton1 = Button(root,text="ÇIKIŞ",bg='#f7f1e3', fg='black', command=root.destroy)
    buton1.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
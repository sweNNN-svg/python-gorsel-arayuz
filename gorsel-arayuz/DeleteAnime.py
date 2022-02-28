from tkinter import *
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
animeTable = "animes" #Anime Table

#silme işlemi içiçn yardım alındı stckwrflw
def deleteAnime():
    
    aid = animeInfo.get()
    
    deleteSql = "delete from "+animeTable+" where aid = '"+aid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Başarılı!',"Anime/Manga başarılı bir şekilde silindi")
    except:
        messagebox.showinfo("Anime ID kontrol ediniz!")


    print(aid)

    animeInfo.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global animeInfo, animeInfo2, animeInfo3, animeInfo4, animeInfo5, animeInfo6, animeInfo7, animeInfo8, animeInfo9, Canvas1, con, cur, animeTable, root
    
    root = Tk()
    root.title("Sil!")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#180750")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#260EAF",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Anime & Manga \n Kayıt Silme ", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # kayıt id
    lb2 = Label(labelFrame,text="Kayıt ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    animeInfo = Entry(labelFrame)
    animeInfo.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # sil butonu
    buton1 = Button(root,text="SİL !",bg='#d1ccc0', fg='black',command=deleteAnime)
    buton1.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    # çıkış butonu
    buton2 = Button(root,text="ÇIKIŞ",bg='#f7f1e3', fg='black', command=root.destroy)
    buton2.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
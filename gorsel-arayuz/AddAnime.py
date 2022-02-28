import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import pymysql





def animeKayit():
    aid = animeInfo.get()
    ana_baslik = animeInfo2.get()
    kaynak = animeInfo3.get()
    tip = animeInfo4.get()
    durum = animeInfo5.get()
    baslama_tarihi = animeInfo6.get()
    bitis_tarihi = animeInfo7.get()
    yayin = animeInfo8.get()
    studyo = animeInfo9.get()

    tur1 = Var4.get()
    tur2 = Var5.get()
    tur3 = Var6.get()
    tur4 = Var7.get()
    tur5 = Var8.get()
    tur6 = Var9.get()
    tur7 = Var10.get()
    tur8 = Var11.get()
    tur9 = Var12.get()
    tur10 = Var13.get()
    tur11 = Var14.get()
    tur12 = Var15.get()

    sure = Var1.get()
    derece = Var2.get()

    pro = listbox.get(ANCHOR)


    insertanimes = "insert into "+animeTable+" values ('"+aid+"','"+ana_baslik+"','"+str(kaynak)+"','"+str(tip)+"','"+durum+"','"+baslama_tarihi+"','"+bitis_tarihi+"','"+yayin+"','"+studyo+"','"+tur1+"','"+tur2+"','"+tur3+"','"+tur4+"','"+tur5+"','"+tur6+"','"+tur7+"','"+tur8+"','"+tur9+"','"+tur10+"','"+tur11+"','"+tur12+"','"+sure+"','"+derece+"','"+pro+"')"
    try:
        cur.execute(insertanimes)
        con.commit()
        messagebox.showinfo('Başarılı!', "Anime/Manga başarılı bir şekilde eklendi")
    except:
        messagebox.showinfo("Hata!", "Veritabanına eklenemedi!")

    print(aid)
    print(ana_baslik)
    print(kaynak)
    print(tip)
    print(durum)
    print(baslama_tarihi)
    print(bitis_tarihi)
    print(yayin)
    print(studyo)

    print(tur1)
    print(tur2)
    print(tur3)
    print(tur4)
    print(tur5)
    print(tur6)
    print(tur7)
    print(tur8)
    print(tur9)
    print(tur10)
    print(tur11)
    print(tur12)


    print(sure)
    print(derece)
    print(pro)



    root.destroy()


def addAnime():
    global animeInfo, animeInfo2, animeInfo3, animeInfo4, animeInfo5, animeInfo6, animeInfo7, animeInfo8, animeInfo9, Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8, Var9, Var10, Var11, Var12, Var13, Var14, Var15, listbox, Canvas1, con, cur, animeTable, root


    root = tk.Toplevel()
    root.title("Ekle!")
    width = 800
    height = 900
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    # mysql bağlantısı
    # veritab = mysql.connector.connect(
    # host="localhost",
    # user="root",
    # passwd="",
    # database="sirket"
    # )
    mypass = "root"
    mydatabase = "anime"

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database=mydatabase
    )
    cur = con.cursor()

    animeTable = "animes" # anime tablos

    # arkplan1
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#180750")
    Canvas1.pack(expand=True, fill=BOTH)

    # başlık
    headingFrame1 = Frame(root, bg="#260EAF", bd=5)
    headingFrame1.place(x=100, y=10, width=600, height=50)

    headingLabel = Label(headingFrame1, text="Anime&Manga Ekle", bg='black', fg='white', font=('Courier', 20))
    headingLabel.place(x=0, y=0, width=590, height=40)

    # arkplan2
    labelFrame = Frame(root, bg='black')
    labelFrame.place(x=100, y=100, width=600, height=750)

    # Anime ID
    lb1 = Label(labelFrame, text="Anime ID : ", bg='black', fg='white', font=('Courier', 11))
    lb1.place(x=0, y=10, height=10)

    animeInfo = Entry(labelFrame)
    animeInfo.place(x=200, y=10, width=300, height=20)

    # Ana Başlık
    lb2 = Label(labelFrame, text="Ana Başlık : ", bg='black', fg='white', font=('Courier', 11))
    lb2.place(x=0, y=50, height=10)

    animeInfo2 = Entry(labelFrame)
    animeInfo2.place(x=200, y=50, width=300, height=20)

    # Kaynak
    lb3 = Label(labelFrame, text="Kaynak : ", bg='black', fg='white', font=('Courier', 11))
    lb3.place(x=0, y=90, height=15)

    n = tk.StringVar()
    animeInfo3 = ttk.Combobox(labelFrame, textvariable=n, values = ('Manga', 'Oyun', 'Roman', 'Diğer'))
    animeInfo3.place(x=200, y=90, width=300, height=20)


    # Tip
    lb4 = Label(labelFrame, text="Tip : ", bg='black', fg='white', font=('Courier', 11))
    lb4.place(x=0, y=130, height=15)

    n = tk.StringVar()
    animeInfo4 = ttk.Combobox(labelFrame, textvariable=n, values = ('TV Dizisi', 'Filmler', 'OVA', 'ONA', 'ÖZEL BÖLÜM'))
    animeInfo4.place(x=200, y=130, width=300, height=20)


    # Durum
    lb5 = Label(labelFrame, text="Durum : ", bg='black', fg='white', font=('Courier', 11))
    lb5.place(x=0, y=170, height=15)

    n = tk.StringVar()
    animeInfo5 = ttk.Combobox(labelFrame, textvariable=n, values = ('Şu Anda Yayınlanıyor', 'Yayın Tamamlandı', 'Henüz Yayınlanmadı', 'Yakında...'))
    animeInfo5.place(x=200, y=170, width=300, height=20)

    # Yayınlanma Tarihi
    lb6 = Label(labelFrame, text="Başlama Tarihi : ", bg='black', fg='white', font=('Courier', 11))
    lb6.place(x=0, y=210, height=15)

    animeInfo6 = Entry(labelFrame)
    animeInfo6.place(x=200, y=210, width=300, height=20)

    lb7 = Label(labelFrame, text="Bitiş Tarihi : ", bg='black', fg='white', font=('Courier', 11))
    lb7.place(x=0, y=250, height=15)

    animeInfo7 = Entry(labelFrame)
    animeInfo7.place(x=200, y=250, width=300, height=20)

    # Yayın
    lb8 = Label(labelFrame, text="Yayın : ", bg='black', fg='white', font=('Courier', 11))
    lb8.place(x=0, y=290, height=15)

    animeInfo8 = Entry(labelFrame)
    animeInfo8.place(x=200, y=290, width=300, height=20)

    # Stüdyolar
    lb9 = Label(labelFrame, text="Stüdyolar : ", bg='black', fg='white', font=('Courier', 11))
    lb9.place(x=0, y=330, height=15)

    animeInfo9 = Entry(labelFrame)
    animeInfo9.place(x=200, y=330, width=300, height=20)

    # Türler
    lb10 = Label(labelFrame, text="Türler : ", bg='black', fg='white', font=('Courier',11))
    lb10.place(x=0, y=370, height=15)

    Var4 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Aksiyon", variable=Var4, onvalue='Aksiyon', offvalue='').place(x=200, y=370, width=80,height=25)
    # 2
    Var5 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Komedi", variable=Var5, onvalue='Komedi', offvalue='').place(x=290, y=370,width=80, height=25)
    # 3
    Var6 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Dram", variable=Var6, onvalue='Dram', offvalue='').place(x=380, y=370, width=80,height=25)
    # 4
    Var7 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Fantezi", variable=Var7, onvalue='Fantezi', offvalue='').place(x=470, y=370,width=80,height=25)
    # 5
    Var8 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Oyun", variable=Var8, onvalue='Oyun', offvalue='').place(x=200, y=410, width=80,height=25)
    # 6
    Var9 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Sihir", variable=Var9, onvalue='Sihir', offvalue='').place(x=290, y=410, width=80,height=25)
    # 7
    Var10 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Romantik", variable=Var10, onvalue='Romantik', offvalue='').place(x=380, y=410,width=80,height=25)
    # 8
    Var11 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Okul", variable=Var11, onvalue='Okul', offvalue='').place(x=470, y=410, width=80,height=25)
    # 9
    Var12 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Bilim Kurgu", variable=Var12, onvalue='Bilim Kurgu', offvalue='').place(x=200,y=450,width=80,height=25)
    # 10
    Var13 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Seinen", variable=Var13, onvalue='Seinen', offvalue='').place(x=290, y=450,width=80, height=25)
    # 11
    Var14 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Macera", variable=Var14, onvalue='Macera', offvalue='').place(x=380, y=450,width=80, height=25)
    # 12
    Var15 = tk.StringVar()
    ttk.Checkbutton(labelFrame, text="Shōnen", variable=Var15, onvalue='Shōnen', offvalue='').place(x=470, y=450,width=80, height=25)

    #Süre
    lb11 = Label(labelFrame, text="Süre : ", bg='black', fg='white', font=('Courier',11))
    lb11.place(x=0, y=500, height=15)
    #1
    Var1 = tk.StringVar()
    ttk.Radiobutton(labelFrame, text="0 - 10 min.",variable = Var1,value = "0 - 10 min.").place(x=200, y=500, width=90)
    ttk.Radiobutton(labelFrame, text="10 - 15 min",variable = Var1,value="10 - 15 min").place(x=300, y=500, width=90)
    ttk.Radiobutton(labelFrame, text="15 - 24 min",variable = Var1,value= "15 - 24 min").place(x=400, y=500, width=90)


    #Derecelendirme
    lb13 = Label(labelFrame, text="Derecelendirme : ", bg='black', fg='white', font=('Courier',11))
    lb13.place(x=0, y=550, height=15)
    #1
    Var2 = tk.StringVar()
    ttk.Radiobutton(labelFrame, text=" 7+ ",variable = Var2, value = " 7+ ").place(x=200, y=550, width=50)
    ttk.Radiobutton(labelFrame, text=" 13+ ",variable = Var2, value = " 13+ ").place(x=300, y=550, width=50)
    ttk.Radiobutton(labelFrame, text=" 15+ ",variable = Var2, value = " 15+ ").place(x=400, y=550, width=50)
    ttk.Radiobutton(labelFrame, text=" 18+ ",variable = Var2, value = " 18+ ").place(x=500, y=550, width=50)


    #Prömiyer
    lb14 = Label(labelFrame, text="Prömiyer : ", bg='black', fg='white', font=('Courier', 11))
    lb14.place(x=0, y=600, height=15)

    listbox = Listbox(labelFrame, bg='#F0F8FF', font=('arial', 12, 'normal'), width=40, height=8)

    listbox.insert('0', 'Sonbahar-2021')
    listbox.insert('1', 'Yaz-2021')
    listbox.insert('2', 'İlkbahar-2021')
    listbox.insert('3', 'Kış-2021')

    listbox.insert('4', 'Sonbahar-2020')
    listbox.insert('5', 'Yaz-2020')
    listbox.insert('6', 'İlkbahar-2020')
    listbox.insert('7', 'Kış-2020')

    listbox.insert('8', 'Sonbahar-2019')
    listbox.insert('9', 'Yaz-2019')
    listbox.insert('10', 'İlkbahar-2019')
    listbox.insert('11', 'Kış-2019')

    listbox.insert('12', 'Sonbahar-2018')
    listbox.insert('13', 'Yaz-2018')
    listbox.insert('14', 'İlkbahar-2018')
    listbox.insert('15', 'Kış-2018')

    listbox.insert('16', 'Sonbahar-2017')
    listbox.insert('17', 'Yaz-2017')
    listbox.insert('18', 'İlkbahar-2017')
    listbox.insert('19', 'Kış-2017')

    listbox.insert('20', 'Sonbahar-2016')
    listbox.insert('21', 'Yaz-2016')
    listbox.insert('22', 'İlkbahar-2016')
    listbox.insert('23', 'Kış-2016')

    listbox.insert('24', 'Sonbahar-2015')
    listbox.insert('25', 'Yaz-2015')
    listbox.insert('26', 'İlkbahar-2015')
    listbox.insert('27', 'Kış-2015')

    listbox.insert('28', 'Sonbahar-2014')
    listbox.insert('29', 'Yaz-2014')
    listbox.insert('30', 'İlkbahar-2014')
    listbox.insert('31', 'Kış-2014')

    listbox.insert('32', 'Sonbahar-2013')
    listbox.insert('33', 'Yaz-2013')
    listbox.insert('34', 'İlkbahar-2013')
    listbox.insert('35', 'Kış-2013')

    listbox.insert('36', 'Sonbahar-2012')
    listbox.insert('37', 'Yaz-2012')
    listbox.insert('38', 'İlkbahar-2012')
    listbox.insert('39', 'Kış-2012')

    listbox.insert('40', 'Sonbahar-2011')
    listbox.insert('41', 'Yaz-2011')
    listbox.insert('42', 'İlkbahar-2011')
    listbox.insert('43', 'Kış-2011')

    listbox.insert('44', 'Sonbahar-2010')
    listbox.insert('45', 'Yaz-2010')
    listbox.insert('46', 'İlkbahar-2010')
    listbox.insert('47', 'Kış-2010')

    listbox.insert('48', 'Sonbahar-2009')
    listbox.insert('49', 'Yaz-2009')
    listbox.insert('50', 'İlkbahar-2009')
    listbox.insert('51', 'Kış-2009')

    listbox.insert('52', 'Sonbahar-2008')
    listbox.insert('53', 'Yaz-2008')
    listbox.insert('54', 'İlkbahar-2008')
    listbox.insert('55', 'Kış-2008')

    listbox.insert('56', 'Sonbahar-2007')
    listbox.insert('57', 'Yaz-2007')
    listbox.insert('58', 'İlkbahar-2007')
    listbox.insert('59', 'Kış-2007')
    listbox.place(x=200, y=600)


    # Butonlar
    gonderBtn = Button(root, text="GÖNDER", bg='#d1ccc0', fg='black',command=animeKayit)
    gonderBtn.place(x=200, y=860, width=60, height=30)

    cikisBtn = Button(root, text="ÇIKIŞ", bg='#d1ccc0', fg='black',command=root.destroy)
    cikisBtn.place(x=500, y=860, width=60, height=30)

    root.mainloop()












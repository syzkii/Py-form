from tkinter import *
import tkinter.font
from tkinter.ttk import Combobox


root = Tk()
root.geometry("370x650")


changefont = tkinter.font.Font(size=20)
judl = Label(root,text = "REGISTER",font =changefont)
judl.place(x =130,y = 10)

labelfr = LabelFrame(root,text = "Hasil",padx=20,pady=40)
labelfr.place(x = 60,y = 380)

nama = Label(root,text = "Nama :")
email = Label(root,text = "Email : ")
noTelp = Label(root,text = "No Telp : ")
password = Label(root,text = "Password : ")
password2 = Label(root,text = "Masukkan Password Lagi : ")
kebangsaan = Label(root,text = "Kebangsaan : ")
jeniskelamin = Label(root,text = "Jenis Kelamin : ")

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)
e4 = Entry(root,width=40,show="*")
e5 = Entry(root,width=40,show="*")
e6 = Entry(root,width=40)



nama.place(x = 20, y =50)
email.place(x = 20, y =90)
noTelp.place(x = 20, y =130)
password.place(x = 20, y =170)
password2.place(x = 20, y =210)
kebangsaan.place(x = 20, y =250)
jeniskelamin.place(x = 20, y =295)


e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)
e6.place(x = 20, y = 270)



r = StringVar()
r.set("none")

rb = Radiobutton(root,text = "Male",variable=r,value="male").place(x = 140,y =295 )
rb2 = Radiobutton(root,text = "Female",variable=r,value="female").place(x = 200,y =295 )



def login():
    class orang:
        def __init__(self,nama,email,noTelp,password,password2,kebangsaan,jeniskelamin):
            self.nama = nama
            self.email = email
            self.noTelp = noTelp
            self.password = password
            self.password2 = password2
            self.kebangsaan = kebangsaan
            self.jeniskelamin = jeniskelamin
        def hasil(self):
            lbl = Label(labelfr,text="Nama = "+self.nama+"\nEmail = "+self.email+"\nNo Telp ="+self.noTelp+"\nPassword = "+self.password+"\nMasukkan Password Lagi ="+self.password2+"\nKebangsaan ="+self.kebangsaan+"\nJenis Kelamin ="+self.jeniskelamin).grid()
    ditampilkan = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(), r.get())
    ditampilkan.hasil()



btn = Button(root,text = "Register",command=login).place(x = 150,y = 350)

root.mainloop()

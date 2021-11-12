from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from tkinter.font import BOLD
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_Generator | Developed by Siddhartha Routhu")
        self.root.resizable(False,False)

        title=Label(self.root,text="Qr code Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

        #=====STUDENT DETAILS WINDOW=====
        #====Variables====

        self.var_Std_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_college=StringVar()

        Std_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Std_Frame.place(x=50,y=100,width=500,height=380)

        Std_title=Label(Std_Frame,text="Student Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_Std_code=Label(Std_Frame,text="Student Reg.No :-",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(Std_Frame,text="Name :-",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(Std_Frame,text="Department :-",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_university=Label(Std_Frame,text="College/University Name :-",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_university=Entry(Std_Frame,font=("times new roman",15),textvariable=self.var_Std_code,bg='lightyellow').place(x=260,y=60)
        txt_name=Entry(Std_Frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=260,y=100)
        txt_department=Entry(Std_Frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=260,y=140)
        txt_university=Entry(Std_Frame,font=("times new roman",15),textvariable=self.var_college,bg='lightyellow').place(x=260,y=180)

        btn_generate=Button(Std_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=87,y=250,width=173,height=30)
        btn_clear=Button(Std_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=290,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(Std_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #=====STUDENT QRcode WINDOW=====
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        Std_title=Label(qr_Frame,text="Student QR code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)


        self.qr_code=Label(qr_Frame,text='No QR \nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_Std_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_college.set('')

        self.msg=''
        self.lbl_msg.config(text=self.msg)

        self.qr_code.config(image='')

    def generate(self):
        if self.var_college.get()=='' or self.var_Std_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='':
            self.msg='All Fields are required...!'
            self.lbl_msg.config(text=self.msg,fg='red')
            self.qr_code.config(image='')

        else:
            qr_data=(f"Student Reg.No: {self.var_Std_code.get()}\nName: {self.var_name.get()}\nDepartment: {self.var_department.get()}\nCollege/University Name: {self.var_college.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("PYPROJECT/QR/Std_"+str(self.var_Std_code.get())+'.png')
            #===QRcode Image update====
            self.im=ImageTk.PhotoImage(file="PYPROJECT/QR/Std_"+str(self.var_Std_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #===UPDATING NOTIFICATION===
            self.msg='QRcode Generated Successfully...!'
            self.lbl_msg.config(text=self.msg,fg='green')


root=Tk()
obj =Qr_Generator(root)
root.mainloop()

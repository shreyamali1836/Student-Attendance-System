from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face2 import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Student_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")

        
        # bg img 
        img=Image.open(r"images\bg2.jpg")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="HOSTEL ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # student button
        img4=Image.open(r"images\std1.jpg")
        img4=img4.resize((230,230))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=140,width=230,height=230)         
        
        b1=Button(f_lbl,text="1.Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),fg="red")
        b1.place(x=200,y=340,width=230,height=40)

        # train button
        img8=Image.open(r"images\tra.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_lbl,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=500,y=140,width=230,height=230)         
        
        b1=Button(f_lbl,text="2.Train",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),fg="red")
        b1.place(x=500,y=340,width=230,height=40)


        # Detect Face button
        img5=Image.open(r"images\f_det.jpg")
        img5=img5.resize((230,230))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(f_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=800,y=140,width=230,height=230)         
        
        b1=Button(f_lbl,text="3.Detect Face",command=self.face_data,cursor="hand2",font=("times new roman",20,"bold"),fg="red")
        b1.place(x=800,y=340,width=230,height=40)

        # Attendance button
        img6=Image.open(r"images\att.jpg")
        img6=img6.resize((230,230))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_lbl,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=1100,y=140,width=230,height=230)         
        
        b1=Button(f_lbl,text="4.Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",20,"bold"),fg="red")
        b1.place(x=1100,y=340,width=230,height=40)

        
        # help face button
        img7=Image.open(r"images\hlp.jpg")
        img7=img7.resize((180,180))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_lbl,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=220,y=440,width=180,height=180)         
        
        b1=Button(f_lbl,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",17,"bold"),fg="red")
        b1.place(x=220,y=620,width=180,height=40)

        # Photos button
        img9=Image.open(r"images\det1.jpg")
        img9=img9.resize((180,180))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(f_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=520,y=440,width=180,height=180)         
        
        b1=Button(f_lbl,text="Data",cursor="hand2",command=self.open_img,font=("times new roman",17,"bold"),fg="red")
        b1.place(x=520,y=620,width=180,height=40)

        # developer button
        img10=Image.open(r"images\dev.jpg")
        img10=img10.resize((180,180))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(f_lbl,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=820,y=440,width=180,height=180)         
        
        b1=Button(f_lbl,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",17,"bold"),fg="red")
        b1.place(x=820,y=620,width=180,height=40)

        # Exit button
        img11=Image.open(r"images\exi.jpg")
        img11=img11.resize((180,180))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(f_lbl,image=self.photoimg11,cursor="hand2",command=self.exit_data,)
        b1.place(x=1120,y=440,width=180,height=180)         
        
        b1=Button(f_lbl,text="Exit",cursor="hand2",command=self.exit_data,font=("times new roman",17,"bold"),fg="red")
        b1.place(x=1120,y=620,width=180,height=40)


    def open_img(self):
        os.startfile("data")

    def exit_data(self):
        self.exit_data=tkinter.messagebox.askyesno("Face Recognation","Are you sure to exit this project",parent=self.root)
        if self.exit_data>0:
            self.root.destroy()
        else:
            return


    # ================function buttons===================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    


if __name__ == "__main__":
    root=Tk()
    obj=Student_Attendance_System(root)
    root.mainloop()
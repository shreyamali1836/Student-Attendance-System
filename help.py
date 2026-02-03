from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")

        img=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\t_bg1.jpg")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="pink")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        help_label=Label(f_lbl,text="Developer name:Pranali D. Yelavikar Sayee S. Patil Shreya V. Mali Ankita R. Ature \n if you have any queries directly contact to this number \n or do email \n Contact No:9156223455 \n Email:shreyamali22@gmail.com",font=("times new roman",18,"bold"),bg="pink")
        help_label.place(x=20,y=80,width=900,height=150)

        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
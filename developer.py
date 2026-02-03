from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")

        img=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\bgReg.jpg")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        dev_label=Label(f_lbl,text="This project is developed by Shreya,Pranali,Ankita,Sayee.\n We are Diploma students who completing there diploma 3rd year completion project.\n This poject is named as HOSTEL ATTENDANCE SYSTEM \n where the attendance will taken with the face detection.",font=("times new roman",18,"bold"),bg="pink")
        dev_label.place(x=20,y=80,width=900,height=150)

        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
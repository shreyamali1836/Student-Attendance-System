from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance System")

        img=Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\ITR\Student Attendance System\images\bg.png")
        img=img.resize((1550,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        title_lbl=Label(f_lbl,text="TRAINING DATA",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        train_btn=Button(f_lbl,text="Click here to \n train your data",command=self.train_classifer,width=20,font=("times new roman",19,"bold"),bg="blue",fg="light blue")
        train_btn.place(x=670,y=450,width=200,height=100)



    def train_classifer(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ********************train the classifier***************************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
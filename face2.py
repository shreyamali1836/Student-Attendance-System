from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Hostel Attendance System")

        img = Image.open(r"C:\Users\shery\OneDrive\Documents\DIPLOMA\CPP\Student Attendance System\images\face_bg_bg.jpg")
        img = img.resize((1550, 760))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=50, width=1550, height=760)

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        b1_1 = Button(f_lbl, text="Click here to Do Your \n Face Recognation done", command=self.face_recog, cursor="hand2",font=("times new roman", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=300, width=300, height=60)
       

    # **********attendance****************
    def mark_attendance(self, i, r, n, d):
        with open("C:/Users/shery/OneDrive/Documents/DIPLOMA/CPP/Student Attendance System/HAS.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
        
    # ****************Face_Recognition*****************
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="shreya@1836", database="shreya")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT stdid FROM student WHERE stdid="+str(id))
                i = my_cursor.fetchone()
                if i:
                    i = str(i[0])  

                my_cursor.execute("SELECT roll FROM student WHERE stdid="+str(id))
                r = my_cursor.fetchone()
                if r:
                    r = str(r[0])

                my_cursor.execute("SELECT name FROM student WHERE stdid="+str(id))
                n = my_cursor.fetchone()
                if n:
                    n = str(n[0])

                my_cursor.execute("SELECT batch FROM student WHERE stdid="+str(id))
                d = my_cursor.fetchone()
                if d:
                    d = str(d[0])
                
                if confidence > 77:
                    cv2.putText(img, f"ID:2212280081", (x, y-80),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll:36", (x, y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:Shreya", (x, y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Hostel:Chandrabhaga", (x, y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i, r, n, d)
                    
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown face:", (x, y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
       

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
